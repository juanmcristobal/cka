1. Create a deployment named Nagari that runs the busybox image and expose port 8080, has 5 replicas and executes the command echo “Hello World”. Use imperative commands.
2. Create a nginx pod with label env=test in engineering namespace.
3. Create a pod that echo “hello world” and then exists. Have the pod deleted automatically when it‘s completed.
4. List nginx-dev and nginx-prod pods and delete those pods.
5. Create a pod with image nginx called nginx and allow traffic on port 80.
6. Create a namespace called ‘development‘ and a pod with image nginx called nginx on this namespace.
7. Get list of all the pods showing name and namespace with a jsonpath expression.
8. Check the image version in pod without the describe command.
9. From the pod label name=cpu-utilizer, find the pod consuming most CPU.
10. Create and configure the service front-end-service so it‘s accessible through NodePort and routes to the existing pod named front-end. Assume front-end pod is exposing port 80.
11. List pod logs named frontend and search for the pattern "started" and write it to a file /opt/error-logs.
12. List the nginx pod with custom columns POD_NAME and POD_STATUS.
13. List all persistent volumes sorted by capacity, saving the full kubectl output to /opt/exam/volume_list.
14. Create a job that calculates pi to 2000 decimal points using the container with the image named perl and the following commands issued to the container: ["perl", "-Mbignum=bpi", "-wle", "print bpi(2000)"]. Once the job has completed, check the logs and export the result to pi-result.txt.
15. Create a new service account with the name podviewer.
16. Create a ClusterRole named podviewer-role that can list persistent volumes.
17. Create a role binding named podviewer-role-binding that grants the cluster role you created in the previous question with the service account podviewer.
18. Create a role named pod-reader which grants read access to pods in the colmenajero namespace.
19. Use imperative commands to create a role named pod-reader which grants read access to pods in the colmenajero namespace.
20. Bind the previously created pod-viewer role to a user named John in the colmenarejo namespace.
21. Deploy a pod named nginx-pod using the nginx:alpine image.
22. Deploy a pod named spectrum using the nginx:alpine image with the labels set to gametype=arcade. Use imperative commands.
23. Get the list of pods with label gametype=arcade in the default namespace.
24. Create a namespace named videogames. Use the shortcut available for namespaces to create the namespace.
25. Get a list of all nodes in the cluster in JSON format and store it in /opt/CKA/nodes.json.
26. Use selectors to get all pods with a videogames value in the metadata.namespace attribute. Consider that the pods could be deployed in non-default namespaces.
27. Expose the spectrum pod you created in previous questions by creating a service named spectrum-service to expose the spectrum application within the cluster on port 6379. Select the two valid answers.
28. Create a deployment named tetris-web-app using the image ckaexa/tetris-webapp with 4 replicas.
29. Create a yaml file called runtime-secret.yaml for a secret called runtime-user-pass. The secret has two fields: username and password. The username should be admin and the password should be supersecret. You must provide the values of the secret directly in the imperative command and generate runtime-secret.yaml from there.
30. Create a secret that will store container environment variables and will be later used for creating a pod with that secret. The values in the secret must be admin for the username key and supersecret for the password key. Use a file and kubectl apply instead of using imperative commands.
31. Create a pod named secret-pod with a container named busybox using busybox image, and use the previously created secret (named mysecret) to add it to the container env variables. The container must execute a command to print the environmental variables so you can check the secret has been correctly configured.
32. Create a static pod named static-nginx on the controlplane node that uses nginx image and the command echo “hello control plane”.
33. There is a new application named orange that has been recently deployed. There is an issue with the application and the pod status is Init:CrashLoopBackOff. A CKA admin has provided you the following information coming from a kubectl describe po orange command. Identify and fix the issue.
34. List all the pods sorted by created timestamp.
35. You have been requested to upgrade the control plane node named k8s-control. Which commands you should use to drain the control plane so you can perform the upgrade?
36. Which command should you use to generate the command required to join a node to a cluster by using a token previously generated with kubeadm token generate?
37. Create a multicontainer pod named multi-pod. The first container is named redis and uses the redis image. Also, it will listen on port 6369. The second container is named frontend and uses a django image listening on pod 8000. Which spec template is the right one for that container?
38. Create a pod named security-context-demo-4 using gcr.io/google-samples/node-hello:1.0 that is allowed to modify system time.
39. Label a node named k8s-worker2 with the value core-services=false.
40. Create a pod named runAsPod that has a container named busybox1000 and runs all processes as user 1000 and as group 3000. The pod will execute the following command: sleep 4800.
41. You have created a mongo-db deployment and a mongo-db service that is exposing the database on port 27017 using a ClusterIP type.
42. You want to forward the local port 28015 to the service port. Which command could you execute? (select two)
43. Create a pod named dummy-pod that outputs some data to the host using a volume. The pod must use image busybox and should mount the volume in /output/.
44. You have created a multicontainer pod with two containers named multi-pod. One of the containers is named test and the other one prod. You want to list the files in the root folder of the test container, which command should you use?
45. You have created a pod named milena with the wrong image name. You‘ve realized about your mistake and want to remove the pod as soon as possible. Which command you should use?
46. You have created a deployment named condor. The deployment currently has 3 replicas but you have identified the need to scale it out to 5. Which imperative command could you use?
47. Create a pod named frontend with a container named app that requests 64 megabytes of memory but can only use up to 128 megabytes.
48. Create a pod that creates a file in /tmp, then will wait 20 seconds, remove the file, and wait another 300 seconds. You need to configure a livenessProbe that will monitor the file in /tmp/alive and throw a warning if it‘s removed. The probe will be executed every 7 seconds.
49. You have created a deployment named nginx using nginx:1.8 as the image. You have been asked to do an update to nginx:1.9.1. Which command should you execute?
50. List the InternalIP of all nodes of the cluster. Save the result to a file /root/exam/node_ips.
51. We have deployed a new pod called np-test-1 and a service called np-test-service. Incoming connections to this service are not working. Troubleshoot and fix it. Create NetworkPolicy, by the name ingress-to-nptest that allows incoming connections to the service over port 80.
52. List the DNS IP address(s) used by all pods in ALL namespaces. Save the output to /tmp/nameservers.txt.
53. You need to create a multi-container with two containers: Container 1, name: ying, image: redis. Container 2, name: yang, image: busybox. You also need to configure the following environment variables: Container 1: name: future. Container 2: name: past. Container 2 should execute sleep 3000 command. Select the right solution manifest to create such multi-container pod.
54. A new pod called goku-pod has been deployed in the default namespace and exposed through a service called freezer-svc. For some reason incoming connections to this service are not working. In order to fix it you need to create NetworkPolicy, by the name ingress-to-freezersvc that allows incoming connections to the service over port 80. Select the right manifest to achieve that.
55. List out all the iptables rules defined for ALL services running in the cluster. Save the output to /tmp/fw-rules.txt.
56. Which command would you use to show all the DaemonSets in the cluster?
57. Which command would you use to list ALL nodes in the cluster?
58. Which command would you use to show the pod names and labels?
59. Deploy an Ingress resource called video-svc-ingress with the following configuration: backend path: /streaming, backend service: streaming-service, backend port: 8080, hostname: streaming.example.com, backend path: /live, backend service: livevideo-service, backend port: 9000, hostname: livevideo.example.com.
60. Create a NetworkPolicy called allow-port which allows access ONLY to port 8080. The pods must meet the following criteria: 1. They CANNOT communicate on any port other than 8080. 2. Pods running in ALL other namespaces can also access port 8080.
61. Create a pod called facebook using nginx image. It should be accessible on local port 80 as well as on node‘s port. Make sure the port should be same for all nodes in the cluster.
62. You have been asked to create a pod named db-storage using the redis:alpine image. Create the pod manifest using imperative commands and redirect the output to a db-storage.yaml file. After that, mount a volume named tmp-volume with type emptyDir in /data/db.
63. A pod definition file has been created in /tmp/pod-use-pv.yaml. Also, there is a persistent volume already created in the cluster named pv-1. You have been asked to create a persistentVolume claim named my-pvc so it can be later used to binding the pv-1 to the pod.
64. Taking into account the previous question data, modify the pod manifest to mount pv-1 using the mountPath: /data and the persistentVolumeClaim we created in the previous question (my-pvc).
65. Create a new deployment called nginx-dp, with image nginx:1.19 and 2 replicas. Record the version. Next, upgrade the deployment to version 1.21 using rolling update. Make sure that the version upgrade is recorded in the resource annotation.
66. Taking into account the previous question scenario, perform a rollback of the update you made.
