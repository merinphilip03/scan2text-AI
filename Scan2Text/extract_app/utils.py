import os
from PIL import Image
import fitz
import pytesseract
import io


def extract_text_img(img_path):
    if isinstance(img_path, str):
        im = Image.open(img_path)
    elif isinstance(img_path, bytes):
        im = Image.open(io.BytesIO(img_path))
    else:
        print("error")
    result = pytesseract.image_to_string(im)
    return result


def extract_text_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    comb_text = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        comb_text += text

        image_list = page.get_images(full=True)
        for img_num, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_text = extract_text_img(image_bytes)
            print(image_text)

            comb_text += "\n"
            comb_text += "\n--- OCR from Page ---\n"
            comb_text += image_text

    return comb_text
