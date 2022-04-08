#Data Types & Variables Exercises

# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?


little_mermaid = 3 * 3
brother_bear = 5 * 3
hercules = 1 * 3

print(little_mermaid + brother_bear + hercules)

#answer- $27.00

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google_rate = 400
amazon_rate = 380
facebook_rate = 350

(facebook_rate * 10) + (google_rate * 6) + (amazon_rate * 4)

#answer- $7,420 

# A student can be enrolled to a class only if the class is not full and 
# the class schedule does not conflict with her current schedule.

class_not_full = True
no_schedule_conflict = True

student_may_enroll = class_not_full and no_schedule_conflict

print(student_may_enroll)


# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

number_of_items = 5
offer_not_expired = True
premium_member = True

product_offer = (number_of_items and offer_not_expired) or premium_member
print(product_offer)

# Continue working in your data_types_and_variables.py file. Use the following code to follow the instructions below:

# username = 'codeup'
# password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

p_length = (len(password) >= 5)
u_length = (len(username) <= 20)
p_and_u_different = (password != username)
no_whitespace = ((username,password).count(' ') == 0)

