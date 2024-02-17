# kube-apiserver

## Introducción

El **kube-apiserver** es crucial para gestionar cambios en el clúster. Autentica, valida solicitudes y actualiza datos en *etcd*, siendo el único componente que se comunica directamente con éste. Otros componentes como el *kube-scheduler*, *kube-controller-manager* y *kubelet* utilizan el kube-apiserver para realizar actualizaciones en sus áreas específicas del clúster.

### Funciones del kube-apiserver

El kube-apiserver cumple diversas funciones críticas en Kubernetes:

- **Autenticación y autorización:** Verifica la identidad de los usuarios y componentes que intentan interactuar con el clúster, y decide qué acciones están permitidas.

- **Exposición de la API:** Ofrece una interfaz RESTful que permite a los usuarios y aplicaciones acceder a los recursos y funcionalidades del clúster.

- **Validación y admisión:** Examina y valida las solicitudes de API entrantes para garantizar que cumplen con las políticas y restricciones del clúster.

- **Persistencia de recursos:** Almacena y recupera la información sobre el estado del clúster en el almacén de datos etcd.

- **Notificaciones de eventos:** Genera eventos para informar sobre cambios en el estado del clúster.
