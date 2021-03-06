class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):  # constructor
        """Initialise a ProgrammingLanguage"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string to represent a ProgrammingLanguage."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing,
                                                                           self.reflection, self.year)

    def is_dynamic(self):
        """Check if the programming language is dynamically typed or not."""
        return self.typing == "Dynamic"
