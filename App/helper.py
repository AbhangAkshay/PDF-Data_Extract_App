print("In Helper file")



import fitz
from app_req import data_dir, output_dir


def read_PDF_to_image(data_dir, output_dir, pdf_file):
    data_dir = data_dir
    output_folder = output_dir

    pdf_path = data_dir + '\\' + pdf_file
    print(pdf_path)
    
    doc = fitz.open(pdf_path)
    zoom = 4
    mat = fitz.Matrix(zoom, zoom)
    
    for i in range(doc.page_count):
        image_path = f"{output_folder}/image_{i+1}.jpg"
        page = doc.load_page(i)
        pix = page.get_pixmap(matrix=mat, dpi=300)
        pix.save(image_path)
        print(f"Saved Page at {image_path}")
        break
    doc.close()