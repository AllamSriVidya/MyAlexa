import pyttsx3
try:
    tts_engine = pyttsx3.init()
    voices = tts_engine.getProperty('voices')
    for voice in voices:
        print(voice.name)
    print(voices)
    tts_engine.setProperty('voice','com.apple.speech.synthesis.voice.zuzana')
    print(voice)
    tts_engine.say('This is just a test.')
    tts_engine.runAndWait()
    input('Press enter to exit.')
except:
    print('error')