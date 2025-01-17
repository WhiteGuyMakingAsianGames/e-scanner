import pytesseract
from PIL import ImageGrab
import pyttsx3
import time

# Configure the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def scan_screen_for_letter(letter='e'):
    # Capture the screen
    screen = ImageGrab.grab()
    # Perform OCR on the screen
    text = pytesseract.image_to_string(screen)
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
