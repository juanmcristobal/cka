# kube-controllers

En Kubernetes, los`controller-manager` son componentes esenciales en Kubernetes que garantizan que el estado del clúster se mantenga de acuerdo con las especificaciones deseadas. A través de sus bucles de control, supervisan, ajustan y mantienen los recursos del clúster, lo que facilita la administración y la orquestación de aplicaciones en un entorno de Kubernetes. 

### Tipos de Controladores en Kubernetes

#### Replicaset
- Garantiza un número específico de Pods en ejecución.
- Elimina o crea Pods según sea necesario.

#### Deployment
- Ejecuta un Pod con un número deseado de réplicas.
- Permite estrategias de implementación, como actualizaciones sin tiempo de inactividad.

#### Daemonset
- Garantiza que todos o algunos nodos ejecuten una copia del Pod.
- Útil para implementar un Pod por nodo o por subconjunto de nodos.

#### Statefulset
- Adecuado para cargas de trabajo con almacenamiento persistente.
- Mantiene identidades únicas para cada Pod y gestiona eventos del ciclo de vida.

#### Job
- Supervisa Pods para tareas específicas.
- Utilizado para procesamiento por lotes.
- Los Pods no se eliminan automáticamente; debe hacerse manualmente.

#### Cronjob
- Similar a Job, pero se ejecuta según un horario definido.
- Gestiona automáticamente la creación de Jobs según la programación.

#### Controladores Personalizados
- Extienden la funcionalidad de Kubernetes.
- Permite a los desarrolladores crear comportamientos personalizados.
- Ejemplo: `kubernetes-external-secrets` para gestionar secretos externos.

#### Escritura de Controladores Personalizados
- No es necesario usar Go; se pueden usar varios lenguajes.
- Ejemplo: `kubernetes-external-secrets` está escrito en JavaScript.
- Monitorizan recursos y actúan en cambios detectados.

