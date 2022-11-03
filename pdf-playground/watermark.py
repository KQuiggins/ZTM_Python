import PyPDF2

watermark_template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(watermark_template.getNumPages()):
    page = watermark_template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    with open(f'watermarked_output.pdf', 'wb') as file:
        output.write(file)