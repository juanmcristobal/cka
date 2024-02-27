1. Create a busybox pod that runs the command "env" and save the output to "envpod" file.
2. Watch the job that runs 10 times one by one and verify 10 pods are created and delete those after it’s completed.
3. List all the pods sorted by name.
4. Undo/Rollback deployment to specific revision "1".
5. Create an nginx pod and load environment values from the above configmap "keyvalcfgmap" and exec into the pod and verify the environment variables and delete the pod.
6. Create a Cronjob with busybox image that prints date and hello from Kubernetes cluster message for every minute.
7. Create an nginx pod and list the pod with different levels of verbosity.
8. Check the history of deployment.
9. List all service account and create a service account called "admin".
10. Get the pods with labels env=dev and env=prod and output the labels as well.
11. List all configmap and secrets in the cluster in all namespace and write it to a file /opt/configmapsecret.
12. Create an nginx pod with container Port 80 and it should only receive traffic only if it checks the endpoint / on port 80 and verify and delete the pod.
13. Create a job named "hello-job" with the image busybox which echos "Hello I’m running job".
14. Get the pods with label env=dev and output the labels.
15. Expose deployment as service named "myservice".
16. Label a node as app=test and verify.
17. Scale the deployment from 5 replicas to 20 replicas and verify.
18. List the nginx pod with custom columns POD_NAME and POD_STATUS.
19. Create an nginx pod with containerPort 80 and with a PersistentVolumeClaim "task-pv-claim" and has a mount path "/usr/share/nginx/html".
20. Change the Image version back to 1.17.1 for the pod you just updated and observe the changes.
21. Get the list of pods of webapp deployment.
22. Get all the pods with label "env".
23. Get the memory and CPU usage of all the pods and find out top 3 pods which have the highest usage and put them into the cpuusage.txt file.
24. Check the rollout history and make sure everything is ok after the update.
25. Create a secret mysecret with values user=myuser and password=mypassword.
26. Create a Pod with three busybox containers with commands "ls; sleep 3600;", "echo Hello World; sleep 3600;", and "echo this is the third container; sleep 3600" respectively and check the status.
27. Pause the rollout of the deployment.
28. Get the number of schedulable nodes and write to a file /opt/schedulable-nodes.txt.
29. Create a deployment named "myapp" that having 2 replicas with nginx.
30. Get list of PVs and order by size and write to file "/opt/pvstorage.txt".
31. Make the node schedulable by uncordon the node.
32. Get IP address of the pod – "nginx-dev".
33. Create a pod with image nginx called nginx and allow traffic on port 80.
34. Check logs of each container that "busyboxpod-{1,2,3}".
35. Create a redis pod and expose it on port 6379.
36. Get the DNS records for the service and pods for the deployment redis and put the value in /tmp/dnsrecordpod and /tmp/dnsrecord-service.
37. View certificate details in /etc/kubernetes/pki.
38. Delete the pod without any delay (force delete).
39. Annotate the pod with name=webapp.
40. Create a pod with init container which waits for a service called "myservice" to be created. Once the init container completes, the myapp-container should start and print a message "The app is running" and sleep for 3600 seconds.
41. Deploy a pod with image=redis on a node with label disktype=ssd.
42. Create a file called "config.txt" with two values key1=value1 and key2=value2. Then create a configmap named "keyvalcfgmap" and read data from the file "config.txt" and verify that configmap is created correctly.
43. Deployment:
    - Create a deployment of webapp with image nginx:1.17.1 with container port 80 and verify the image version.
44. Create a namespace called ‘development’ and a pod with image nginx called nginx on this namespace.
45. Create a Pod with main container busybox which executes this "while true; do echo ‘Hi I am from Main container’ >> /var/log/index.html; sleep 5; done" and with a sidecar container with nginx image which exposes on port 80. Use an emptyDir Volume and mount this volume on path /var/log for busybox and on path /usr/share/nginx/html for nginx container. Verify both containers are running.
46. Create the nginx pod with version 1.17.4 and expose it on port 80.
47. Modify "hello-job" and make it run 10 times one after another and 5 times with parallelism: 5.
48. Get a list of all the pods showing name and namespace with a jsonpath expression.
49. Create a pod in a specific node (node1) by placing the pod definition file in a particular folder "/etc/kubernetes/manifests".
50. Create a pod with an init container which creates a file "test.txt" in "workdir" directory. Main container should check if the file "test.txt" exists and execute sleep 9999 if the file exists.
51. List pod logs named "frontend" and search for the pattern "started" and write it to a file "/opt/errorlogs".
52. Remove taint added to node "worker-2".
53. Create a pod that echoes "hello world" and then exits. Have the pod deleted automatically when it’s completed.
54. Create a pod that having 3 containers in it? (Multi-Container).
55. Create a PersistentVolumeClaim of at least 3Gi storage and access mode ReadWriteOnce and verify status is Bound.
56. Create an nginx pod which reads username as the environment variable.
57. Create a busybox pod which executes this command sleep 3600 with the service account admin and verify.
58. Undo the deployment with the previous version and verify everything is Ok.
