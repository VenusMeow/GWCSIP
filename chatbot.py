# --- Define your functions below! ---
#function that introduces chatbot to user
def intro():
    print("Hi! My name is chatbot. I like to chat with people about anything.")

#function that responds to user depending on what they say
def process_input(input):
    if input == "hi":
        print("Good afternoon!")
    else:
        print("That's cool!")

# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        process_input(answer)

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
