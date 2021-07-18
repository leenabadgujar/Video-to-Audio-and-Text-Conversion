import speech_recognition as sr 
import moviepy.editor as mp
from gtts import gTTS
import os
import scipy.io.wavfile
import matplotlib.pyplot as plt
clip = mp.VideoFileClip(r"Vlog.mp4")

clip.audio.write_audiofile(r"converted.wav")
r = sr.Recognizer()

audio = sr.AudioFile("converted.wav") #extracting audio from video

with audio as source:
  audio_file = r.record(source)
result = r.recognize_google(audio_file)

with open('recognized.txt',mode ='w') as file: 
   file.write("Recognized Speech:") 
   file.write("\n") 
   file.write(result) 
   print("ready!")

fh = open("recognized.txt","r")
myText = fh.read().replace("\n"," ")
language = "en"
output = gTTS(text = myText, lang = language, slow = False)
output.save("output.mp3")
fh.close()

os.system("start output.mp3") #playing the video

rate,data = scipy.io.wavfile.read("converted.wav")
plt.plot(data)
plt.show() #plotting the audio signal
