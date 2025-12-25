# main.py

import os
from openai import OpenAI
from questions import QUESTIONS
from evaluator import evaluate_answer
from agents import *

# =============================
# CONFIG
# =============================
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def llm_call(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# =============================
# PROJECT 1: FEEDBACK-DRIVEN LOOP
# =============================

def feedback_driven_learning():
    print("\n=== PROJECT 1: FEEDBACK-DRIVEN LLM IMPROVEMENT (RL DEMO) ===\n")

    for q in QUESTIONS:
        print(f"Question: {q['question']}")
        feedback = ""

        for attempt in range(1, 4):

            # FORCE error on first attempt
            force_error = (attempt == 1)

            answer = llm_call(
                solver_prompt(q["question"], force_error=force_error)
                + "\n"
                + feedback
            )

            reward, reason = evaluate_answer(answer, q["answer"], attempt)

            print(f"\nAttempt {attempt}")
            print(answer)
            print("Reward:", reward)
            print("Evaluation:", reason)

            if reward == 1:
                print("Correct — learning converged\n")
                break
            else:
                feedback = f"""
Feedback:
Your previous answer was incorrect.

Error type: {reason}
You must correct the mistake and try again.
"""

# =============================
# PROJECT 2: MULTI-AGENT SYSTEM
# =============================

def multi_agent_reasoning():
    print("\n=== PROJECT 2: MULTI-AGENT PHYSICS REASONING ===\n")

    for q in QUESTIONS:
        print(f"Question: {q['question']}")

        solution = llm_call(solver_prompt(q["question"]))
        concept_feedback = llm_call(concept_checker_prompt(solution))
        math_feedback = llm_call(math_checker_prompt(solution))
        judgment = llm_call(
            judge_prompt(solution, concept_feedback, math_feedback)
        )

        print("\nSolver Output:\n", solution)
        print("\nConcept Checker:\n", concept_feedback)
        print("\nMath Checker:\n", math_feedback)
        print("\nJudge Decision:\n", judgment)
        print("\n" + "-"*60 + "\n")

# =============================
# RUN
# =============================

if __name__ == "__main__":
    feedback_driven_learning()
    multi_agent_reasoning()
