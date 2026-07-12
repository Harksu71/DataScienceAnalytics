"""Minimal Python code that imports the vulnerable packages.

This file is intentionally simple. The purpose of the project is to let
Snyk detect vulnerable package versions from requirements.txt.
Do not deploy this application to production.
"""

import django
import urllib3
import yaml


SAMPLE_YAML = """
service: demo
purpose: snyk-sca-registration
"""


def show_versions() -> dict:
    """Return package versions so the imports are actually used."""
    return {
        "django": django.get_version(),
        "urllib3": urllib3.__version__,
        "pyyaml": yaml.__version__,
    }


def parse_sample_yaml() -> dict:
    """Parse static YAML using safe_load.

    PyYAML is intentionally pinned to a vulnerable version in requirements.txt,
    but this demo avoids exploit-style payloads.
    """
    return yaml.safe_load(SAMPLE_YAML)


def create_http_manager() -> urllib3.PoolManager:
    """Create a urllib3 manager without making outbound requests."""
    return urllib3.PoolManager()


if __name__ == "__main__":
    print("Snyk Python vulnerable demo")
    print(show_versions())
    print(parse_sample_yaml())
    print(type(create_http_manager()).__name__)
