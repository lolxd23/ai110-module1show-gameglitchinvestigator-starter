from logic_utils import check_guess, parse_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_parse_guess_rejects_negative_number():
    # Negative numbers are below the valid range and should be rejected
    ok, value, error = parse_guess("-10", 1, 100)
    assert ok is False
    assert error is not None


def test_parse_guess_rejects_non_numeric_string():
    # Letters/words aren't valid guesses
    ok, value, error = parse_guess("banana", 1, 100)
    assert ok is False
    assert "not a number" in error.lower()


def test_parse_guess_rejects_empty_string():
    # Submitting with nothing typed in should be rejected
    ok, value, error = parse_guess("", 1, 100)
    assert ok is False
    assert error is not None


def test_parse_guess_handles_decimal_input():
    # Decimal input should be truncated to an int, not crash
    ok, value, error = parse_guess("42.7", 1, 100)
    assert ok is True
    assert value == 42