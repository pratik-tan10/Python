#Playsound Module
from playsound import playsound

playsound('myfile.wav')

#Using Simple Audio Module
import simpleaudio as sa

filename = 'myfile.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done()  # Wait until sound has finished playing

#USing winsound module works only for wav files
import winsound

filename = 'myfile.wav'
winsound.PlaySound(filename, winsound.SND_FILENAME)

#Beep speakers using winsound
import winsound

winsound.Beep(1000, 100)  # Beep at 1000 Hz for 100 ms

#Using sounddevice module
import sounddevice as sd
import soundfile as sf

filename = 'myfile.wav'
# Extract data and sampling rate from file
data, fs = sf.read(filename, dtype='float32')  
sd.play(data, fs)
status = sd.wait()  # Wait until file is done playing
