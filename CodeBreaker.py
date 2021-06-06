f = open('GFG.html', 'w')
html_template = """<html>
<title>Web Speech API Demo</title>
<p id="info_start">Hey,there!Welcome to our website. We request you to please answer the following questions by clicking on the start button below them on the right side.Your answer appears in the text-box below it.</p>
<div>
	<h1>Q1.Do you suffer from any health diseases ?</h1>
	<h>Options:["Diabetes","Thyroid","Cancer","Others","None"]
</h></br>
<h1>Q2.What’s your annual income?</h1>
	<h>Options:["<2lakh,"2lakh-5lakh","5lakh-10lakh","10lakh>"]</h>
</br>
<h1>Q3.What is your dob?
</h1>
	<h>Options:["All the answers be DD/MM/YYYY format"]
</h></br></html>
"""
f.write(html_template)

f.close()
import speech_recognition as sr

recog = sr.Recognizer()
recog
filename = input("Please provide the file with extension: ")
with sr.Audiofile(filename) as source:
    audiofile = recog.listen(source)
    try:
        text = recog.recognize_google(audiofile)
        print(text)
    except:
        print('check internet connectivity')
with sr.Microphone() as source
    audio = recog.listen(source)
    try:
        text = recog.recognize_google(audio)
        arr = text.split()
        option = ["Cancer", "Thyroid", "Diabetes", "None", "Other"]
        for i in range(0, len(option) - 1):
            c = option[i]
            for j in range(0, len(arr)):
                if (arr[j] == c):
                    print(arr[j])
                else:
                    continue
        import datetime

        inputDate = text
        day, month, year = inputDate.split('/')
        isValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
            datetime.datetime(int(day), int(month), int(year))
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False
        if (isValidDate):
            print("The date of birth is valid ..")
        else:
            print("The date of birth is not valid..")

        val = int(text)
        if (val < 2):
            print("<2 lakh")
        if (val == 3 or val == 4):
            print("2lakh-5lakh")
        if (val == 5 or val == 6 or val == 7 or val == 8 or val == 9):
            print("5lakh-10lakh")
        if (val == 10 or val == 11 or val == 12 or val == 13 or val == 14):
            print("10lakh-15lakh")
        if (val == 15 or val == 16 or val == 17 or val == 18 or val == 19):
            print("15lakh-20lakh")
    except:
       print('Internet connectivity issue')