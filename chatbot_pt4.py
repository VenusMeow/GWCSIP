# --- Define your functions below! ---
#introduction
def intro():
    print("Hi! My name is chatbot. I like to chat with people about anything.")

#default reply
def say_default():
    print("What will you say?")

#greeting reply
def say_greetings():
    print("Hi! How are you?")

#checking if the user has entered greeting messages
def is_input_greetings(input,greeting_responses):
    if input in greeting_responses:
        return True
    else:
        return False

#process the user's input based on its contents
def process_input(input):
    greeting_responses = ["hi","hello","hey","what's up","good morning","good day","good afternoon"]
    flag = is_input_greetings(input,greeting_responses)
    if flag == True:
        say_greetings()
    else:
        say_default()

# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        process_input(answer)

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
