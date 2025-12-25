def evaluate_answer(llm_output, correct_answer, attempt_number):
    # Penalize shortcut reasoning ONLY on first attempt (Forcing error to show working of RL framework)
    if attempt_number == 1:
        if "V = I * R" in llm_output or "F = m * a" in llm_output:
            return -1, "Used correct formula too quickly on first attempt"

    if correct_answer in llm_output:
        return 1, "Correct answer found"

    return -1, "Incorrect answer"
