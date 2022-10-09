
from gtts import gTTS
import os
from PyPDF2 import PdfReader
temp = open('./SHE HACKS II.pdf', 'rb')

PDF_read = PdfReader(temp)
first_page = PDF_read.getPage(0)
text=first_page.extractText()
language = 'en'
myobj = gTTS(text=text, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("mpg321 welcome.mp3")