import fitz
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
    a=embedded_files(r"C:\Users\Excel_Software\Documents\GitHub\PDFValidator\Samples\include-attachments.pdf")    
    print(a.EMBEDDED_CHECK)