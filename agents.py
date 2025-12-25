# agents.py

def solver_prompt(question, force_error=False):
    if force_error:
        return f"""
You are a physics problem solver.

IMPORTANT:
- Answer QUICKLY
- Do NOT double-check formulas
- Use plain text ONLY
- Do NOT use LaTeX, symbols, or math formatting
- Write equations like: F = m * a
- Prefer division over multiplication if unsure

Problem:
{question}

Give a final numerical answer in plain text.
"""
    else:
        return f"""
You are a careful physics problem solver.

IMPORTANT:
- Use plain text ONLY
- Do NOT use LaTeX, \\( \\), \\[, \\], \\boxed, or symbols
- Write equations like: F = m * a
- Write units like: m/s^2, N, V
- Explain in simple English

Problem:
{question}

Solve step by step and give the final correct answer in plain text.
"""


def concept_checker_prompt(solution):
    return f"""
Check whether the correct physical concept and formula were used.

IMPORTANT:
- Use plain text only
- No LaTeX or math symbols

Solution:
{solution}
"""

def math_checker_prompt(solution):
    return f"""
Check only the arithmetic and calculations.

IMPORTANT:
- Use plain text only
- No LaTeX or math symbols

Solution:
{solution}
"""

def judge_prompt(solution, concept_feedback, math_feedback):
    return f"""
You are a judge.

IMPORTANT:
- Use plain text only
- No LaTeX or math symbols

Original Solution:
{solution}

Concept Check:
{concept_feedback}

Math Check:
{math_feedback}

Decide if the solution is correct.
If incorrect, clearly state the main reason.
"""