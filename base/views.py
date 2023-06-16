from django.shortcuts import render, redirect
#from threading import Thread
import pyttsx3
import PyPDF2
import os
from .models import PDF, Audios
from pathlib import Path

eng = pyttsx3.init()
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[1].id)


def convert(filename):
    path = f"{os.getcwd()}/media/pdfs/{filename}"
    book = open(rf"{path}", 'rb')
    pdfReader = PyPDF2.PdfReader(book)
    pages = len(pdfReader.pages)

    speaker = pyttsx3.init()
    
    aud = ""
    for num in range(0, pages):
        page = pdfReader.pages[num]
        text = page.extract_text()
        print(text)
        aud += text
        
    speaker.save_to_file(aud,f"{os.getcwd()}/media/audios/{filename.split('.')[0]}.mp3")
    
    speaker.runAndWait()
        
        
    return f"{filename.split('.')[0]}.mp3"


def index(request):
    if request.method == "POST":
        file = request.FILES['pdf']
        
        s = PDF.objects.create(
            pdf = file
        )
        s.save();
        
        context={}
    
        pdf = PDF.objects.all()[0]
        
        #audio = Audios.objects.all().values()[0]['audio']
        
        d=convert(f"{file}")
        
        if d:
            context['audio_file'] = f"http://127.0.0.1:8000/media/audios/{d}"

        print(context)
        
        return render(request, "index.html", context)

    
    
    context={}
    
    print(os.listdir(fr'{os.getcwd()}/media/pdfs'))
    
    
    return render(request, "index.html", context)
        
        
        
        