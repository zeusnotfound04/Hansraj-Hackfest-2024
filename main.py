from voice_assistant import listen, process_command, greet_user

def main():
    greet_user()  # Greet the user at the start
    print("Starting the voice assistant. Say 'stop' to end.")
    
    while True:
        command = listen()
        if command == "stop":
            print("Stopping the assistant.")
            break
        process_command(command)

if __name__ == "__main__":
    main()
