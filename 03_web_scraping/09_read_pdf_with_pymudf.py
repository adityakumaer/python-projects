import fitz


def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()
    return text

def main():
    file_path = input("Enter the path to the PDF file: ")
    pdf_text = read_pdf(file_path)
    print("\nPDF Content:\n")
    print(pdf_text)

if __name__ == "__main__":
    main()