# PDF versions 1.4 through 1.7, PDF/A-1 and PDF/A-2 are acceptable for documents.
import fitz
import traceback
class check:
    def __init__(self,location_pdf):
        self.location_pdf=location_pdf
        self.VERSION=None
        self.details=None
        try:
            pdf=fitz.open(self.location_pdf)
            metadata=pdf.metadata
            self.details=metadata
            self.VERSION=metadata['format']
        finally:
            pdf.close()
if __name__=="__main__":
    a=check(r"/home/excel/Desktop/Project_001/Rquirements/FDA_PDF_Specifications-v4-1-FINAL-9-14-2016_fixed.pdf")
    print (a.VERSION)