import time
import pyautogui as auto
import schedule
import webbrowser
import sounddevice as sd
import numpy as np
import wavio

link = "meet.google.com/rmn-wbhi-tzs"
meeting_time = "12:51"

sample_rate = 44100  
duration = 60  
output_filename = "meeting_audio.wav"

def join():
    webbrowser.open_new_tab('https://' + link)
    time.sleep(7)
    auto.hotkey('ctrl', 'd')
    auto.hotkey('ctrl', 'e')
    auto.click(1352, 541)

def record_audio():
    audio_data = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()
    wavio.write(output_filename, audio_data, sample_rate, sampwidth=2)


schedule.every().day.at(meeting_time).do(join)
schedule.every().day.at(meeting_time).do(record_audio)


while True:
    schedule.run_pending()
    time.sleep(1)
