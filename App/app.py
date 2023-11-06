print("In app file")

import os
from helper import read_PDF_to_image




class PDF:

    def __init__(self) -> None:
        pass
        
    def load_pdf_file(self, data_dir,output_dir,  file_name):
        print("In load_pdf_file")
        data_dir = data_dir
        files = os.listdir(data_dir)
        # print(files)
        # print(file_name)

        pdf_file = [i for i in files if file_name in i][0]

        read_PDF_to_image(data_dir, output_dir,  pdf_file )
        
        
        # read_PDF_to_image(pdf_file)



