from pdf2docx import Converter, parse   

pdf_file = r'./Dispensa por Termino do Contrato Experiência IZABELLE.pdf'
doc_file = r'./Dispensa por Termino do Contrato Experiência IZABELLE.docx'

# Converter todas as páginas
cv = Converter(pdf_file)
cv.convert(doc_file)
cv.close()

# Metodo alternativo é o parse

