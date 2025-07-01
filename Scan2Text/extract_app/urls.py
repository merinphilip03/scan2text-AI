from django.urls import path
from extract_app import views

urlpatterns = [
    path('file/', views.upload_documents, name='upload_files')
]
