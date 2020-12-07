# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 10:16:55 2020

@author: Renu
"""

# Import the required module for text   
# to speech conversion 
import pyttsx3 
import PyPDF2

# Open and reda he pdf file in binary mode
pdf_file = open('Business Value.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)

# Get the number of pages in the PDG files
number_of_pages = read_pdf.getNumPages()

# iterarte thru all the pages and raed them one by one
for i in range(0,1 ):
    page = read_pdf.getPage(i)
    # extract the text of the page from the PDF file
    page_content = page.extractText()
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
    newVoiceRate =150
    engine.setProperty('rate',newVoiceRate)
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    voice = engine.getProperty('voice')

    
    # say method on the engine that passing input text to be spoken 
    engine.say(page_content) 

    # run and wait method, it processes the voice commands.  
    engine.runAndWait() 
