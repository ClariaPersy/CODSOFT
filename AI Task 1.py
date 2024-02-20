import re

def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Simple pattern matching for user queries
    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hello! How can I help you today?"

    elif re.search(r'\b(how are you|how do you do)\b', user_input):
        return "I'm just a computer program, but I'm doing well. Thank you for asking!"

    elif re.search(r'\b(goodbye|bye|see you)\b', user_input):
        return "Goodbye! Have a great day!"
    elif re.search(r'\b(my name)\b', user_input):
        return "oh that's a cute name^-^"
    elif re.search(r'\b(your name)\b', user_input):
        return "i'm sorry i dont have a name...maybe you can give me one ^3^"
    elif re.search(r'\b(ok)\b', user_input):
        return "sounds good <3"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"

# Main loop for the chatbot
while True:
    # Get user input
    user_input = input("You: ")

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    # Get the chatbot's response based on user input
    response = simple_chatbot(user_input)

    # Print the chatbot's response
    print("Chatbot:", response)