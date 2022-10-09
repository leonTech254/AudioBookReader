
from gtts import gTTS
from assets.leonResources import color,custom_output,user_input
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
    
    
    # display files
    documents=applicationStore.AvailableFiles
    print(documents)
    for num in range(0,len(documents),2):
        print(num)
        if num-2==-2:
            pass
        else:
            currentDoc=documents[num-2]
            nextNum=num-1
            nextDoc=documents[nextNum]
            custom_output.info(f"{num-2}{currentDoc} {nextNum}{nextDoc}",color.red)
        
        
    
listFiles()

    

# temp = open('./SHE HACKS II.pdf', 'rb')
# PDF_read = PdfReader(temp)
# first_page = PDF_read.getPage(0)
# text=first_page.extractText()
# language = 'en'
# myobj = gTTS(text=text, lang=language, slow=False)
# myobj.save("welcome.mp3")
# os.system("mpg321 welcome.mp3")