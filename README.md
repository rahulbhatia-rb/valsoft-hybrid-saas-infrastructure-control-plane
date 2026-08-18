# Valsoft Hybrid SaaS Infrastructure Control Plane

Role-specific proof-of-work for Valsoft / TAG Software Group's Senior Infrastructure Engineer opening.

The project models a production-readiness contract for customer-facing SaaS products spanning cloud and on-prem environments. It focuses on reliability, security, networking, DR, automation, CI/CD, documentation, and cost ownership.

## Core idea

**Standardize the non-negotiables across many products without forcing every product into the same architecture.**

```text
Product / customer environment
        |
        v
Infrastructure contract
        |
        v
Production readiness gate
   /       |        \
cloud   network    security
  |        |          |
IaC     VPN/DNS     IAM/vuln
  \        |         /
     reliability
         |
   DR / backup / SLO
         |
     allow / deny
```

## What the gate checks

- infrastructure is managed as code
- CI/CD and rollback capability exist
- backups are configured and restore-tested
- RPO/RTO are explicit
- monitoring and alert ownership exist
- no public databases or administrative surfaces
- least privilege and managed secrets
- vulnerability management is active
- firewall and network ownership are explicit
- DNS and load-balancer ownership exist
- VPN/private connectivity is documented where required
- Linux/Windows patching ownership
- cost ownership and technical documentation

## Why this maps to Valsoft / TAG

Valsoft operates a portfolio of long-lived vertical software businesses. The infrastructure challenge is therefore not one greenfield stack: it is creating reliable, secure, supportable standards across different products, customer environments, legacy constraints, and cloud/on-prem topologies.

The gate focuses on a **minimum production contract** rather than prescribing one cloud, one OS, or one deployment platform.

## Repository layout

```text
.
├── README.md
├── pyproject.toml
├── src/valsoft_infra/gate.py
├── examples/
│   ├── production-saas.json
│   └── unsafe-customer-env.json
├── tests/test_gate.py
└── docs/
    ├── architecture.md
    └── dr-runbook.md
```

## Run locally

```bash
python -m pytest -q
```

## 30 / 60 / 90 direction

**0-30 days**
- inventory cloud/on-prem environments and ownership
- map critical customer dependencies and failure modes
- baseline backup/restore, monitoring, IAM, network, and patching posture
- identify repetitive operational toil

**31-60 days**
- standardize Terraform/IaC modules and environment contracts
- improve CI/CD and rollback paths
- establish tested DR runbooks
- centralize infrastructure documentation and ownership

**61-90 days**
- automate compliance/readiness checks
- improve cost and capacity reporting
- reduce manual changes
- create reusable standards across portfolio products without blocking product teams

## Design tradeoff

A portfolio platform should standardize outcomes, not force every acquired product into one implementation. A Windows VM estate, an AWS Kubernetes platform, and an Azure SaaS application can all satisfy the same production contract differently.

## Disclaimer

Independent proof-of-work based only on the public job description. It does not represent Valsoft or TAG Software Group's internal architecture.
