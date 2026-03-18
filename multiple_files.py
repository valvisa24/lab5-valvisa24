from utils import flip, count_letters

message = input("Please type your message\n")
encoded = flip(message) + str(count_letters(message, 'a'))

print("Your encoded message is: " + encoded)