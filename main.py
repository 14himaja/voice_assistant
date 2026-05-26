import webbrowser
import datetime as datetime 
import speech_recognition as sr
import os 
import pyttsx3 
import pywhatkit
from datetime import datetime, date
import wikipedia 
import pyjokes
import random
from pynput import keyboard
from pynput.keyboard import Controller,Key
import pyautogui
import cv2
import subprocess
import pywhatkit as kit
import ctypes
from AppOpener import run

class Assistant:
   
    def speak(self, text):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()
        engine.stop()

    def wish(self):
        hour = int(datetime.now().hour)

        if hour >= 0 and hour < 12:
            self.speak("Good Morning!")
        elif hour >= 12 and hour < 18:
            self.speak("Good Afternoon!")
        else:
            self.speak("Good Evening!")

    def input_command(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎤 Speak something...")
            audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower().strip()
            print("📝 You said:", command)
            return command
        except sr.UnknownValueError:
            print("😕 Sorry, I could not understand the audio.")
            self.speak("I could not understand, please say that again.")
            return None
        except sr.RequestError:
            print("🚫 Could not request results from Google Speech Recognition service.")
            self.speak("Network error, please check your internet connection.")
            return None

    def play_song(self,command):   
        song=command.replace("play","")
        if song:
            self.speak(f"playing {song} on youtube")
            kit.playonyt(song)
        else:
            self.speak("please say what to play")
                     
    def time(self):
        time_text = datetime.now().strftime("%I:%M:%S %p")
        self.speak(f"The time is {time_text}")
        print(time_text)
    
    def date(self):
        date_text = datetime.now().strftime("%d %B %Y")
        self.speak(f"Today is {date_text}")
        print(date_text)

    def search_google(self,command):
        query=command.replace("search","")
        if query:
            self.speak(f"searching google for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            self.speak("what should i seach for")

    def copy_text(self):
            kb=Controller()
            kb.press(Key.ctrl)
            kb.press('c')
            kb.release('c')
            kb.release(Key.ctrl)
            self.speak("copied")

    def paste_text(self):
            kb=Controller()
            kb.press(Key.ctrl)
            kb.press('v')
            kb.release('v')
            kb.release(Key.ctrl)
            self.speak("pasted")

    def tell_joke(self):
        joke=pyjokes.get_joke()
        print(joke)
        self.speak(joke)
    
    def open_application(self,app_name):
        app=app_name.replace("open","")
        if "notepad" in app_name:
            os.system("start notepad")
            self.speak("opening notepad")
        elif "calculator" in app_name:
            os.system("start calc")
            self.speak("opening calculator")
        elif "chrome" in app_name:
            os.system("start chrome")
            self.speak("opening chrome")    
        elif "word" in app_name:
            os.system("start word")
            self.speak("opening word") 
        elif "excel" in app_name:
            os.system("start excel")
            self.speak("opening excel")  
           
        else:
            self.speak(f"sorry,I dont know how to open{app_name}")

    def search_wikipedia(self,command):
        try:
            person = command.replace("who is", "")
            info = wikipedia.summary(person, 2)
            self.speak(info)
        except wikipedia.exceptions.DisambiguationError:
            self.speak("Multiple results found. Please be more specific.")
        except Exception:
            self.speak("I couldn't find anything on Wikipedia.")

    def location(self, place):
        try:
    
            url = f"https://google.nl/maps/place/{place}/"
            webbrowser.open(url)
            self.speak("This is what I found")
            self.speak("Hope I found the correct one")

            pyautogui.click(270, 132, clicks=1, duration=1, button='left')  # Click directions
            self.speak("Locating from your home address")
            pyautogui.click(54, 504, clicks=1, duration=1, button='left')   # Choose home location
            self.speak("Let's start")
            pyautogui.click(122, 341, clicks=1, duration=1, button='left')  # Start navigation

        except Exception as e:
            self.speak("Please check your Internet")
            print("Error:", e)


        
         
    def run_assistant(self):
        self.wish()
        self.speak("Hello, I am your voice assistant. How can I help you today?")
        
        while True:
            command1 = self.input_command()
            if command1 is not None:
                command1=command1.lower()

                if "hello" in command1 or "hi" in command1:
                    self.speak("Hello, how can I assist you?")

                elif "time" in command1:
                    self.time()

                elif "date" in command1:
                    self.date()
                
                elif "joke" in command1:
                    self.tell_joke()
                
                elif "open" in command1:
                    self.open_application(command1)

                elif "search" in command1:
                    self.search_google(command1)

                elif "locate" in command1:
                    location_name = command1.replace("locate", "").strip()
                    self.location(location_name)
                    

                elif "copy" in command1:
                    self.copy_text()

                elif "paste" in command1:
                    self.paste_text()

                elif "play" in command1:
                    self.play_song(command1)

                elif "wikipedia" in command1 or "who is" in command1:
                    self.search_wikipedia(command1)

                elif any(word in command1 for word in ["stop","exit","bye","quit"]):
                    self.speak("GoodBye!")
                    break

                elif 'doing' in command1:
                    self.speak('Spending time with you')

                elif 'about me' in command1:
                    self.speak('Are you kidding...  You are super cool..')

                else:
                    self.speak("sorry,I dont know that command")
            else:
                self.speak("Speak Something")


if __name__ == "__main__":

    obj = Assistant()
    obj.run_assistant()