
from dataclasses import replace
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
    pageContents=""
    lines=""


for i in range(0,70):
    applicationStore.lines+="-"

def listFiles():
    path=os.getcwd()
    for (root, dirs, file) in os.walk(path):
        for f in file:
            if os.path.splitext(f)[1] in applicationStore.supportedDocuments:
                applicationStore.AvailableFiles.append(f)
    
    
    # display files
    documents=applicationStore.AvailableFiles
    custom_output.info("AVAILABLE BOOK ",color.yellow)
    custom_output.info(f"{applicationStore.lines}\n",color.blue)
    for num in range(0,len(documents),2):
        if num-2==-2:
            pass
        else:
            currentDoc=documents[num-2]
            nextNum=num-1
            nextDoc=documents[nextNum]
            custom_output.info(("{:<2} {:<50} {:<2} {:<50}".format(int(num-2),currentDoc, int(nextNum),nextDoc)),color.red)
            
            # custom_output.info(f"{num-2} {currentDoc} \t\t {nextNum} {nextDoc}",color.red)

def userChooseFile():
    bookSelected=user_input.useruput("Enter book to conver to audio: ")    
    check=str.isnumeric(bookSelected)
    if bool(check)==False:
        custom_output.error("Invalid choice")
    try:
        selectBook=applicationStore.AvailableFiles[int(bookSelected)]
        applicationStore.selectedBook=selectBook
    except:
        custom_output.error("invalid choose")

def bookInfo():
     bookSelected=applicationStore.selectedBook
     temp = open("./"+bookSelected, 'rb')
     PDF_read = PdfReader(temp)
     NumOfpages=len(PDF_read.pages)
     first_page = PDF_read.getPage(1)
     text=first_page.extractText()
     firstLine=text.strip("\n")
    #  print(firstLine.replace("\n"," "))
     firstLines=""
     for i in firstLine:
         firstLines+=i 
     firstLine=firstLines.replace('\n' ,' ')         
     fileCreationDate=time.ctime(os.path.getctime("./"+bookSelected))
     filesize=os.stat("./"+bookSelected)
     filesize=filesize.st_size/(1024*1024)
     filesize=round(filesize,3)
     summuryInfo=f'''
\tSelected book: {color.white}{bookSelected}{color.green}
\tNo of pages: {color.white}{NumOfpages}{color.green}
\tPage firstLine: {color.white}{firstLine}{color.green}
\tFileCreation: {color.white}{fileCreationDate}{color.green}
\tFileSize: {color.white}{filesize}MB {color.white}
     '''
     custom_output.info(summuryInfo,color.green)
     custom_output.info(f"{applicationStore.lines}\n",color.blue)
     
     confirm=user_input.useruput(f"Convert {applicationStore.selectedBook} to audio? (y/yes,n/no)")
     if confirm=="y" or confirm=="yes":
        # applicationStore.selectedBook=selectBook
        NumOfpagesToAudio=user_input.useruput(f"Enter number of pages[user * to convert all]")
        if NumOfpages=='*':
            pass
        else:
            if bool(str.isnumeric(NumOfpagesToAudio))==False:
                custom_output.error("Invalid input")
                bookInfo()
            startPage= int(user_input.useruput(f"Enter start page"))
            for i in range(int(startPage),int(NumOfpagesToAudio)+int(startPage)): 
                content = PDF_read.getPage(i)
                text=content.extractText()
                applicationStore.pageContents+=text
     else:
        userChooseFile()

def convertToAudio():
    custom_output.info("converting to Audio......",color.blue)
    myobj = gTTS(text=applicationStore.pageContents, lang=applicationStore.language, slow=False)
    myobj.save(f"./mp3/{applicationStore.selectedBook}.mp3")
    custom_output.info(f"[*] Audio book created successfully check mp3/{applicationStore.selectedBook}.mp3",color.cyan)

def main():
    listFiles()
    userChooseFile()
    bookInfo()  
    convertToAudio()
      
main()

    

# #
# language = 'en'
