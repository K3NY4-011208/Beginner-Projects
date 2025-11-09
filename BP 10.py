print("Welcome to the Quiz Game!")
score = 0

questions = {
    "What is the capital of France? ": "paris",
    "What is 5 + 7? ": "12",
    "What color do you get when you mix red and white? ": "pink",
    "Who wrote 'Romeo and Juliet'? ": "shakespeare"
}

for question, answer in questions.items():
    user_answer = input(question).lower()
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"You got {score} out of {len(questions)} correct.")
