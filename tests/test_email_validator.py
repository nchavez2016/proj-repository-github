from validators.email_validator import validate_email


def test_valid_emails_are_accepted():
    assert validate_email("usuario@dominio.com")
    assert validate_email("usuario.nombre@sub.dominio.com")
    assert validate_email("user+tag@example.co")


def test_domain_starting_with_dot_is_rejected():
    assert not validate_email("usuario@.com")


def test_domain_with_consecutive_dots_is_rejected():
    assert not validate_email("usuario@dominio..com")


def test_domain_label_starting_with_hyphen_is_rejected():
    assert not validate_email("usuario@-dominio.com")


def test_domain_label_ending_with_hyphen_is_rejected():
    assert not validate_email("usuario@dominio-.com")


def test_missing_at_symbol_is_rejected():
    assert not validate_email("usuariodominio.com")


def test_non_string_input_is_rejected():
    assert not validate_email(None)
    assert not validate_email(12345)
