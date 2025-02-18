from pdf2docx import Converter, parse   

pdf_file = r'./RESCISÃO_Mateus Cardoso Batista - TRCT.pdf'
doc_file = r'./RESCISÃO_Mateus Cardoso Batista - TRCT.docx'

# Converter todas as páginas
cv = Converter(pdf_file)
cv.convert(doc_file)
cv.close()

# Metodo alternativo é o parse

