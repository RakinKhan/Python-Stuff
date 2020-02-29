import PyPDF2
import sys

inputs = sys.argv[1:]


def waterMarking(pdfFiles):
    watermark = pdfFiles[0]
    pdfToMerge = pdfFiles[1]

    with open(pdfToMerge, 'rb') as original:
        org = PyPDF2.PdfFileReader(original)

        with open(watermark, 'rb') as watermark_page:
            watermarkpage = PyPDF2.PdfFileReader(watermark_page)
            with open('edited.pdf', 'wb') as edited:
                wtrversion = PyPDF2.PdfFileWriter()
                for x in range(org.getNumPages()):
                    page = org.getPage(x)
                    page.mergePage(watermarkpage.getPage(0))
                    wtrversion.addPage(page)
                wtrversion.write(edited)


waterMarking(inputs)
