# Design Decisions

## Architecture Choice

The deployment was designed using a public API Gateway/Bastion VM and private worker instances inside a VPC subnet.

The architecture flow is:

Internet → API Gateway VM → Caller Worker VM → Python Worker VM

This design was chosen to isolate inference workers from direct public access while still allowing external API requests.

---

## Why a Public API Gateway Was Used

The API Gateway VM acts as:
- the public HTTP endpoint
- the SSH bastion host
- the internal request router

Only this VM has a public IP address.

This minimizes the public attack surface while simplifying administration of private worker nodes.

---

## Why Workers Were Deployed in a Private Subnet

The worker instances were intentionally deployed inside a private subnet.

Benefits:
- workers cannot be directly accessed from the internet
- inference services remain internal
- RPC communication occurs over private IP addresses
- better network isolation

The workers communicate internally using VPC networking.

---

## RPC Communication Design

RPC communication occurs between:
- API Gateway → Caller Worker
- Caller Worker → Python Worker

Private IP addresses were used instead of public IPs to ensure:
- lower exposure
- internal-only communication
- reduced attack surface

Example internal communication:
- 10.0.1.10
- 10.0.1.20

---

## Why Terraform Was Used

Terraform was used to provision:
- VPC
- subnets
- EC2 instances
- route tables
- security groups

Using Infrastructure as Code improves:
- reproducibility
- automation
- consistency
- deployment speed

The infrastructure can be recreated from scratch using terraform apply.

---

## Security Considerations

Several security decisions were made during deployment:

- Only API Gateway VM has a public IP
- Worker VMs are private
- Security groups restrict unnecessary inbound traffic
- Internal worker communication uses private networking
- SSH access is routed through the bastion/API VM

---

## Tradeoffs

Using a combined Bastion + API Gateway VM simplified deployment and reduced infrastructure complexity.

However, in a production deployment I would separate:
- SSH bastion host
- API load balancer
- application gateway

This would improve isolation and scalability.

---

## Production Improvements

Before production deployment, I would additionally implement:

- HTTPS/TLS termination
- Reverse proxy using Nginx
- Docker containerization
- Kubernetes orchestration
- CI/CD pipeline
- Centralized logging
- Monitoring using Prometheus/Grafana
- Auto scaling groups
- Secret management

---

## Scaling for Larger Models

If the model size increased significantly, I would:

- move inference workloads to GPU instances
- separate inference services from API routing
- introduce request queues
- implement batching
- deploy Kubernetes clusters
- add autoscaling
- use distributed inference systems

---

## Lessons Learned

This project improved my understanding of:
- VPC networking
- private subnet communication
- RPC-based worker systems
- Terraform provisioning
- security group configuration
- deployment troubleshooting