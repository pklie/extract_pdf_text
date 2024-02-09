import sys
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path, txt_path):
    # Open the PDF file
    with fitz.open(pdf_path) as doc:
        text = ""
        # Iterate through each page
        for page in doc:
            # Extract text from the page
            text += page.get_text()

    # Write the extracted text to a TXT file
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.pdf output.txt")
    else:
        pdf_path = sys.argv[1]
        txt_path = sys.argv[2]
        extract_text_from_pdf(pdf_path, txt_path)
        print(f"Text extracted from {pdf_path} and saved to {txt_path}")

