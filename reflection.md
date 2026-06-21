# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When I ran the game the first time, there was difficulty setting option where you can pick which level you want too. It was a simple game that wasnt hard to follow. I didnt find it engaging 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  They were 2 bugs that I notice in this game was the range and the guessing. The range is 1-100, but it includes negative numbers which doesnt make sense. When I was off with my number, it would say go higher but it doesnt make sense why itll go higher (ex 101, go higher).

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess | Go higher! |       | Go Lower!      | none.                  |
  of 0 |
| Guess of | Go higher! Invalid input | | Go lower!     | none                    |
-1 |
| Guess of of 101| Go lower! |   Go Higher!   | none

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used claude for this game glitch. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I was getting weird "go higher/go lower" messages that didn't make sense, like guessing 200 would tell me to go higher even though the secret was way lower than that. Claude pointed out that the code was secretly converting the secret number into a string every other attempt, so when it tried comparing my guess to it, Python threw an error. The fix-up code in the except block then turned my guess into a string too, so it ended up comparing "200" and "42" like text instead of numbers, which is why it broke. Claude told me to just cast both numbers to int before comparing and skip the string stuff entirely. I checked this myself by walking through the example by hand (200 vs 42, string comparison vs number comparison) and yeah, that's exactly what was happening. After applying the fix the hints came back correct every time, no matter which attempt number I was on.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
At one point Claude told me there were two more bugs: that Hard mode was actually returning a smaller number range (1-50) than Normal (1-100), which would make Hard easier instead of harder, and that the "too high/too low" messages were swapped so guessing too high would say "go higher" by mistake. Neither of these turned out to be true when I actually went and looked at the code. Hard mode was never set to 1-50 in any version I had — it was either 1-100 (before fixing) or 1-200 (after), so if anything it was already correctly the hardest. And the messages were never swapped either, too high always said go lower and too low always said go higher in every version. So I just double checked the actual lines myself and realized Claude basically made that one up, and I didn't apply any changes for it since there was nothing to fix.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Mostly I just picked specific numbers and walked through what the code would actually do with them, step by step, instead of trusting that the fix "looked right." For the check_guess bug I literally traced through guess=200, secret=42 by hand both before and after the fix to see if the comparison gave the right hint. If the logic checked out with real numbers and matched what should actually happen in the game, I counted it as fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran a manual test using guess = 200 and secret = 42 on what would be an "even" attempt number. Before the fix, the code converted secret into the string "42," guess stayed as the int 200, and the comparison broke into the except block where it compared "200" > "42" as strings — which came out False since string comparison just looks at the first character, so it told me to go higher even though 200 was already way too high. After applying the fix where both numbers get cast to int before comparing, the same test case correctly returned "Too High / Go Lower," which is what should actually happen. That one test basically proved the whole bug and the fix in one go.
- Did AI help you design or understand any tests? How?
Yeah, same way. Claude basically walked me through that 200 vs 42 example step by step, showing exactly where the comparison would break and why the string version gave the wrong answer. I didn't come up with that test case totally on my own — Claude suggested it as a way to actually see the bug happen instead of just reading the code and assuming. It also helped me understand that the issue wasn't really about the messages being wrong, it was about the comparison itself happening between two different types, which I probably wouldn't have caught just from reading the code casually

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
