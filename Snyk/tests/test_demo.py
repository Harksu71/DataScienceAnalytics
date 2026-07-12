from demo_app.main import parse_sample_yaml, show_versions


def test_versions_present():
    versions = show_versions()
    assert "django" in versions
    assert "urllib3" in versions
    assert "pyyaml" in versions


def test_parse_sample_yaml():
    data = parse_sample_yaml()
    assert data["service"] == "demo"
