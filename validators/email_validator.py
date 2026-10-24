import re

# Local part: standard RFC-5322-ish subset (letters, digits, and common
# special chars, no leading/trailing or consecutive dots).
_LOCAL_PART = r"[a-zA-Z0-9](?:[a-zA-Z0-9._%+-]*[a-zA-Z0-9])?"

# Each domain label must start and end with an alphanumeric character,
# so it can't start with "." (empty label) or "-" (invalid hostname).
_DOMAIN_LABEL = r"[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?"

_EMAIL_RE = re.compile(
    rf"^{_LOCAL_PART}@{_DOMAIN_LABEL}(?:\.{_DOMAIN_LABEL})+$"
)


def validate_email(email: str) -> bool:
    """Return True if `email` is a well-formed email address.

    Rejects malformed domains such as:
      - usuario@.com           (domain starts with a dot)
      - usuario@dominio..com   (consecutive dots)
      - usuario@-dominio.com   (domain label starts with a hyphen)
      - usuario@dominio-.com   (domain label ends with a hyphen)
    """
    if not isinstance(email, str):
        return False
    return bool(_EMAIL_RE.match(email))
