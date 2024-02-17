# Comandos Imperativos (Imperative Commands)

Los comandos imperativos son una forma rápida y directa de realizar tareas en Kubernetes sin necesidad de definir archivos de configuración YAML.

1. **Crear un Pod de manera imperativa:**
    - Comando: `kubectl run [nombre_del_pod] --image=[nombre_de_la_imagen]`
    - Propósito: Crea un nuevo pod de manera imperativa con el nombre y la imagen especificados.

2. **Exponer un servicio de manera imperativa:**
    - Comando: `kubectl expose pod [nombre_del_pod] --port=[puerto] --target-port=[puerto_destino] --name=[nombre_del_servicio]`
    - Propósito: Expone un servicio de manera imperativa para un pod específico con los puertos especificados.

3. **Escalado de replicación de un Deployment de manera imperativa:**
    - Comando: `kubectl scale deployment [nombre_del_despliegue] --replicas=[número_de_replicas]`
    - Propósito: Realiza el escalado de replicación de un deployment de manera imperativa ajustando el número de réplicas.

4. **Creación de un espacio de nombres de manera imperativa:**
    - Comando: `kubectl create namespace [nombre_del_namespace]`
    - Propósito: Crea un nuevo espacio de nombres de manera imperativa.

5. **Establecer el espacio de nombres por defecto para el contexto actual de manera imperativa:**
    - Comando: `kubectl config set-context --current --namespace=[nombre_del_namespace]`
    - Propósito: Establece de manera imperativa el espacio de nombres por defecto para el contexto actual.

6. **Creación de un servicio de manera imperativa:**
    - Comando: `kubectl create service clusterip [nombre_del_servicio] --tcp=[puerto]:[puerto_destino] --dry-run=client -o yaml > service.yaml`
    - Propósito: Crea un servicio de manera imperativa y genera la definición YAML para el servicio.

7. **Eliminación de un recurso de manera imperativa:**
    - Comando: `kubectl delete [tipo_de_recurso] [nombre_del_recurso]`
    - Propósito: Elimina un recurso específico de manera imperativa.

8. **Obtención de la configuración YAML de un recurso de manera imperativa:**
    - Comando: `kubectl get [tipo_de_recurso] [nombre_del_recurso] -o yaml > resource.yaml`
    - Propósito: Obtiene de manera imperativa la configuración YAML de un recurso específico.

9. **Actualización de un recurso de manera imperativa:**
    - Comando: `kubectl set [tipo_de_recurso] [nombre_del_recurso] --[atributo]=[nuevo_valor]`
    - Propósito: Actualiza de manera imperativa un atributo específico de un recurso.

# Comandos para trabajar con Nodos (Nodes)

1. **Obtener información sobre los nodos:**
    - Comando: `kubectl get nodes`
    - Propósito: Muestra una lista de todos los nodos en el clúster.

2. **Describir un nodo específico:**
    - Comando: `kubectl describe node [nombre_del_nodo]`
    - Propósito: Proporciona información detallada sobre un nodo específico, incluyendo detalles sobre recursos, capacidad y estado.

# Comandos para trabajar con Espacios de Nombres (Namespaces)

3. **Crear un nuevo espacio de nombres:**
    - Comando: `kubectl create namespace [nombre_del_namespace]`
    - Propósito: Crea un nuevo espacio de nombres en el clúster.

4. **Establecer el espacio de nombres por defecto para el contexto actual:**
    - Comando: `kubectl config set-context --current --namespace=[nombre_del_namespace]`
    - Propósito: Establece el espacio de nombres por defecto para el contexto actual. Los comandos subsiguientes operarán en este espacio de nombres.

5. **Obtener la configuración del espacio de nombres y guardarla en un archivo YAML:**
    - Comando: `kubectl get namespace [nombre_del_namespace] -o yaml > [nombre_del_archivo_yaml]`
    - Propósito: Obtiene la configuración del espacio de nombres especificado y guarda la información en un archivo YAML llamado team-12-namespace.yml.

# Comandos para trabajar con Pods

1. **Obtener información sobre los pods:**
    - Comando: `kubectl get pods`
    - Propósito: Muestra una lista de todos los pods en el clúster.

2. **Crear un nuevo pod:**
    - Comando: `kubectl run [nombre_del_pod] --image=[nombre_de_la_imagen]`
    - Propósito: Crea un nuevo pod con el nombre y la imagen especificados.

3. **Obtener detalles de un pod:**
    - Comando: `kubectl describe pod [nombre_del_pod]`
    - Propósito: Proporciona información detallada sobre un pod específico, incluida la imagen utilizada.

4. **Obtener información detallada sobre los nodos en los que se ejecutan los pods:**
    - Comando: `kubectl get pods -o wide`
    - Propósito: Muestra información adicional, incluido el nodo en el que se ejecuta cada pod.

5. **Eliminar un pod:**
    - Comando: `kubectl delete pod [nombre_del_pod]`
    - Propósito: Elimina un pod específico.

6. **Editar un pod para cambiar la imagen:**
    - Comando: `kubectl edit pod [nombre_del_pod]`
    - Propósito: Abre un editor para modificar la definición de un pod y realizar cambios, como cambiar la imagen utilizada.

7. **Reemplazar un recurso existente con un nuevo recurso proporcionado.**
    - Comando: `kubectl replace --force -f [nombre_del_archivo_yaml]`
    - Propósito: El comando kubectl replace se utiliza para actualizar un recurso existente en el clúster de Kubernetes con la definición de un nuevo recurso proporcionado en un archivo YAML. La opción --force indica que se debe realizar el reemplazo sin solicitar confirmación adicional.

