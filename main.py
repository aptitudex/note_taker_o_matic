import whisper
import os
import sounddevice as sd
from datetime import datetime
import rec_unlimited as record

# setup audio characteristics
frequency = 44100

# setup recording user input
class_input = input("Which class is this? \n [1] ECE300 CT  [2] ECE250 Device  [3] MA382 Stats  [4] ENGLH290\n Input: ")
classname = "UNDEFINED"
if(class_input == '1'):
    classname = "ECE300"
elif(class_input == '2'):
    classname = "ECE250"
elif(class_input == '3'):
    classname = "MA382"
elif(class_input == '4'):
    classname = "ENGLH290"

#record
record.make_recording()

model = whisper.load_model("base.en")

files = [filename for filename in os.listdir() if filename.startswith('temp')] 

print(files[0])
result = model.transcribe(files[0], fp16=False)

os.remove(files[0])

notated_text = list()

for item in result["segments"]:
    notated_text.append(f"[{item['start']}] {item['text']}")

current_time = datetime.now().strftime("%Y_%m_%d")

file = open(f"{classname}_{current_time}", 'w')

for item in notated_text:
    file.write(item+"\n")
file.close()