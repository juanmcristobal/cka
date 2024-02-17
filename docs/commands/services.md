Configuración y Creación de Recursos

Crear un Deployment en Kubernetes:

```bash
kubectl create deployment <nombre> --image=<imagen>
```

Crear un Deployment con replicas específicas:

```bash
kubectl create deployment <nombre> --replicas=<número> --image=<imagen>
```

Actualizar la imagen de un Deployment:

```bash
kubectl set image deployment/<nombre> <nombre>=<nueva-imagen>
```

Exponer un Deployment como un servicio:

```bash
kubectl expose deployment <nombre> --type=NodePort --port=<puerto>
```

Gestión de Recursos

Escalar un Deployment:

```bash
kubectl scale deployment <nombre> --replicas=<número>
```
Eliminar un Deployment:

```bash
kubectl delete deployment <nombre>
```
Ver registros de un Pod:

```bash
kubectl logs -l <selector>
```
Ejecutar un comando en un Pod:

```bash
kubectl exec -it <nombre-del-pod> -- <comando>
```

Copiar archivos desde o hacia un Pod:

```bash
kubectl cp <nombre-del-pod>:<ruta-remota> <ruta-local>
```

Ver y Depurar Recursos

Ver la información detallada de un recurso:

```bash
kubectl describe <recurso> <nombre>
```
Ver los eventos relacionados con un recurso:

```bash
kubectl get events
```
Ejecutar una shell dentro de un Pod:

```bash
kubectl exec -it <nombre-del-pod> -- /bin/sh
```
Ver la configuración de un recurso en YAML:

```bash
kubectl get <recurso> <nombre> -o yaml
```
Gestión de Estado

Reiniciar un Pod:

```bash
kubectl delete pod <nombre-del-pod>
```
Eliminar todos los Pods de un Deployment:

```bash
kubectl delete pods -l <selector>
```
Forzar la terminación de un Pod:

```bash
kubectl delete pod <nombre-del-pod> --grace-period=0 --force
```
Desencadenar un Deployment manualmente:

```bash
kubectl rollout restart deployment/<nombre-del-deployment>
```
Escalado y Balanceo de Carga

Escalar un Deployment manualmente:

```bash
kubectl scale deployment <nombre> --replicas=<número>
```
Exponer un servicio en un puerto específico:

```bash
kubectl expose deployment <nombre> --port=<puerto>
```
Crear un servicio de tipo LoadBalancer:

```bash
kubectl expose deployment <nombre> --type=LoadBalancer --port=<puerto>
```
Configurar el balanceo de carga para un servicio:

```bash
kubectl scale deployment/<nombre-del-deployment> --replicas=<número>
```
Control de Acceso y Seguridad

Crear un usuario y asignarle un rol:

```bash
kubectl create serviceaccount <nombre-del-usuario>
kubectl create clusterrolebinding <nombre-del-binding> --clusterrole=<nombre-del-rol> --serviceaccount=<nombre-del-namespace>:<nombre-del-usuario>
```
Crear un secreto a partir de un archivo:

```bash
kubectl create secret generic <nombre-del-secreto> --from-file=<clave>=<archivo>
```
Crear una regla de red para permitir el tráfico entrante:

```bash
kubectl create networkpolicy allow-traffic --pod-selector=<selector-del-pod> --namespace=<nombre-del-namespace> --ingress --port=<puerto>
```
Obtener información de un recurso concreto:

```bash
kubectl get <recurso> <nombre> -o json
```