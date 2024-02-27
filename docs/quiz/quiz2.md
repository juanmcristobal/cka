# Quiz - 2

1. List all pods in the current namespace, with more details
2. List Events sorted by timestamp
3. List all pods in all namespaces
4. Rolling restart of the “frontend” deployment
5. Show Merged kubeconfig settings
6. Get the documentation for pod manifests
7. Get all running pods in the namespace
8. Start a single instance of nginx
9. Rolling update “www” containers of “frontend” deployment, updating the image
10. List pods Sorted by Restart Count
11. Create a daemonset named “Prometheus-monitoring” using image=prom/Prometheus which runs in all the nodes in the cluster.

```shell
TODO
```
12. Get the deployment `nginx-deployment`rollout status 

```shell
kubectl rollout history deployment/nginx-deployment
```

13. Print pod name and start time to “/opt/pod-status” file

```shell
k get pod -A -o custom-columns=NAME:.metadata.name,START:.status.startTime>/opt/pod-status

kubectl get pod  -A -o=jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.startTime}{"\n"}{end}'

```

14. Undo the deployment to the previous version 1.17.1 and verify Image has the previous version

```shell
kubectl rollout undo deployment/deployment-nginx
```

15. Create a busybox pod and add “sleep 3600” command
16. Resume the rollout of the deployment
17. Fix a node that shows as non-ready
18. List all the pods showing name and namespace with a json path expression
19. Scale down the deployment to 1 replica
20. Create 5 nginx pods in which two of them is labeled env=prod and three of them is labeled env=dev
21. List all the pods that are serviced by the service “webservice” and copy the output in /opt/$USER/webservice.targets
22. Get list of all pods in all namespaces and write it to file “/opt/pods-list.yaml”
23. Create an nginx pod which loads the secret as environment variables

24. Update the deployment with the image version 1.16.1 and verify the image and check the rollout history


25. Create a deployment called webapp with image nginx having 5 replicas in it, put the file in /tmp directory with named webapp.yaml

26. Evict all existing pods from a node-1 and make the node unschedulable for new pods.

27. Create a hostPath PersistentVolume named task-pv-volume with storage 10Gi, access modes ReadWriteOnce, storageClassName manual, and volume at /mnt/data and verify

28. Create a Pod nginx and specify a CPU request and a CPU limit of 0.5 and 1 respectively

29. Create a nginx pod with label env=test in engineering namespace


30. Create a configmap called myconfigmap with literal value appname=myapp


31. Create a pod with environment variables as var1=value1.Check the environment variable in pod

32. List all the pods sorted by created timestamp

33. Create nginx image pods in which one of them is labelled with env=prod

34. Add a taint to node “worker-2” with effect as “NoSchedule” and list the node with taint effect as “NoSchedule”
```shell
TODO
```

35. Delete the above pod and create again from the same yaml file and verifies there is no “test-file.txt” in the path /data/redis (Since non-persistent storage “emptyDir” is used).

36. Change the label for one of the pod to env=uat and list all the pods to verify


37. List “nginx-dev” and “nginx-prod” pod and delete those pods

38. List all the pods sorted by name

39. Create an nginx pod and set an env value as ‘var1=val1’. Check the env value existence within the pod

40. Get list of all the nodes with labels

41. Get list of persistent volumes and persistent volume claim in the cluster

42. Create a ETCD backup of kubernetes cluster Note :You don’t need to memorize command, refer – https://kubernetes.io/docs/tasks/administer-cluster/configureupgrade-etcd/ during exam

43. Update the deployment with the image version 1.17.4 and verify

44. Create a redis pod, and have it use a non-persistent storage Note: In exam, you will have access to kubernetes.io site, Refer : https://kubernetes.io/docs/tasks/configure-pod-container/configurevolume-storage/


45. Change the Image version to 1.15-alpine for the pod you just created and verify the image version is updated.
46. Check the Image version of nginx-dev pod using jsonpath
47. Print all pod name and all image name and write it to a file name “/opt/pod-details.txt”
48. Create a redis pod, and have it use a non-persistent storage (volume that lasts for the lifetime of the Pod)
49. Scale the deployment to 5 replicas
50. Create a Job with an image node which prints node version and verifies there is a pod created for this job
51. Create a NetworkPolicy which denies all ingress traffic
52. Get list of PVs and order by size and write to file – /opt/pvlist.txt
53. Check the history of the specific revision of that deployment
54. Check the image version in pod without the describe command
55. List all the events sorted by timestamp and put them into file.log and verify
56. Set CPU and memory requests and limits for existing pod name “nginx-prod”. Set requests for CPU and Memory as 100m and 256Mi respectively Set limits for CPU and Memory as 200m and 512Mi respectively
57. Delete persistent volume and persistent volume claim
58. Create a nginx pod that will be deployed to node with the label “gpu=true”

59. Clean the cluster by deleting deployment and hpa you just created
60. Apply the autoscaling to this deployment with minimum 10 and maximum 20 replicas and target CPU of 85% and verify hpa is created and replicas are increased to 10 from 1
