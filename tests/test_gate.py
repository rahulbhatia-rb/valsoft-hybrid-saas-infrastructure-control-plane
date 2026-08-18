import json
from pathlib import Path

from src.valsoft_infra.gate import evaluate


def load(name):
    return json.loads((Path(__file__).parents[1] / "examples" / name).read_text())


def test_safe_environment_passes():
    result = evaluate(load("production-saas.json"))
    assert result.allowed
    assert result.findings == []


def test_unsafe_environment_fails():
    result = evaluate(load("unsafe-customer-env.json"))
    assert not result.allowed
    assert len(result.findings) >= 20
