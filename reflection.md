# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  Ans: When I first ran it, the game website looked so AI generated. From the emojis used to the background color, it looked like the website was created with a single prompt. When I ran the game the hints were misleading.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. The new game button does not seem to be working, it should reset the attempts and make the user play again.
  2. The hint given is opposite to what actually is true. 
  3. The number range doesn't change with change in difficulty. 
  4. Also the attempts don't match with the ones given in the setting panel.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used copilot for this project
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The AI suggested me to change the hint message to lower if guessed word is lower than the target and vice versa for high.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  Easy had range from 1-20 and normal had from 1-100 and hard as 1-50, the AI here when I asked to change it, it changed hard from 1-200 but in the settings tab it was given normal should be 1-50 and hard should be 1-100 so I had to undo changes and ask the AI again this time specifying details. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I manually checked the difference between the changed code each time and then selected keep
- Describe at least one test you ran (manual or using pytest) 
  and what it showed you about your code.
  I tested most of my changes directly on the website, one of it is seeing if the attempts counter changed based on the difficulty chosen.
- Did AI help you design or understand any tests? How?
  Hmm no I personally wanted to test the code on my own.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  the secret number kept changing because the logic corelated with the logic of the new game button
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  basically just reloading a webpage to get the latest changes 
- What change did you make that finally gave the game a stable secret number?
  I made it such a way that the secret number should only change when the new game button is pressed.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    Reading the changes that AI makes and then approving it instead of just blindly giving yes to all changes as even AI can make mistakes.
- What is one thing you would do differently next time you work with AI on a coding task?
  I would go through the codebase on my own before asking AI to make any changes
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project really made me believe that context is everything and that you need to be specific on what you ask to the AI for it to perform its job well. 
