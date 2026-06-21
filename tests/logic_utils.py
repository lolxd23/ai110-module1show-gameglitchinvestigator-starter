# FIX: Collaborated with Claude to identify and fix bugs in app.py:
# - get_range_for_difficulty returned wrong range for Hard mode (1,50 instead of larger than Normal)
# - check_guess had reversed hints ("Go HIGHER" when guess was too high) and a string-vs-int
#   comparison bug on even attempts caused by secret being cast to str before the call
# - Hardcoded 1,100 ranges in the New Game button and info banner replaced with low/high variables
# Logic is scaffolded here for future refactor into logic_utils.py

def get_range_for_difficulty(difficulty: str):
    """
    Return the (low, high) guessing range for a given difficulty.
 
    Easy: 1-50, Normal: 1-100, Hard: 1-200.
    Falls back to 1-100 for any unrecognized difficulty.
    """
    ranges = {
        "Easy": (1, 50),
        "Normal": (1, 100),
        "Hard": (1, 200),
    }
    return ranges.get(difficulty, (1, 100))
 
 
def parse_guess(raw: str, low: int, high: int):
    """
    Validate and convert raw text input into an integer guess.
 
    Returns a tuple of (is_valid, value, error_message).
    Rejects empty input, non-numeric input, and out-of-range values.
    """
    if raw is None:
        return False, None, "Enter a guess."
 
    if raw == "":
        return False, None, "Enter a guess."
 
    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."
 
    if value < low or value > high:
        return False, None, f"Enter a number between {low} and {high}."
 
    return True, value, None
 
 
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).
 
    outcome examples: "Win", "Too High", "Too Low"
    """
    guess = int(guess)
    secret = int(secret)
 
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"
 
 
def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update the player's score based on the outcome of a guess.
 
    Wins award points that shrink with more attempts (minimum 10).
    Both "Too High" and "Too Low" consistently subtract 5 points.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points
 
    if outcome == "Too High":
        return current_score - 5
 
    if outcome == "Too Low":
        return current_score - 5
 
    return current_score