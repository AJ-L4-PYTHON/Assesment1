glossary = {
    'input': 'the data that the program receives while it is running.',
    'algorithm': ' set of well-defined logical steps that must be taken to perform a task.',
    'end-line comment': 'appears at the end of a line of code and it typically explains the purpose of that line.',
    'strings': ' a sequence of characters in python that are surrounded by either single quotation marks, or double quotation marks.',
    'list': "an object that contains multiple data items.",
    'comments': 'are notes of explanation within a program that is ignored by Python interpreter. It is intended for a person reading the program’s code.',
    'function': ' is a piece of pre written code that performs an operation.',
    'variables': 'names that represent a value stored in the computer memory',
    'control structure': ' logical design that controls order in which set of statements execute.',
    'for loop': 'used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")