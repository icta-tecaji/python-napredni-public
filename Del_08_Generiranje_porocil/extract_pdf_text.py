from pathlib import Path

from PyPDF2 import PdfFileReader


def extract_pdf_text(
    path, output_path="Del_08_Generiranje_porocil/data/pdf_output.txt"
):
    pdf_reader = PdfFileReader(str(path))
    output_file_path = Path.cwd() / output_path

    text_all = []
    with output_file_path.open(mode="w") as output_file:
        title = pdf_reader.documentInfo.title
        num_pages = pdf_reader.getNumPages()
        output_file.write(f"{title}\\nNumber of pages: {num_pages}\\n\\n")

        for page in pdf_reader.pages:
            text = page.extractText()
            output_file.write(text)
            text_all.append(text)

    return text_all


if __name__ == "__main__":
    pdf_path = Path.cwd() / "Del_08_Generiranje_porocil" / "data" / "sample.pdf"

    text = extract_pdf_text(pdf_path)
    print(text)
