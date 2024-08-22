import tkinter as tk
import threading
import speech_recognition as sr
import pyttsx3
import webbrowser
import music as mu
import openn as app
from PIL import Image, ImageTk

# Initialize the Text-to-Speech engine
def Text_2_speech(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 125)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        label.config(text=f"Error in Text-to-Speech: {e}")

# Speech Recognition function
def Speech_Recognizer():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:  # Continuous listening loop
            label.config(text="Listening ...")
            try:
                audio = r.listen(source, phrase_time_limit=2)
                command = r.recognize_google(audio).lower()
                label.config(text=f"You said: {command}")
                return command
            except sr.UnknownValueError:
                label.config(text="Could not understand the audio")
            except sr.RequestError as e:
                label.config(text=f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                label.config(text=f"Error during speech recognition: {e}")

# Main Assistance function
def Assistance():
    Text_2_speech("How can I help you?")
    while True:  # Continuous assistance loop
        command = Speech_Recognizer()
        if command:
            if "play" in command:
                Text_2_speech("Playing")
                mu.songs(command)
            elif "open" in command:
                Text_2_speech("Opening")
                app.apps(command)
            elif "google search" in command:
                query = command.replace("google search", "").strip()
                Text_2_speech(f"Searching Google for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            elif "exit" in command or "destroy" in command:
                Text_2_speech("Exiting")
                root.quit()  # Gracefully exit the application
                break
            else:
                Text_2_speech("Please speak again")
        else:
            Text_2_speech("I didn't catch that. Please speak again.")

# Function to handle the "Start" button click
def start_assistance():
    def run_assistance():
        while True:  # Continuous listening for "panda"
            command = Speech_Recognizer()
            if "panda" in command:
                Assistance()
            elif "exit" in command or "destroy" in command:
                Text_2_speech("Ending App")
                root.quit()  # Gracefully exit the application
                break

    threading.Thread(target=run_assistance, daemon=True).start()

# Set up the GUI
root = tk.Tk()
root.title("Voice Command Application")
root.geometry("1600x600")  # Adjusted for better visual appeal

# Load and set the background image
try:
    bg_image = Image.open("background.jpg")  # Ensure the image file is in the same folder as the script
    bg_image = bg_image.resize((1600, 800), Image.Resampling.LANCZOS)  # Resize to match window dimensions

    bg_photo = ImageTk.PhotoImage(bg_image)
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
except Exception as e:
    print(f"Error loading background image: {e}")

# Create and place widgets
frame = tk.Frame(root, bg="#A9A9A9", bd=2)
frame.place(relwidth=1.0, relheight=0.5, relx=0.03, rely=0.7)

label = tk.Label(frame, text="Welcome Master", font=("Helvetica", 16), bg="#D3D3D3")
label.pack(pady=20)

start_button = tk.Button(frame, text="Start Listening", command=start_assistance, font=("Helvetica", 14), bg="#ADD8E6", fg="black")
start_button.pack(pady=10)

exit_button = tk.Button(frame, text="Exit", command=root.quit, font=("Helvetica", 14), bg="#f44336", fg="white")
exit_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
