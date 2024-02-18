import yaml


def load_secrets() -> dict[str, str]:
    with open("secrets.yaml", "r") as file:
        secrets = yaml.safe_load(file)
    return secrets
