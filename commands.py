import webbrowser
import os

def execute_command(command):
    """Execute a specific command if it matches predefined actions."""
    if "open browser" in command:
        webbrowser.open("http://www.google.com")
        print("Opening browser...")
        return True
    elif "search for" in command:
        query = command.replace("search for", "").strip()
        webbrowser.open(f"http://www.google.com/search?q={query}")
        print(f"Searching for {query}...")
        return True
    elif "open notepad" in command:
        os.system("notepad")
        print("Opening Notepad...")
        return True
    # Add more commands here as needed.
    return False
