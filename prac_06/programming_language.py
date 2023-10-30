class PL:
    # Constructor
    def __init__(self, Name, Typing, Reflection, Year):
        self.Name = Name  # Name of the programming language.
        self.Year = Year  # Year of first appearance
        self.Reflection = Reflection  # Reflection: True/False
        self.Typing = Typing       # Typing: Static/Dynamic

    # Judgment statement, returns True if the programming language is dynamically typed, otherwise returns False
    def is_dynamic(self):
        return self.Typing == "Dynamic"

    def __str__(self):
        return f"{self.Name}, {self.Typing} Typing, Reflection={self.Reflection}, First appeared in {self.Year}"
