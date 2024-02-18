# Deployments in Kubernetes

Deployments in Kubernetes are a powerful tool for managing container-packed applications, enabling automatic updates, rollbacks, scaling, and much more. Below, we detail how to manage Deployments for various use cases.

## Creating a Deployment

To deploy an application in Kubernetes and ensure its Pods are managed by a ReplicaSet in the background, you can use two approaches: declarative (using a YAML file) or imperative (using a command). Below, both methods are detailed for deploying an Nginx server as an example.

- **Define the Deployment in a YAML file:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: nginx-deployment
  name: nginx-deployment
spec:
  replicas: 3  # Specifies the desired number of replicas
  selector:
    matchLabels:
      app: nginx-deployment
  template:
    metadata:
      labels:
        app: nginx-deployment
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80  # The port the container exposes

```
This YAML specifies a Deployment that manages a set of Pods. Each Pod runs a container based on the Nginx 1.14.2 image. The `replicas: 3` line indicates that three replicas of the Pod should be maintained at all times.

- **Apply the Deployment:**
After defining your Deployment in a YAML file, use `kubectl` to create it in your Kubernetes cluster:

```shell
kubectl apply -f nginx-deployment.yaml
``` 
This command tells Kubernetes to make the cluster's state match the desired state described in the `nginx-deployment.yaml` file.

!!! note

    Alternatively, you can create a Deployment imperatively using a single kubectl command. This method is quicker for simple deployments or for testing purposes:

    ```kubectl create deployment nginx-deployment --image=nginx:1.14.2 --replicas=3```

- **Check the [Rollout 📝](./deployments-rollouts.md#monitoring-rollouts) status:**

```shell
kubectl rollout status deployment/nginx-deployment
```

## Updating a Deployment

To update the Pods to a new state, modify the pod specification in the Deployment. This creates a new ReplicaSet and begins moving the Pods to the new state at a controlled rate.

- **Update the container image in your Deployment file or use kubectl:**

```shell
kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1
```

- **Each new ReplicaSet updates the revision of the Deployment, which you can verify with:**

```shell
kubectl rollout history deployment/nginx-deployment
```

## [Rolling Back a Deployment 📝](./deployments-rollouts.md#managing-rollback)

If the current state is not stable, you can rollback to a previous revision of the Deployment:

- **Find the revision to rollback to:**

```shell
kubectl rollout history deployment/nginx-deployment
```

- **Rollback the Deployment to a previous revision:**

```shell
kubectl rollout undo deployment/nginx-deployment --to-revision=<revision>
```

## Scaling a Deployment

To handle more load, you can increase the number of replicas of the Deployment:

```shell
kubectl scale deployment/nginx-deployment --replicas=5
```

## [Pausing/Resuming a Rollout 📝](./deployments-rollouts.md#pausing-and-resuming-rollouts)

During a Deployment's rollout, you might find the need to temporarily halt the update process. This could be due to a discovered issue that requires immediate attention or to batch several updates together before continuing the rollout. Kubernetes allows you to pause and later resume the rollout process of a Deployment. This feature is particularly useful for managing and controlling the rollout process more granitcally.

### Pausing the Rollout

Pausing a rollout prevents any further updates to the Pods managed by the Deployment, but it does not affect the Pods that have already been updated. To pause the ongoing rollout of a Deployment, use the following command:

```shell
kubectl rollout pause deployment/nginx-deployment
```

This command will halt the rollout process for the `nginx-deployment` Deployment, allowing you to perform necessary updates, fixes, or changes to the Deployment's pod template (`spec.template`) without triggering a new rollout for each change.

#### Resuming the Rollout

After applying the necessary changes and ensuring that everything is set correctly, you can resume the rollout to start updating Pods with the new configuration. To resume a paused rollout, use the following command:

```shell
kubectl rollout resume deployment/nginx-deployment
```


## Using the Deployment's Status as an Indicator

If a [Rollout 📝](./deployments-rollouts.md) has stuck, the Deployment's status can indicate it. Check the status and events of the Deployment to diagnose issues:

```shell
kubectl describe deployment/nginx-deployment
```

## Cleaning Up Old ReplicaSets

Deployments can leave behind old ReplicaSets that are no longer needed. You can manually clean up these resources or adjust the Deployment's policies to do it automatically.

- **List all ReplicaSets:**

```shell
kubectl get rs
```

- **Delete the ReplicaSets you no longer need:**

```shell
kubectl delete rs <replicaset-name>
```

To automatically manage the cleanup of old ReplicaSets, adjust `spec.revisionHistoryLimit` in your Deployment to the desired number of ReplicaSets history to keep.

### Conclusion

Deployments in Kubernetes offer a robust mechanism for deploying, updating, and scaling applications, as well as for safely rolling back to previous states. Effectively using these capabilities can significantly improve the lifecycle management of your applications in Kubernetes.

For more information and detailed guides, consult the official Kubernetes documentation: [https://kubernetes.io/docs/concepts/workloads/controllers/deployment/](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
