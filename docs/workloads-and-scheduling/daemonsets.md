# DaemonSets
DaemonSets are a resource in Kubernetes that ensure one or several copies of a Pod run on all (or some) nodes in the cluster. They are particularly useful for deploying infrastructure tasks that need to run on every node, such as log collection, monitoring, or any service that needs to be deployed on each node of the cluster.

### What Does a DaemonSet Do?

A DaemonSet ensures that all (or some) Nodes run a copy of a Pod. As nodes are added to the cluster, Pods are added to them. Similarly, as nodes are removed from the cluster, those Pods are garbage collected. Deleting a DaemonSet will clean up the Pods it created.

### Common Use Cases

- **Monitoring and Logging**: Deploy monitoring and logging tools across every node.
- **Security**: Deploy security agents on every node.
- **Storage**: Deploy software that is part of a distributed storage system.

### Practical Example of a DaemonSet

Let's create a DaemonSet that deploys an Nginx web server Pod on every node of the cluster.

1. **DaemonSet Definition**: Create a file named `nginx-daemonset.yaml` with the following content:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: nginx-daemonset
  namespace: default
spec:
  selector:
    matchLabels:
      name: nginx
  template:
    metadata:
      labels:
        name: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
```

This YAML file defines a DaemonSet named `nginx-daemonset`, which will deploy containers based on the latest Nginx image on each node of the cluster.

2. **Deploying the DaemonSet**: To deploy this DaemonSet, run the following command in your terminal:

```shell
kubectl apply -f nginx-daemonset.yaml
```

3. **Verification**: To verify that the DaemonSet Pods have been deployed on all nodes, you can use the following command:

```shell
kubectl get pods -o wide -l name=nginx
```

This command lists all Pods with the `name=nginx` label, allowing you to see on which nodes they have been deployed.

### Cleanup

To remove the DaemonSet and its associated Pods, run:

```shell
kubectl delete daemonset nginx-daemonset
```

This command deletes the DaemonSet and all the Pods it created in the cluster.

### Official Documentation

For more information about DaemonSets and their capabilities, refer to the official Kubernetes documentation:

- DaemonSets Documentation: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/

This example provides you with a foundation on how to use DaemonSets in Kubernetes to ensure Pods run on all or some nodes of your cluster. Experiment by modifying the YAML file to familiarize yourself more with the available options and how they affect your DaemonSet's behavior.
