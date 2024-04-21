# refer to https://www.geeksforgeeks.org/convert-pdf-file-text-to-audio-speech-using-python/
import PyPDF2
import pyttsx3


def main():
    # path of the PDF file
    path = 'the_little_mermaid.pdf'

    # creating a PdfFileReader object
    # pdfReader = PyPDF2.PdfFileReader(path)
    pdfReader = PyPDF2.PdfReader(path)

    # check if PDF has more than one page
    if len(pdfReader.pages) > 1:
        # read only the first page
        # the page with which you want to start
        # from_page = pdfReader.getPage(1)
        from_page = pdfReader.pages[0]

        # extracting the text from the PDF
        # text = from_page.extractText()
        text = from_page.extract_text()

        # reading the text
        speak = pyttsx3.init()
        speak.say(text)
        speak.runAndWait()
    else:
        print("PDF file has only one page.")

if __name__ == "__main__":
    main()
