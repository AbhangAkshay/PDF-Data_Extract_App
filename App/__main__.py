print("App running......")


from app import PDF
from app_req import data_dir, output_dir

obj = PDF()

file_name = "HealthReport_2022_06_20_4_15_21_199"
obj.load_pdf_file(data_dir,output_dir,  file_name)

page_no = 1
keywords = "Patient Name"
obj.func2(page_no)


