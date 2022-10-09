
from gtts import gTTS
import os
from PyPDF2 import PdfReader

class applicationStore:
    DocumentName=""
    NarratorSpeed=""
    language='en' #default
    supportedDocuments=['.pdf','.docx']
    AvailableFiles=[]
    
def listFiles():
    path=os.getcwd()
    for (root, dirs, file) in os.walk(path):
        for f in file:
            if os.path.splitext(f)[1] in applicationStore.supportedDocuments:
                applicationStore.AvailableFiles.append(f)
    
listFiles()
    

# temp = open('./SHE HACKS II.pdf', 'rb')
# PDF_read = PdfReader(temp)
# first_page = PDF_read.getPage(0)
# text=first_page.extractText()
# language = 'en'
# myobj = gTTS(text=text, lang=language, slow=False)
# myobj.save("welcome.mp3")
# os.system("mpg321 welcome.mp3")