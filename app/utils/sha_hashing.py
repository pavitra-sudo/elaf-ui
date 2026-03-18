import hashlib


def normalize_info(info: dict) -> str:
    """
    Sort keys → ensure same order always
    """
    parts = []

    for key in sorted(info.keys()):
        value = str(info[key]).strip().lower()
        parts.append(f"{key}={value}")

    return "|".join(parts)


def generate_system_id(system_info: dict) -> str:
    normalized = normalize_info(system_info)

    sha = hashlib.sha256()
    sha.update(normalized.encode())

    return sha.hexdigest()