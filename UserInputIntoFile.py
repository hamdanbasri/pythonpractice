def save_input_to_file(user_input, file_name):
    with open(file_name, 'w') as file:
        file.write(user_input)

# Example user input
#user_input = "This is an example of user input that will be saved into a .txt file."
user_input = input("Tell me your name: ")

# Save the input into 'user_input.txt'
save_input_to_file(user_input, 'user_input.txt')

print("User input has been saved to 'user_input.txt'.")
