import speech_recognition as sr
import mouse, time

recognizer = sr.Recognizer()
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You said: " + command)
            if "Click" in command:
                for i in range(0, 151):
                    mouse.click("left")
                    time.sleep(0.07)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

while True:
    listen_for_command()
