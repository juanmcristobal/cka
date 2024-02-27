# Persistent Volumes

Kubernetes supports managing storage through Persistent Volumes (PV) and Persistent Volume Claims (PVC), offering a high level of abstraction to handle storage resources.

## Persistent Volumes (PV) and Persistent Volume Claims (PVC) Comparison

In Kubernetes, the concepts of PersistentVolume (PV) and PersistentVolumeClaim (PVC) work together to provide persistent storage, but they serve different purposes and operate from distinct perspectives. Below are the key differences between the two:

### PersistentVolume (PV)

- **Storage Resources:** A PV is a piece of storage in the cluster that has been provisioned by an administrator or dynamically through StorageClasses. It represents a physical resource in the underlying infrastructure, such as a disk in the cloud, NFS storage, among others.
- **Independent Lifecycle:** The lifecycle of a PV is independent of any individual pod that consumes it. This means the storage resource can survive after the pods are destroyed.
- **Managed by Administrators:** PVs are generally provisioned and managed by cluster administrators. This includes the creation, configuration, and management of the storage lifecycle policy.
- **Reclaim Policies:** PVs include policies that define what happens to the volume once the PVC is released. These policies can be Retain, Recycle, or Delete.

### PersistentVolumeClaim (PVC)

- **Storage Request:** A PVC is essentially a storage request by the user. Application developers use PVCs to request specific sizes and access modes for the storage they need for their applications.
- **User Abstraction:** PVCs provide an abstraction layer over the specific details of the physical storage. Users do not need to know where or how the PV is stored; they just need to request the size and access they require.
- **Lifecycle Tied to User:** The lifecycle of a PVC is more closely tied to the lifecycle of the pods that use it. A PVC will exist as long as it is needed for the pods and will be deleted by the user if it is no longer necessary.
- **Dynamic Binding:** A PVC can be satisfied by any PV that meets the requirements of the PVC (size, access modes, StorageClass), and this "binding" process is managed by Kubernetes dynamically.

### Direct Comparison

- **Purpose:** PV = offer of storage; PVC = request for storage.
- **Management:** PVs are managed by administrators; PVCs are requested by end-users.
- **Lifecycle:** PVs have a lifecycle independent of the pods; PVCs are designed to be used and possibly discarded by the pods.
- **Policies:** PVs can define reclaim policies; PVCs define the required size and access.
- **Allocation:** A PV is a resource in the cluster; a PVC is a ticket to utilize those resources.

In summary, PVs and PVCs are two sides of the same coin, designed to work in conjunction within Kubernetes to provide persistent storage in a manner that is secure, efficient, and easy to use for developers and system administrators.

## Persistent Volumes (PV) and Persistent Volume Claims (PVC) Description

### Persistent Volume

A Persistent Volume (PV) in Kubernetes is a piece of storage that has been provisioned by an administrator or dynamically provisioned using Storage Classes. It is a cluster resource that can be used by applications running in pods.

#### Capacity

Defines the size of the volume. It is specified when the PV is created and is important for matching PVs with Persistent Volume Claims (PVCs).

#### Access Modes

Determines how the volume can be accessed by the containers. The access modes include:

- `ReadWriteOnce (RWO)` - The volume can be mounted as read-write by a single node.
- `ReadOnlyMany (ROX)`- The volume can be mounted as read-only by many nodes.
- `ReadWriteMany (RWX)` - The volume can be mounted as read-write by many nodes.

#### Volume Modes

Specifies whether the volume is presented as a block device or a filesystem. The two modes are:

- `Block`
- `Filesystem`

A volume with `volumeMode: Filesystem` is mounted into Pods into a directory. If the volume is backed by a block device and the device is empty, Kubernetes creates a filesystem on the device before mounting it for the first time.
By default, Kubernetes uses the `Filesystem` mode for volumes. When a PersistentVolume (PV) or a PersistentVolumeClaim (PVC) is created without specifying the `volumeMode`

#### Storage Class

The StorageClass used for dynamic provisioning. It specifies the type of storage to be used and configurations like replication factor, disk type, etc.

#### Reclaim Policy

Determines what happens to the volume after it is released from its claim. Options include:

- `Retain` - The volume is kept after it is released.
- `Delete` - The volume and its data are deleted after it is released.
- `Recycle` - Deprecated.

#### Mount Options

Custom mount options that the volume should be mounted with.

#### Phase

Indicates the current phase of the Persistent Volume (e.g., Available, Bound, Released, Failed).

#### Create a Persistent Volume

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-example
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: standard
  mountOptions:
    - hard
    - nfsvers=4.1
  hostPath:
    path: "/mnt/data"
```

### Persistent Volume Claim

A PVC is a request for storage by a user. It specifies the size, access modes, and other requirements for storage.

#### Access Modes

Same as for PVs, determines how the volume can be accessed by the containers.

#### Volume Modes

Specifies whether the requested volume is a block device or a filesystem.

#### Resources

Specifies the minimum size of the volume that the claim should match.

#### Selector

Allows the claim to specify the PV to bind to using labels.

#### Class

The name of the StorageClass used for dynamic provisioning.

#### Create Persistent Volume Claim

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-example
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: standard
```

#### Use PVC in a Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-using-pvc
spec:
  containers:
  - name: my-container
    image: nginx
    volumeMounts:
    - mountPath: "/var/www/html"
      name: my-volume
  volumes:
  - name: my-volume
    persistentVolumeClaim:
      claimName: pvc-example
```

## Reclaiming

The `persistentVolumeReclaimPolicy` field controls the PV's fate once its PVC is deleted:

- `Retain`: The volume remains until manually deleted.
- `Delete`: The volume is deleted automatically with the PVC.
- `Recycle`: Deprecated in favor of dynamic provisioning.

## Dynamic Provisioning

Allows automatic creation of storage resources when a PVC is created, based on the StorageClass specifications.

## Summary

Persistent Volumes (PVs) and Persistent Volume Claims (PVCs) provide a way for users and administrators to abstract details of how storage is provided from how it is consumed. Through the use of PVs and PVCs, Kubernetes allows for storage provisioning that can be managed independently of the application using the storage.


For more detailed information, visit the official Kubernetes documentation on Persistent Volumes: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
