import PyPDF2
import sys
import os 

inputs = sys.argv[1:]

def PdfCombiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()

    for pdf in pdf_list:
        merger.append(pdf)
    # Write to an output PDF document
    merger.write('new_super.pdf')
    
PdfCombiner(inputs)

os.remove('super.pdf')

    

