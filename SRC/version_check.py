# PDF versions 1.4 through 1.7, PDF/A-1 and PDF/A-2 are acceptable for documents.
import fitz
import traceback
import re
from select_file import get_file
class check:
    def __init__(self,location_pdf):
        self.location_pdf=location_pdf
        self.VERSION=None
        self.details=None
        self.VERSION_CHECK=None
        try:
            pdf=fitz.open(self.location_pdf)
            metadata=pdf.metadata
            self.details=metadata
            self.VERSION=metadata['format']
            version=float(re.findall(r"\d?\.\d?",self.VERSION)[0])
            if version<1.4 or version>1.7:
                self.VERSION_CHECK=False
            else:
                self.VERSION_CHECK=True
        finally:
            pdf.close()
if __name__=="__main__":
    pdf=get_file()
    if pdf[0]=="Submit":
        a=check(pdf[1])
        print (a.VERSION_CHECK)