
def is_two(x):
    if x == 2:
        return True
    elif x == '2':
        return True
    else:
        return False

# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise

def is_vowel(char):
    if char.casefold() in 'aeiou'and len(char.casefold()) == 1:
        return True
    else:
        return False

# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise.
# Use your is_vowel function to accomplish this

def is_consonant(char):
    if char.casefold() not in 'aeiou' and len(char.casefold()) == 1:
        return True
    else:
        return False

# Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.

def is_word(x):
    if x[0].casefold() not in 'aeiou':
        return x.capitalize()
    else:
        return x

# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, and return the amount to tip

def calculate_tip(tip_percent, bill_total):
    if float(tip_percent) > 0 and float(tip_percent) <=1:
        return float(tip_percent) * float(bill_total)
    else:
        return('invalid')

# Define a function named apply_discount. It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied

def apply_discount(price, discount):
    return float(price) - (float(price) * float(discount))

# Define a function named handle_commas. 
# It should accept a string that is a number that contains commas in it as input, and return a number as output

def handle_commas(x):
    return float(x.replace(",", ""))

# Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F)

def get_letter_grade(num):
    if float(num) >= 90 and float(num) <= 100:
        return 'A'
    if float(num) >= 80 and float(num) < 90:
        return 'B'
    if float(num) >= 70 and float(num) < 80:
        return 'C'
    if float(num) >= 60 and float(num) < 70:
        return 'D'
    if float(num) >= 0 and float(num) < 50:
        return 'F'

get_letter_grade(98) 

# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed

def remove_vowels(text):
    for i in 'aeiouAEIOU':
        text = text.replace(i,"")
    return text

# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores

def normalize_name(s):
    invalid_char = ['@', '$', '#', '%', '.', ' ', '/', '!', '&', ',']
    for i in invalid_char:
        s = s.replace(i,'_')
    while True:
        if s[0].isdigit():
            s = s[1:]
        else:
            break
    s = s.strip()
    return s.lower()

# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(list_of_nums):
    csum = []
    for x in range(len(list_of_nums)):
        working_sum = sum(list_of_nums[:x + 1])
        csum.append(working_sum)
    return csum
        
cumulative_sum([1, 2, 3])