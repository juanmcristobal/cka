# etcd

## Introducción 

`etcd` es un almacén de clave-valor distribuido utilizado en Kubernetes para almacenar configuraciones y metadatos críticos. `etcd` desempeña un papel fundamental al proporcionar un almacenamiento distribuido confiable, consistente y coordinado, lo que contribuye a la estabilidad, confiabilidad y escalabilidad de los clústeres de Kubernetes.

### Inicio Rápido con etcd

Kubeadm implementa etcd como un pod en el espacio de nombres kube-system. No obstante, si deseas probarlo de manera independiente, puedes realizar la siguiente prueba:

```shell
rm -rf /tmp/etcd-data.tmp && mkdir -p /tmp/etcd-data.tmp && \
  docker rmi gcr.io/etcd-development/etcd:v3.5.10 || true && \
  docker run \
  -p 2379:2379 \
  -p 2380:2380 \
  --mount type=bind,source=/tmp/etcd-data.tmp,destination=/etcd-data \
  --name etcd-gcr-v3.5.10 \
  gcr.io/etcd-development/etcd:v3.5.10 \
  /usr/local/bin/etcd \
  --name s1 \
  --data-dir /etcd-data \
  --listen-client-urls http://0.0.0.0:2379 \
  --advertise-client-urls http://0.0.0.0:2379 \
  --listen-peer-urls http://0.0.0.0:2380 \
  --initial-advertise-peer-urls http://0.0.0.0:2380 \
  --initial-cluster s1=http://0.0.0.0:2380 \
  --initial-cluster-token tkn \
  --initial-cluster-state new \
  --log-level info \
  --logger zap \
  --log-outputs stderr

docker exec etcd-gcr-v3.5.10 /usr/local/bin/etcd --version
docker exec etcd-gcr-v3.5.10 /usr/local/bin/etcdctl version
docker exec etcd-gcr-v3.5.10 /usr/local/bin/etcdutl version
docker exec etcd-gcr-v3.5.10 /usr/local/bin/etcdctl endpoint health
docker exec etcd-gcr-v3.5.10 /usr/local/bin/etcdctl put foo bar
docker exec etcd-gcr-v3.5.10 /usr/local/bin/etcdctl get foo
```

Más información:
[https://github.com/etcd-io/etcd/releases/tag/v3.5.10](https://github.com/etcd-io/etcd/releases/tag/v3.5.10)