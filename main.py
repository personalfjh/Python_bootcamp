# Hi all, this is my first code I will post all my beginner projects here. I will do my best to try to comment on all
# my codes, and make it easy to understand to all of you guys who are on the same path. Please if you have any comments
# or doubts please do not hesitate to contact me by discord FrankHH#3110 and my github "https://github.com/personalfjh

# Just run the code

from beginner_code import Beginner
from options_finder import Finder


finder = Finder()
code = Beginner()

valid = True
while valid:
    finder.select_day()
    code.call_function(finder.day, finder.option)
    answer = input('Would you like to try another day and lesson: (yes or no) ').lower()
    if answer == 'no':
        valid = False
    else:
        print("\n" * 15)










