# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

**Purpose:** The app is a simple number-guessing game built in Streamlit. The player picks a difficulty, the app generates a secret number, and the player guesses repeatedly until they win, run out of attempts, or hit "New Game" to restart.

**Bugs found:**
1. `get_range_for_difficulty()` ignored the difficulty entirely and always returned a 1–100 range, so Easy/Normal/Hard all played identically.
2. `check_guess()` was being fed the secret as a *string* on every other attempt due to a stray `str()` conversion at the call site. This caused a `TypeError`, which the code caught by converting the guess to a string too — meaning the comparison happened as text instead of numbers (e.g. `"200" > "42"` evaluates `False`), so guesses like 200 got told "go higher" when they were already way too high.
3. `update_score()` had inconsistent scoring on "Too High" outcomes — on even-numbered attempts it added 5 points instead of subtracting, while "Too Low" always subtracted.
4. `parse_guess()` had no bounds checking, so out-of-range guesses (like 200 in a 1–100 game) were silently accepted instead of being rejected.

**Fixes applied:**
1. Made `get_range_for_difficulty()` actually branch on difficulty (Easy: 1–50, Normal: 1–100, Hard: 1–200), and updated the "New Game" button and info banner to use the dynamic range instead of hardcoded `1, 100`.
2. Removed the `str()` conversion entirely and rewrote `check_guess()` to cast both `guess` and `secret` to `int` before comparing — no more `try/except` needed.
3. Fixed `update_score()` so "Too High" always subtracts 5 points, consistent with "Too Low".
4. Added a range check in `parse_guess()` that rejects guesses outside `low`–`high` with a clear error message.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Run `streamlit run app.py` and select a difficulty (Easy, Normal, or Hard) from the sidebar — note the range now actually changes (e.g. Hard shows "Range: 1 to 200").
2. Open "Developer Debug Info" to see the secret number for this round.
3. Enter a guess in the text box and click "Submit Guess 🚀" — the hint correctly tells you to go higher or lower based on the *real* numeric comparison, even on attempts where the old bug used to trigger.
4. Try an out-of-range guess (e.g. 200 on a 1–100 game) — the app now rejects it with an error instead of silently accepting it and giving a backwards hint.
5. Keep guessing toward the secret number using the hints; each wrong guess correctly deducts points regardless of attempt number.
6. Guess the secret number exactly — the app shows the balloons animation, declares the win, and displays your final score.
7. Click "New Game 🔁" — a new secret number is generated within the correct range for your selected difficulty, not always 1–100.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->


## 🧪 Test Results

```

(base) hajramuzammal@Hajras-MacBook-Air ai110-module1show-gameglitchinvestigator-starter % pytest
============================================= test session starts =============================================
platform darwin -- Python 3.12.4, pytest-7.4.4, pluggy-1.0.0
rootdir: /Users/hajramuzammal/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.2.0
collected 3 items                                                                                             

tests/test_game_logic.py ...                                                                            [100%]

============================================== 3 passed in 0.01s ==============================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
