from dataclasses import dataclass


@dataclass
class Result:
    allowed: bool
    findings: list[str]


def evaluate(spec: dict) -> Result:
    cloud = spec.get("cloud", {})
    network = spec.get("network", {})
    security = spec.get("security", {})
    dr = spec.get("dr", {})
    operations = spec.get("operations", {})

    checks = [
        (spec.get("owner"), "environment owner is required"),
        (cloud.get("iac") is True, "infrastructure must be managed as code"),
        (cloud.get("cicd") is True, "CI/CD automation is required"),
        (cloud.get("rollback") is True, "rollback capability is required"),
        (security.get("least_privilege") is True, "least privilege is required"),
        (security.get("managed_secrets") is True, "managed secrets are required"),
        (security.get("vulnerability_management") is True, "vulnerability management is required"),
        (security.get("public_database") is False, "production database cannot be public"),
        (security.get("public_admin") is False, "administrative interfaces cannot be public"),
        (network.get("firewall_owner"), "firewall ownership is required"),
        (network.get("dns_owner"), "DNS ownership is required"),
        (network.get("load_balancer_owner"), "load balancer ownership is required"),
        (network.get("connectivity_documented") is True, "VPN/private connectivity must be documented"),
        (dr.get("backups") is True, "backups are required"),
        (dr.get("restore_tested") is True, "backup restore must be tested"),
        (dr.get("rpo_minutes", 99999) <= 240, "RPO must be 4 hours or less"),
        (dr.get("rto_minutes", 99999) <= 480, "RTO must be 8 hours or less"),
        (operations.get("monitoring") is True, "monitoring is required"),
        (operations.get("alert_owner"), "alert ownership is required"),
        (operations.get("runbook"), "runbook is required"),
        (operations.get("oncall_owner"), "on-call owner is required"),
        (operations.get("patching_owner"), "Linux/Windows patching ownership is required"),
        (operations.get("cost_owner"), "cost ownership is required"),
        (operations.get("documentation") is True, "technical documentation is required"),
    ]

    findings = [message for ok, message in checks if not ok]
    return Result(allowed=not findings, findings=findings)
