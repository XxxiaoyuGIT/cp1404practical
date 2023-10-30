from programming_language import PL

# Create three ProgrammingLanguage objects
python = PL("Python", "Dynamic", True, 1991)
ruby = PL("Ruby", "Dynamic", True, 1995)
visual_basic = PL("Visual Basic", "Static", False, 1991)

# Print the Python object
print(python)

# Create a list containing these three objects
languages = [python, ruby, visual_basic]

# Print descriptions of all programming languages
for language in languages:
    print(language)
