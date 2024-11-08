import random

def funA(min_val, max_val):
    """
    Generate a random integer.
    """
    return random.randint(min_val, int(max_val))  # Cast max to int for compatibility

def funB():
    return random.choice(['+', '-', '*'])

def funC(num1, num2, op):
    prob = f"{num1} {op} {num2}"
    if op == '+':
        ans = num1 + num2  # Corrected addition operation
    elif op == '-':
        ans = num1 - num2  # Corrected subtraction operation
    else:
        ans = num1 * num2  # Corrected multiplication operation
    return prob, ans

def math_quiz():
    score = 0
    total = 2  # Reduced to 2 for quick testing

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total):
        num1 = funA(1, 10)
        num2 = funA(1, 5)  # Removed decimal to be compatible with randint
        op = funB()

        PROBLEM, ANSWER = funC(num1, num2, op)  # Use num1, num2, op as arguments
        print(f"\nQuestion: {PROBLEM}")
        
        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total}")

if __name__ == "__main__":
    math_quiz()
