# DevOps Internship Assignment — Devagya Rattan

## Overview

This project deploys the iii quickstart distributed worker system on AWS using private networking.

The deployment consists of:
- Public bastion API Gateway VM
- Private TypeScript Caller Worker VM
- Private Python Inference Worker VM

Documentation

Detailed deployment notes, troubleshooting steps, and engineering reasoning are documented separately.

### Documentation Links

- [Deployment Notes](https://github.com/devagya-rattan/DevOps-Internship-Assignment-Devagya-Rattan/blob/main/docs/deployment-notes.md)
- [Design Decisions]([./docs/deployment-notes.md](https://github.com/devagya-rattan/DevOps-Internship-Assignment-Devagya-Rattan/blob/main/docs/design-decisions.md))

## Architecture

<img width="1401" height="688" alt="image" src="https://github.com/user-attachments/assets/4364d2bc-ccc3-4529-967a-bd4d6f156773" />


## Infrastructure
VPC

<img width="958" height="713" alt="Screenshot from 2026-05-22 12-49-20" src="https://github.com/user-attachments/assets/22f25591-33df-4435-a1a5-065c2cc64dd2" />
<img width="1590" height="730" alt="Screenshot from 2026-05-22 12-49-02" src="https://github.com/user-attachments/assets/45077b65-ddcb-4708-b56d-44584ef6905e" />

EC2
<img width="1559" height="263" alt="Screenshot from 2026-05-21 01-10-26" src="https://github.com/user-attachments/assets/262d319c-3c52-4162-8a7c-2d41722b10db" />

Worker deployment in ec2 private subnet(logs)
<img width="1538" height="385" alt="Screenshot from 2026-05-21 18-43-29" src="https://github.com/user-attachments/assets/d2b0ff5e-30d7-43ae-8912-8a66e9324f51" />
<img width="1671" height="270" alt="Screenshot from 2026-05-21 19-00-56" src="https://github.com/user-attachments/assets/606e6abd-d32b-4002-b121-58fa8ee495d9" />
### Terraform apply output
@@For terraform to apply you mus connect to your aws account via aws cli@@

<img width="1337" height="538" alt="image" src="https://github.com/user-attachments/assets/bdaf9508-4fc2-490a-a2db-7bb7cc41e0bf" />

### Curl request 
```
curl -X POST http://43.205.212.249:3000/math/add-two-numbers \
  -H "Content-Type: application/json" \
  -d '{
    "a": 100,
    "b": 200
  }'
```
Curl output
```
{
  "c": 300,
  "running_total": 335
}
```

### Components Used
- VPC
- Public Subnet
- Private Subnet
- Internet Gateway
- Route Tables
- Security Groups
- 3 EC2 Instances

### Security Design
- Only API Gateway VM has a public IP
- Worker VMs are inside private subnet
