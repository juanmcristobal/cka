1. Print the names of all deployments in the starwars namespace in the following format: DEPLOYMENT CONTAINER_IMAGE PULL_POLICY READY_REPLICAS NAMESPACE. The data should be sorted by the increasing order of the deployment name.
    - Example of the result: DEPLOYMENT CONTAINER_IMAGE PULL_POLICY READY_REPLICAS NAMESPACE deploy0 nginx:alpine Always 1 admin2406

2. A kubeconfig file called admin.kubeconfig has been created in /tmp/CKA-exam. Investigate what's wrong with the configuration based on netstat command results to ensure all required services are correctly running in the cluster.

3. You have access to multiple clusters from your main terminal through kubectl contexts. Write all those context names into /opt/course/1/contexts. Next, write a command to display the current context into /opt/course/1/context_default_kubectl.sh using kubectl. Finally, write a second command doing the same thing into /opt/course/1/context_default_no_kubectl.sh, but without the use of kubectl.

4. Use context: kubectl config use-context k8s-c1-H. Create a single Pod of image httpd:2.4.41-alpine in Namespace default named pod1 with the container named pod1-container. This Pod should only be scheduled on a master node. Explain why Pods are by default not scheduled on master nodes in /opt/course/2/master_schedule_reason.

5. There are two Pods named o3db-* in Namespace project-c13. Scale the Pods down to one replica to save resources and record the action.

6. There are various Pods in all namespaces. Write a command into /opt/course/5/find_pods.sh which lists all Pods sorted by their AGE (metadata.creationTimestamp). Write a second command into /opt/course/5/find_pods_uid.sh which lists all Pods sorted by field metadata.uid using kubectl sorting for both commands.

7. In Namespace default, create a single Pod named ready-if-service-ready of image nginx:1.16.1-alpine. Configure a LivenessProbe which simply runs true.

8. Using the same pod definition from the previous question, configure a ReadinessProbe to check if the URL http://service-am-i-ready:80 is reachable using wget -T2 -O- http://service-am-i-ready:80. Confirm the Pod isn't ready because of the ReadinessProbe and specify the required modifications to the pod manifest.

9. The metrics-server hasn't been installed yet in the cluster. Write the kubectl commands to show node resource usage and Pod and their containers resource usage into /opt/course/7/node.sh and /opt/course/7/pod.sh, respectively.

10. With the following nodes running in a Kubernetes cluster, temporarily stop the kube-scheduler on the master node. Create a single Pod named manual-schedule of image httpd:2.4-alpine and manually schedule that Pod on node cluster2-master1 ensuring it's running.

11. Discuss the types of selectors that can be used to select objects with a given label.

12. Clarify whether a Service can have its own IP address.

13. Explain what a service uses to logically group a set of Pods.

14. Identify the default Service Type in Kubernetes.

15. Confirm whether we can manage the application from the CLI which we deployed using the GUI (Dashboard).

16. Determine which subcommand of 'kubectl' is needed to look at an object's details.

17. Debate whether in Kubernetes, we must create the Deployment first, and the respective Service later.

18. Discuss whether inside a Pod, a volume is shared among containers.

19. Identify a valid Volume type in Kubernetes.

20. Explain how Persistent Volumes can be provisioned.

21. Identify which sub-command of 'kubectl' can be used to scale an application.

22. Discuss whether defining the Pod, we can give a logical name to a port in a Deployment.

23. Confirm whether we can change the port number while forwarding requests from a Service to connected Pods.

24. Discuss the OSI model layer on which the ingress controller creates a Load Balancer.

25. Explore what can be used to access an application running inside Kubernetes from the external world.

26. List the features provided by Ingress.

27. Identify what objects can be restricted with the Object Count Quota.

28. Discuss whether we cannot roll back a Deployment.

29. Define what Helm is.

30. Highlight a crucial feature of Kubernetes.

31. Identify which components of the Kubernetes control plane serve the Kubernetes API using JSON over HTTP.

32. Discuss the Kubernetes setting that defines the image is pulled every time the pod is started.

33. Identify which component of the Kubernetes control plane selects which node an unscheduled pod runs on, based on resource availability.

34. Discuss on which Kubernetes objects Labels can be attached.

35. Identify which component in Kubernetes is an implementation of a network proxy and a load balancer.

36. Discuss which Kubernetes service helps in restricting the service within the cluster.

37. Identify which component of the Kubernetes control plane is a persistent, lightweight, distributed, key-value data store developed by CoreOS that reliably stores the configuration data of the cluster.

38. Discuss which Kubernetes service exposes the service on a static port on the deployed node.

39. Clarify what should be the value of the -register-node flag for Kubernetes master to register the node automatically.

40. Identify which storage system is not supported by Kubernetes.

41. Discuss which Kubernetes pod can be simply created with the kubectl run command.

42. Identify which components of the Kubernetes control plane is a reconciliation loop that drives the actual cluster state towards the desired cluster state.

43. Discuss which component in Kubernetes is responsible for the running state of each node.

44. Identify which of the following Kubernetes daemon embeds the core control loops.

45. Discuss the default port allocated to the API server.

46. Identify the preferred Kubernetes object to manage stateful applications.

47. Confirm whether Kubernetes implements its own networking model.

48. Define the framework that takes advantage of CustomResourceDefinitions to manage applications running inside a Kubernetes cluster.

49. Identify the base Kubernetes object for running workloads.

50. Discuss the name of the object used, in conjunction with a controller, to manage incoming traffic to workloads.

51. Confirm whether Kubernetes is secured by default.

52. List the benefits of doing container orchestration.

53. Confirm whether Kubernetes can be configured in a multi-master configuration.

54. Discuss the implications for a single master node cluster if just the master node dies.

55. Clarify whether kubelet and kube-proxy also run on the master nodes.

56. Identify which component of the Control Plane can communicate directly with the Key/Value store, which stores cluster state.

57. Discuss whether we can run containers of the same Pod on different nodes.

58. Identify which Container Network Specification Kubernetes uses.

59. Define what is referred to as the Core API Group in the API Server.

60. Discuss which process access management is responsible for implementing policies.

61. Lab Environment: Address the issue with worker node k8s-node-01 being in Not Ready state and perform necessary steps to make k8s-node-01 available again.

62. Set the node named k8s-node-1 as unavailable and reschedule all the pods running on it.

63. Lab Environment: Taint the node k8s-node-01 with key equals to env, value equals to qa, and set a hard effect to avoid
