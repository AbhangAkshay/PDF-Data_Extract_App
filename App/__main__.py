print("App running......")


from app import PDF

obj = PDF()
pdf_file = obj.load_pdf_file()

obj.read_PDF_to_image(pdf_file)