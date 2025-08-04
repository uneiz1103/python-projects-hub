questions = [
    {
        'question': "What is the capital of india?",
        'answer': 'India'
    },
    {
        'question': "What does CPU stands for ?",
        'answer': "Central Processing Unit"
    },
    {
        'question': "Is Python case-sensitive when dealing with identifiers? (yes/no)",
        'answer': "Yes"
    }

]

score = 0

for q in questions:
    print(q['question'])
    user_ans = input("Your answer: ")

    if user_ans.strip().lower() == q['answer'].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {q['answer']}")


print("\nQuiz Complete!")
print(f"Your final score is: {score}/{len(questions)}")
    