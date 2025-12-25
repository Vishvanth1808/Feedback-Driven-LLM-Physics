# Feedback-Driven LLM Physics Reasoning

## Overview
This project explores how Large Language Models (LLMs) can improve their physics problem-solving
through feedback-driven self-correction, inspired by ideas from reinforcement learning.

Instead of training or fine-tuning the model, the system focuses on **correcting behavior**
by evaluating answers, providing feedback, and allowing the model to retry until it reaches
a correct solution.

The project also uses a multi-agent setup to separately verify concepts and calculations,
making the reasoning process more transparent.

---

## Project 1: Feedback-Driven Improvement (RL-style)

In this part of the project, the LLM attempts to solve basic physics problems step by step.
After each attempt, the answer is evaluated and assigned a reward:

- A positive reward is given if the answer is correct.
- A negative reward is given if the answer is incorrect or relies on shortcut reasoning.

If a negative reward is assigned, structured feedback is added to the next attempt.
The model then retries the problem using this feedback.

To make reinforcement-learning-style behavior clearly visible, shortcut reasoning is
intentionally penalized only on the **first attempt**. This forces an exploration step,
after which correct reasoning is rewarded and the process converges.

This demonstrates reinforcement learning concepts at the **behavioral and policy level**,
rather than training model parameters.

---

## Project 2: Multi-Agent Physics Reasoning

The second part of the project extends the system into a multi-agent architecture.

Different agents are responsible for different aspects of reasoning:
- One agent generates the initial solution.
- One agent checks whether the correct physics concepts and formulas were used.
- Another agent verifies the numerical calculations.
- A final judge agent combines this feedback to decide whether the solution is correct.

This separation of roles improves interpretability and helps identify where errors occur
(conceptual versus mathematical).

---

## Project Structure

The project is organized into the following files:

- `main.py` – runs the feedback-driven loop and the multi-agent reasoning system  
- `agents.py` – defines the solver and checker agents  
- `evaluator.py` – assigns rewards and determines correctness  
- `questions.py` – contains physics questions and reference answers  
- `README.md` – project documentation  

---

## Notes
- This project does **not** train or fine-tune an LLM.
- Reinforcement learning is demonstrated through reward-guided self-correction.
- Error induction on the first attempt is intentional to make learning dynamics observable.

---

## Future Work
Possible extensions include:
- Handling more complex physics problems
- Automatically classifying error types
- Logging rewards and convergence behavior
- Applying the framework to other reasoning domains
