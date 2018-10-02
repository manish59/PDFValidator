import fitz
from select_file import get_file
class get_fonts:
    def __init__(self,pdf_location):
        self.pdf_location=pdf_location
        self.List_of_fonts=[]
        try:
            pdf=fitz.open(self.pdf_location)
            total_pages=len(pdf)
            for index in range(total_pages):
                page_font=pdf.getPageFontList(index)
                #print(page_font)
                for font in page_font:
                    if font[3] not in self.List_of_fonts:
                        self.List_of_fonts.append(font[3])
                #if pdf.getPageFontList(index)[2] not in self.List_of_fonts:
                #    self.List_of_fonts.append(pdf.getPageFontList(index)[2])
            print(self.List_of_fonts)
        finally:
            pdf.close()
if __name__=="__main__":
    pdf=get_file()
    if pdf[0]=="Submit":
        get_fonts(pdf[1])