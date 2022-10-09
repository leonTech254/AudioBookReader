
from gtts import gTTS
from assets.leonResources import color,custom_output,user_input
import os
from PyPDF2 import PdfReader
import time

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
        applicationStore.selectedBook=selectBook
        
            
            
        
    except:
        custom_output.error("invalid choose")

def bookInfo():
     bookSelected=applicationStore.selectedBook
     temp = open("./"+bookSelected, 'rb')
     PDF_read = PdfReader(temp)
     NumOfpages=len(PDF_read.pages)
     first_page = PDF_read.getPage(0)
     text=first_page.extractText()
     firstLine=text.partition("\n")[0]
     fileCreationDate=time.ctime(os.path.getctime("./"+bookSelected))
     filesize=os.stat("./"+bookSelected)
     filesize=filesize.st_size/(1024*1024)
     filesize=round(filesize,3)
     summuryInfo=f'''
No of pages: {color.white}{NumOfpages}{color.green}
Page firstLine: {color.white}{firstLine}{color.green}
fileCreation: {color.white}{fileCreationDate}{color.green}
fileSize:{color.white}{filesize}MB {color.white}
     '''
     custom_output.info(summuryInfo,color.green)
     confirm=user_input.useruput(f"Convert {applicationStore.selectedBook} to audio? (y/yes,n/no)")
     if confirm=="y" or confirm=="yes":
        # applicationStore.selectedBook=selectBook
        pass
     else:
        userChooseFile()
     
     
     
     
    
    
    

def main():
    listFiles()
    userChooseFile()
    bookInfo()    
main()

    

# #
# language = 'en'
# myobj = gTTS(text=text, lang=language, slow=False)
# myobj.save("welcome.mp3")
# os.system("mpg321 welcome.mp3")