def get_contains_class(*values: str) -> str:
    xpath = ""
    for value in values:
        xpath += f"//*[contains(@class, '{value}')]"
    return xpath
