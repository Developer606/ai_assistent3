import speech_recognition as sr

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('i am litening...')
        r.adjust_for_ambient_noise = source
        audio = r.listen(source,0,7)

    try:
     query =   r.recognize_google(audio, language="en-in")
     print(f"you:  {query}")
     return query

    except:
        print("not recgning...")




