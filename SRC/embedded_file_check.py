import fitz
from select_file import get_file
class embedded_files:
    def __init__(self,location_of_pdf):
        self.location_of_pdf=location_of_pdf
        self.EMBEDDED_FILES=None
        self.EMBEDDED_CHECK=None
        try:
            pdf=fitz.open(self.location_of_pdf)
            self.EMBEDDED_FILES=pdf.embeddedFileCount
            if self.EMBEDDED_FILES<0:
                self.EMBEDDED_CHECK=False
            else:
                self.EMBEDDED_CHECK=True
        finally:
            pdf.close()
if __name__=="__main__":
    pdf=get_file()
    if pdf[0]=="Submit":
        print(embedded_files(pdf[1]).EMBEDDED_FILES)
