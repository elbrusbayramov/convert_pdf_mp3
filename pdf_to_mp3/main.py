"""
- Share little experience when I made freelance job
- Sometimes juniors faced with this task on interview
- Our goal write script  which takes as input the absolute path of pdf file
- You can choose the language for output mp3 file (en ru hindu)
- And get ready mp3 file in chosen language
- There a lot of third party libs which can fulfill our requirements
- we choose pdfplumber
- install libs pip install pdfplumber gtts

code
1. import libs
2. create function pdf_to_mp3 which have 2 arguments
3. first lets check whether we have a pdf file in provided path
To reach this we need to import pathlib from Path
4. Then lets read pdf file to a  usual text file. We use PDF of lib....then we need to go thru all pages and save text of these pages
5. Now we need remove new lines , or empty lines in order to avoid pauses in our resulting mp3 file
6. Lets create now mp3 file
"""

from gtts import gTTS
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path="test.pdf", language="en"):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'Original file: {Path(file_path).name}')
        print('Converting in progress...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'{file_name}.mp3 created!\n'

    else:
        return 'File not exists, check the file path!'


def main():
    print("PDF-to-MP3")
    file_path = input("\nEnter a file path: ")
    language = input("Choose language: ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
