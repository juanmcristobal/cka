To manage Certificate Signing Requests (CSRs) for a normal user in Kubernetes, it's crucial to first understand what a CSR is and how it functions within the context of Kubernetes. A CSR is a request sent from an applicant to a Certificate Authority (CA) to obtain a digital certificate. In Kubernetes, this process is used for authentication and the creation of certificates that enable secure communication between users and services within the cluster.

Here's a step-by-step example on how to generate a CSR for a normal user and submit it to Kubernetes for signing, which is a common task for administrators preparing the environment for users or services.

### Step 1: Create a configuration file for the user

First, you need to generate a key pair (public and private) for the user. We'll use `openssl` for this purpose. Ensure you have `openssl` installed on your machine.

```bash
openssl genrsa -out user.key 2048
```

Next, create a CSR using the user's private key. During this step, you will specify the username and the group the user will belong to in the `subject` field of the CSR.

```bash
openssl req -new -key user.key -out user.csr -subj "/CN=user/O=group"
```

Where `user` is the username, and `group` is the group the user will belong to.

### Step 2: Create the CSR in Kubernetes

Before you can submit the CSR to Kubernetes, you need to encode it in base64 and create a CSR manifest in Kubernetes.

```bash
cat user.csr | base64 | tr -d "\n"
```

Create a YAML file (`user-csr.yaml`) with the content of the encoded base64 CSR:

```yaml
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: user-request
spec:
  request: <YOUR-BASE64-ENCODED-CSR-HERE>
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - client auth
```

Replace `<YOUR-BASE64-ENCODED-CSR-HERE>` with your base64 encoded CSR.

Apply this file to your Kubernetes cluster:

```bash
kubectl apply -f user-csr.yaml
```

### Step 3: Approve the CSR

Once the CSR is submitted, you need to manually approve it for Kubernetes to issue the certificate:

```bash
kubectl certificate approve user-request
```

### Step 4: Retrieve the Certificate

After the CSR is approved, you can fetch the issued certificate:

```bash
kubectl get csr user-request -o jsonpath='{.status.certificate}' | base64 --decode > user.crt
```

### Step 5: Use the Certificate

Now that you have the certificate (`user.crt`) and the private key (`user.key`), you can configure your Kubernetes client (`kubectl`) to use these credentials to authenticate as the user.

This process allows you to securely manage identities within your Kubernetes cluster, using the cluster's native authentication mechanisms.

For more details and best practices on managing certificates and CSRs in Kubernetes, consult the official documentation: https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/

This procedure is essential for administrators and users who need to configure secure access to a Kubernetes cluster, being a crucial skill for the CKA exam.
