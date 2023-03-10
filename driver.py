import argparse
import locale
import logging
import time

from question_answering import QA_System 
from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient
from aiy.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)
import aiy.voice.tts

# Converts text to speech 
# Turns led to blue while speaking 
def speak_text(text, leds): 
    print('Speaking Text')
    leds.pattern = Pattern.breathe(1500)
    leds.update(Leds.rgb_pattern(Color.BLUE))
    aiy.voice.tts.say(text, speed=100)
    leds.update(Leds.rgb_off())

# Converts speech to text (on button press) 
# Turns led to green while listening 
def get_text(board, leds, client):
    print('Say Something')
    board.button.wait_for_press()
    leds.update(Leds.rgb_on(Color.GREEN))
    text = client.recognize(language_code='en-US')
    leds.update(Leds.rgb_off())
    return text

def main(): 
    assistant = QA_System()
    client = CloudSpeechClient() # Google cloud to speech client 
    with Board() as board, Leds() as leds: 
        speak_text('Hello, press the button and ask me a question about Cal Poly dining.', leds)
        keep_going = True 
        while keep_going: 
            question = get_text(board, leds, client)
            if question is None: 
                print('You said nothing.')
                continue             
            print('You said: "%s"' % question)
            question = question.lower()
            if 'goodbye' in question:
                speak_text('Goodbye, have a nice day.', leds)
                keep_going = False            
            else:             
                answer = assistant.get_answer()
                #answer = 'Hello, this is only a demo answer.'
                speak_text(answer, leds)

if __name__ == '__main__':
    main()