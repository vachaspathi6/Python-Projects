from PyPDF2 import PdfFileMerger

def merge_pdfs(pdf_files, output_filename):
    merger = PdfFileMerger()
    for pdf_file in pdf_files:
        merger.append(pdf_file)
    merger.write(output_filename)
    merger.close()
    print("PDFs merged successfully!")

def main():
    pdf_files = input("Enter PDF files (separated by comma): ").split(',')
    output_filename = input("Enter output filename: ")
    merge_pdfs(pdf_files, output_filename)

if __name__ == "__main__":
    main()
