
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
    selectedBook=""
    
def listFiles():
    path=os.getcwd()
    for (root, dirs, file) in os.walk(path):
        for f in file:
            if os.path.splitext(f)[1] in applicationStore.supportedDocuments:
                applicationStore.AvailableFiles.append(f)
    
    
    # display files
    documents=applicationStore.AvailableFiles
    for num in range(0,len(documents),2):
        if num-2==-2:
            pass
        else:
            currentDoc=documents[num-2]
            nextNum=num-1
            nextDoc=documents[nextNum]
            custom_output.info(f"{num-2} {currentDoc} \t\t {nextNum} {nextDoc}",color.red)

def userChooseFile():
    bookSelected=user_input.useruput("Enter book to conver to audio: ")    
    check=str.isnumeric(bookSelected)
    if bool(check)==False:
        custom_output.error("Invalid choice")
    try:
        selectBook=applicationStore.AvailableFiles[int(bookSelected)]
        custom_output.info(f"Selected book: {color.white}{selectBook}",color.green)
        applicationStore.selectedBook=bookSelected
    except:
        custom_output.error("invalid choose")

def main():
    listFiles()
    userChooseFile()
main()

    

# temp = open('./SHE HACKS II.pdf', 'rb')
# PDF_read = PdfReader(temp)
# first_page = PDF_read.getPage(0)
# text=first_page.extractText()
# language = 'en'
# myobj = gTTS(text=text, lang=language, slow=False)
# myobj.save("welcome.mp3")
# os.system("mpg321 welcome.mp3")