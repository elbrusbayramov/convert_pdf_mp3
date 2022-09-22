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
