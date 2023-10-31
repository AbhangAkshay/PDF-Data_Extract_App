import os
import fitz



print("In app file")


class PDF:

    def __init__(self) -> None:
        self.data_dir = r"App\Data"
        self.output_dir = r"App\Output"

    def read_PDF_to_image(self, pdf_file):
        data_dir = self.data_dir
        output_folder = self.output_dir

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
        doc.close()
        
    def load_pdf_file(self):
        print("In load_pdf_file")
        data_dir = self.data_dir
        files = os.listdir(data_dir)
        pdf_file = files[0]
        return pdf_file



