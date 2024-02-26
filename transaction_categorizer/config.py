import yaml


def load_secrets() -> dict[str, str]:
    with open("secrets.yaml", "r") as file:
        secrets = yaml.safe_load(file)
    return secrets


def parse_categories(config_filepath: str = "categories.yaml"):
    with open(config_filepath, "r") as file:
        categories = yaml.safe_load(file)
    return categories


def format_categories_for_prompt(categories: dict[str, dict]):
    formatted_categories = []
    for category in categories:
        subs = [sub["name"] for sub in category["subcategories"]]
        formatted_categories.append(
            f"""category={category['name']}
            subcategories:{','.join(subs)}
            """
        )
    return "\n".join(formatted_categories)
