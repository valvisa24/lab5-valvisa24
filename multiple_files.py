from utils import flip, count_letters

message = input("Please type your message\n")
flipped_message = flip(message)
count_a = count_letters(message, 'a')
encoded_message = flipped_message + str(count_a)

print("Your encoded message is:", encoded_message)