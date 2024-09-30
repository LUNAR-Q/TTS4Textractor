import pyttsx3
import keyboard
import pyperclip
import time
import multiprocessing

id_prefix = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\VOICEVOX"  # id prefix for voicevox voices
voice_mapping = {'P': "001", 'N': "000", 'O': None}     # P for protagonist, N for narration, O for others
volume = 1.0    # volume between 0.0 and 1.0
speed = 160     # words per minute
last_clipboard = pyperclip.paste()   # avoid reading previous clipboard content

engine = pyttsx3.init()
engine.setProperty("volume", volume)
engine.setProperty("rate", speed)


def set_voice(tag):
    """
    Set the voice of the TTS engine based on the tag.
    """
    if voice_mapping[tag] is not None:
        engine.setProperty("voice", id_prefix + voice_mapping[tag])
        return voice_mapping[tag]
    return None
    
def speak_sentence(clipboard):
    """
    Speak out the sentence in the clipboard (with tags).
    """
    if set_voice(clipboard[0]):
        engine.say(clipboard[1:])
        print("Speaking:", clipboard)
        engine.runAndWait()


def monitor_clipboard():
    global last_clipboard
    global speakThread
    print("Monitoring clipboard...")
    try:
        while True:
            current_clipboard = pyperclip.paste()
            if current_clipboard != last_clipboard:
                print("Detected clipboard change:", current_clipboard)
                last_clipboard = current_clipboard
                if current_clipboard.startswith(('P', 'N', 'O')):  # Only read valid tagged input
                    stop_playback()    # break the previous playback
                    speakThread = multiprocessing.Process(target=speak_sentence, args=[current_clipboard])
                    speakThread.start()
            time.sleep(0.1)
    except:
        KeyboardInterrupt

def stop_playback():
    try:
        if speakThread.is_alive:
            engine.stop()
            speakThread.kill()
            print("Playback stopped.")
    except:
        pass
        

def replay_sentence():
    speak_sentence(last_clipboard)


def setup_hotkeys():
    keyboard.add_hotkey('ctrl+shift+s', stop_playback)
    keyboard.add_hotkey('ctrl+shift+r', replay_sentence)


if __name__ == '__main__':
    setup_hotkeys()
    clipThread = multiprocessing.Process(target=monitor_clipboard)
    clipThread.start()
    