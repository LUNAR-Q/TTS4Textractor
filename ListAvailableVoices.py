import win32com.client as wincl

# Initialize Windows TTS
speaker = wincl.Dispatch("SAPI.SpVoice")

# List all available voices
voices = speaker.GetVoices()

for i in range(voices.Count):
    print(f"Voice {i}: {voices.Item(i).GetDescription()}")
    print(f"ID {i}: {voices.Item(i).id}")