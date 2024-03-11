programming_languages = {
    "Python": "by Guido van Rossum",
    "Brainfuck": "by Urban Müller",
    "Swift": "by Chris Lattner",
    "Java": "by James Gosling",
}

for language, developer in programming_languages.items():
    print(f"My favorite programming language is {language} and it was created by {developer}.")
del programming_languages["Java"]

print(programming_languages)
