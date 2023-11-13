import random


def random_int(min: int, max: int) -> int:
    """
    Generate a random integer in the interval from min to max.

    Parameters
    ----------
    min : int
        Minimum value to be included in the random draw.
    max : int
        Upper end of the interval for the random draw.

    Returns
    -------
    int
        The randomly chosen integer value. 

    """
    return random.randint(min, max)


def random_math_operation() -> str:
    """
    Selects a mathematical operation randomly from addition, 
    subtraction and multiplication and returns the symbol as a string.

    Parameters
    ----------
    None

    Returns
    -------
    str
        The string corresponding to the selected mathematical operator 

    """
    return random.choice(['+', '-', '*'])


def generate_problem_and_answer(number_1: int, number_2: int, operation: str) -> (str, int):
    """
    From two integer numbers and a math operator given as a string, a math problem is generated.
    Then, the correct answer is calculated.

    Parameters
    ----------
    number_1: int
        First number to be used for the math problem

    number_2: int
        Second number to be used for the math problem

    operation: str
        Either *, + or - to represent a mathematical operation

    Returns
    -------
    problem: str
        The string writing out the math problem
    
    answer: int
        The correct answer to the math problem 

    """
    # the math problem as a string for printing
    problem = f"{number_1} {operation} {number_2}"

    # building the actual math problem from the components and calculating the answer
    if operation == '+': answer = number_1 + number_2
    elif operation == '-': answer = number_1 - number_2
    else: answer = number_1 * number_2
    return problem, answer

def math_quiz():
    """
    Start a console math quiz where 3 random small math questions are generated 
    and the user has to input the single digit answer into the console. A point for each correct answer is awarded.

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    score = 0 # starting value for the score
    ROUNDS = 3 # number of rounds to play, thus also max possible score

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(ROUNDS):
        # randomly draw the two numbers and operation needed for the math problem
        random_number_1 = random_int(1, 10)
        random_number_2 = random_int(1, 5) 
        operation = random_math_operation()

        problem, answer = generate_problem_and_answer(random_number_1, random_number_2, operation)
        print(f"\nQuestion: {problem}")

        # only integer answers are valid so check for correct type
        # or handle exception otherwise by asking for new input
        while True:
            try:
                useranswer = input("Your answer: ")
                useranswer = int(useranswer)
                break
            except:
                print("Not a valid answer. Please check if your answer is a number.")

        if useranswer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    # show final score out of maximal points to achieve
    print(f"\nGame over! Your score is: {score}/{ROUNDS}")

if __name__ == "__main__":
    # calls the math quiz upon running the script
    math_quiz()
