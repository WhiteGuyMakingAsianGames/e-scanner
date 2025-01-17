import pyautogui
import pyttsx3
import time

def scan_screen_for_letter(letter='e'):
    # Capture the screen
    screen = pyautogui.screenshot()
    # Convert the image to text (without OCR)
    text = screen.to_text()
    # Check if the letter is in the captured text
    return letter in text

def text_to_speech(message):
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)  # Set volume to maximum
    engine.say(message)
    engine.runAndWait()

def main():
    while True:
        if scan_screen_for_letter('e'):
            text_to_speech('e')
        time.sleep(1)  # Sleep for a second before scanning again

if __name__ == "__main__":
    main()
