# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It first loaded the initial components. It took a while to load the guessing box. The UI was clean and straightforward.

- List at least two concrete bugs you noticed at the start  

Bug 1: Wrong Hint
- When I put the number 3 as my guess, the hint said to go lower. I kept going lower and reached 1 (the lower bound guess), it still said to go lower. I expected 1 to be the answer logically. The answer was actually 43. The hint was wrong.

Bug 2: Unable to start new game
- After I lost the first round, I tried to hit the new game button to play the game again. I expected this button to work since the text says "Game over. Start a new game to try again." But unfortunately, the button did not work. It says stuck in the game over phase and the game is not restarted.

Bug 3: Bound checking broken
- I entered numbers above 100 and below one, and they were still taken in as valid input. The hints still said go lower/go higher. I expected the app the tell me I made an input error. Additional input validation needs to be added.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  
  I mainly used copilot as suggested by the assignment directions.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  
  One suggestion that was correct was how to fix the new game error. The AI told me how the player status was not being reset. This was actually the right reason behind the bug so it was useful. I verified by using a test case.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  
  I did not encounter any incorrect feedback from the AI. One thing was that the AI failed to suggest other fixes to me. It failed to tell me how to optimize my code by refactoring some app.py code into logic_utils.py. I had to tell it using my own knowledge and assignment directions.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  
  I decided this by first running the pytests and then checking manually on my browser and running the streamlit app.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  
  One manual test I ran was to enter wrong inputs on purpose (-300, +500, etc.). I tested that the input bound was working correctly. The app caught my error, so it meant the code was successful. I also kept guessing and saw that the hints were working correctly. I also tested the new game button by clicking on it. It reset all the fields and I could play again without refreshing.

- Did AI help you design or understand any tests? How?

  
  AI copilot helped to generate the pytests for this project. I asked it to make a seperate test for each bug. It was able to design and pass them successfully. I did the manual testing on my own. The manual testing confirmed that the AI tests were correct.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  
  Streamlit reruns mean the app code is re‑executed top‑to‑bottom every time the user interacts with the UI, so without something to “remember” values, everything would reset on each interaction. This is where session state comes in. st.session_state lets you keep track of variables like the secret number, attempt count, and game status across those reruns so the app behaves like a continuous game instead of restarting from scratch every time. I would explain this to a friend by running an app like this one.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

  
  I think the refactoring in the agent mode was helpful. The automatic commit generation feature was also nice. I also liked the pytests. I will reuse these.

- What is one thing you would do differently next time you work with AI on a coding task?
  
  I would share my own inights on the bugs, but I will also ask the AI for suggestions on how I can optimize the code. I won't accpet all the changes blindly though. I will make sure that they make sense.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  
  I realized that AI generates code much better when you give it your own insights and step by step instructions. Commands like "fix this" generates wrong results sometimes. The specific prompts from this assignment caused the AI to be more helpful.
