import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Criteria checks
    length = len(password)
    has_lower = re.search(r"[a-z]", password) is not None
    has_upper = re.search(r"[A-Z]", password) is not None
    has_digit = re.search(r"\d", password) is not None
    has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Scoring
    if length >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if has_lower:
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if has_upper:
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if has_digit:
        score += 1
    else:
        feedback.append("Include numbers.")

    if has_special:
        score += 1
    else:
        feedback.append("Use special characters (e.g. !, @, #, $).")

    # Determine strength
    strength_levels = {
        5: "Very Strong 💪",
        4: "Strong 👍",
        3: "Moderate 😐",
        2: "Weak ⚠️",
        1: "Very Weak ❗",
        0: "Extremely Weak ❌"
    }

    strength = strength_levels[score]

    return strength, feedback


# Example usage:
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength, tips = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")
    if tips:
        print("Suggestions to improve:")
        for tip in tips:
            print(f" - {tip}")
