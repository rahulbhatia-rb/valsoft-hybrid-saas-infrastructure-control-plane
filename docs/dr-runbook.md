# Disaster Recovery Runbook

1. Confirm customer impact and the affected product/environment.
2. Classify the failure: compute, database, network, DNS, dependency, or site/region.
3. Validate the most recent successful backup and replication state.
4. Compare the incident against the declared RPO and RTO.
5. Execute the product-specific failover or restore procedure.
6. Validate application health, data integrity, DNS/load-balancer routing, and monitoring.
7. Communicate recovery status to Support and Customer Success.
8. Record gaps and convert repeated manual recovery steps into automation.

## Recovery principle

Backups are not a recovery strategy unless restores are tested. Recovery objectives should be explicit, product-specific, and validated through exercises rather than assumed from backup configuration alone.
