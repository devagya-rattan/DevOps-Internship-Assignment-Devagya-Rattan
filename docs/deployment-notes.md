# Deployment Notes

## Networking
I have used node PM2 process to deploy workers in private subnet and setup the iii engine in a public subnet with public IP, and then connect the workers to this public ip by changing the connection url in code itself.
### Public API Gateway

- Public IP assigned
- Accepts external HTTP requests
- Routes requests internally

### Private Workers

- No public IPs
- Accessible only through VPC networking

---

## Ports Used

| Service | Port |
|---|---|
| API Gateway | 3000 |

---

## Deployment Order

```diff
- NOTE - INSTALL NODE AND PYTHON IN YOUR SPECIFIC VIRTUAL MACHINES AND SSH INTO THEM 
```
```diff

- IMPORTANT
1. To ssh into bastion apigate way first add your key pair in local laptop -  ```ssh-add key.pem``` (MAC/linux)
2. SSH into bastion vm with -   ```ssh -A user@bastion-public-ip``` (MAC/linux)
3. Once you are in bastion server you can noe ssh into you private vm with - ```ssh -i key.pem user@worker-private-ip```
```

### Step 1 — Provision Infrastructure

```bash
terraform init
terraform apply
```

### Step 2 — Deploy Python Worker

```bash
python -m venv .venv
cd quickstart/workers/math-worker
pip install -r requirements.txt
pm2 start "III_URL=ws://43.205.212.249:49134 python math_worker.py" --name "service-name"
```

### Step 3 — Deploy Caller Worker

```bash
cd quickstart/workers/caller-worker
npm install
pm2 start "npm run dev" --name "service-name"
```

---

## External API Validation

```bash
curl -X POST http://<PUBLIC-IP>:3000/math/add-two-numbers \
-H "Content-Type: application/json" \
-d '{
  "a": 100,
  "b": 200
}'
```

---

## Important Notes

- Workers communicate using private IPs only
- No worker instance is directly exposed publicly
- Security groups restrict unnecessary inbound traffic
- Terraform is used for infrastructure reproducibility
