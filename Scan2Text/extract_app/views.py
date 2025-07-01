from django.shortcuts import render
from .forms import DocumentForm
from .models import UploadedDocs
from .utils import extract_text_img, extract_text_pdf
import os


def upload_documents(request):
    extracted_text = ""
    file_url = None
    is_pdf = False
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save()
            uploaded_file = request.FILES['file']
            file_path = doc.file.path
            if uploaded_file.name.lower().endswith('.pdf'):
                extracted_text = extract_text_pdf(file_path)
                is_pdf = True
            else:
                extracted_text = extract_text_img(file_path)
            doc.extracted_text = extracted_text
            doc.save()
            file_url = doc.file.url
            return render(request, 'upload.html', {'form': form, 'extracted_text': extracted_text, 'file_url': file_url, 'is_pdf': is_pdf})

    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form, 'extracted_text': extracted_text})
