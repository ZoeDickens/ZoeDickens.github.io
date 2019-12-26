# Creates the dictionary to store responses.
answers = {}

'''
Below, write code that will pose the survey questions from the student prompt
to a user. Your program should save user input as a dictionary.
'''
survey = [
"What is your name?",
"how old are you?",
"where are you from?",
"what is your date of birth?"
]

keys = ["name", "age", "home", "DOB"]

for x in range(len(survey)):
    response = input(survey[x]+": ")
    answers[keys[x]] = response



list_of_answers = []
done = "NO"

# Print the context of the dictionary.
print(answers)
