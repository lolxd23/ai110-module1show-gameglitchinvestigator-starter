# FIX: Collaborated with Claude to identify and fix bugs in app.py:
# - get_range_for_difficulty returned wrong range for Hard mode (1,50 instead of larger than Normal)
# - check_guess had reversed hints ("Go HIGHER" when guess was too high) and a string-vs-int
#   comparison bug on even attempts caused by secret being cast to str before the call
# - Hardcoded 1,100 ranges in the New Game button and info banner replaced with low/high variables
# Logic is scaffolded here for future refactor into logic_utils.py

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
