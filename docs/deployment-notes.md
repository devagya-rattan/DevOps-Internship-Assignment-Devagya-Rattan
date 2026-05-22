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

### Step 1 — Provision Infrastructure

```bash
terraform init
terraform apply
```

### Step 2 — Deploy Python Worker

```bash
python -m venv .venv
cd quickstart/workers/python-worker
pip install -r requirements.txt
III_URL=ws://43.205.212.249:49134 python math_worker.py
```

### Step 3 — Deploy Caller Worker

```bash
cd quickstart/workers/caller-worker
npm install
npm run dev
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
