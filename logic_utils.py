class GuessResult(tuple):
    """Tuple-like result that also compares equal to an outcome string."""

    def __new__(cls, outcome: str, message: str):
        return super().__new__(cls, (outcome, message))

    def __eq__(self, other):
        if isinstance(other, str):
            return self[0] == other
        return super().__eq__(other)


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    candidate = raw.strip()
    if candidate == "":
        return False, None, "Enter a guess."

    try:
        value = int(candidate)
    except ValueError:
        return False, None, "That is not a whole number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return GuessResult("Win", "🎉 Correct!")

    if guess > secret:
        return GuessResult("Too High", "📉 Go LOWER!")
    return GuessResult("Too Low", "📈 Go HIGHER!")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        return current_score + max(points, 10)

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