# Comandos para trabajar con ReplicaSets

1. **Obtener información sobre los ReplicaSets:**
    - Comando: `kubectl get ReplicaSet`
    - Propósito: Muestra una lista de todos los ReplicaSets en el clúster.

2. **Crear un ReplicaSet:**
    - Comando: `kubectl create -f [nombre_del_archivo_yaml]`
    - Propósito: Crea un ReplicaSet utilizando un archivo de definición YAML.

3. **Obtener detalles de un ReplicaSet:**
    - Comando: `kubectl describe ReplicaSet [nombre_del_ReplicaSet]`
    - Propósito: Proporciona información detallada sobre un ReplicaSet específico, incluyendo la imagen utilizada para crear los pods.

4. **Eliminar un pod:**
    - Comando: `kubectl delete pod [nombre_del_pod]`
    - Propósito: Elimina un pod específico.

5. **Escalar un ReplicaSet a cinco pods:**
    - Comando: `kubectl scale --replicas=5 replicaset [nombre_del_ReplicaSet]`
    - Propósito: Escala un ReplicaSet para que tenga cinco pods en funcionamiento.

6. **Escalar un ReplicaSet a dos pods:**
    - Comando: `kubectl edit replicaset [nombre_del_ReplicaSet]`
    - Propósito: Edita un ReplicaSet y ajusta el número de réplicas a dos.

# Comandos para trabajar con Despliegues (Deployments)

1. **Verificar los despliegues existentes:**
    - Comando: `kubectl get deployments`
    - Propósito: Muestra una lista de todos los despliegues en el clúster.

2. **Crear un nuevo despliegue:**
    - Comando: `kubectl create deployment [nombre] --image=[nombre_de_la_imagen] --replicas=[número_de_replicas]`
    - Propósito: Crea un nuevo despliegue con el nombre, la imagen y el número de réplicas especificados.

# Comandos para trabajar con Services

1. **Obtener información sobre los servicios:**
    - Comando: `kubectl get service` o `kubectl get svc`
    - Propósito: Muestra una lista de todos los servicios en el clúster.

2. **Obtener el tipo del servicio predeterminado de Kubernetes:**
    - Comando: `kubectl get service <nombre_del_servicio> -n <nombre_del_namespace>`
    - Propósito: Obtiene el tipo del servicio de Kubernetes en un namespace específico.

3. **¿Cuál es el puerto de destino configurado en el servicio de Kubernetes?**
    - Comando: `kubectl describe service <nombre_del_servicio> -n <nombre_del_namespace>`
    - Propósito: Muestra información detallada del servicio, incluyendo el puerto de destino.

4. **¿Cuántas etiquetas están configuradas en el servicio de Kubernetes?**
    - Comando: `kubectl describe service <nombre_del_servicio> -n <nombre_del_namespace>`
    - Propósito: Muestra el número de etiquetas configuradas en el servicio.

5. **¿Cuántos puntos finales están conectados al servicio de Kubernetes?**
    - Comando: `kubectl describe service <nombre_del_servicio> -n <nombre_del_namespace>`
    - Propósito: Muestra el número de puntos finales conectados al servicio.

6. **¿Cuántos despliegues existen en el espacio de nombres predeterminado actual?**
    - Comando: `kubectl get deployments -n <nombre_del_namespace>`
    - Propósito: Obtiene el número de despliegues en un namespace específico.

7. **¿Cuál es la imagen utilizada para crear las cápsulas en el despliegue?**
    - Comando: `kubectl describe deployment <nombre_del_despliegue> -n <nombre_del_namespace>`
    - Propósito: Muestra la imagen utilizada para crear las cápsulas en un despliegue específico.

8. **¿Puedes acceder a la interfaz de la aplicación web?**
    - Propósito: Verifica si puedes acceder a la interfaz de la aplicación web.

9. **¿Qué se necesita hacer para acceder a la interfaz de la aplicación web?**
    - Comando: `kubectl apply -f service-definition.yaml`
    - Propósito: Crea un nuevo servicio para acceder a la interfaz de la aplicación web.

10. **¿Cuál es el nombre del nuevo servicio creado para acceder a la interfaz de la aplicación web?**
     - Comando: `kubectl get service`
     - Propósito: Obtiene el nombre del nuevo servicio creado para acceder a la interfaz de la aplicación web.

11. **¿Cuál es el tipo del nuevo servicio?**
     - Comando: `kubectl describe service web-app-service -n <nombre_del_namespace>`
     - Propósito: Obtiene el tipo del nuevo servicio creado.

12. **¿Cuál es el puerto de destino del nuevo servicio?**
     - Comando: `kubectl describe service web-app-service -n <nombre_del_namespace>`
     - Propósito: Obtiene el puerto de destino del nuevo servicio.

13. **¿Cuál es el puerto del nuevo servicio?**
     - Comando: `kubectl describe service web-app-service -n <nombre_del_namespace>`
     - Propósito: Obtiene el puerto del nuevo servicio.

14. **¿Cuál es el puerto de nodo del nuevo servicio?**
     - Comando: `kubectl describe service web-app-service -n <nombre_del_namespace>`
     - Propósito: Obtiene el puerto de nodo del nuevo servicio.

15. **¿Cuál es el nombre del selector del nuevo servicio?**
     - Comando: `kubectl describe service web-app-service -n <nombre_del_namespace>`
     - Propósito: Obtiene el nombre del selector del nuevo servicio.
