from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('success/', views.success, name='success'),
    path('generate-questions-document/', views.generate_questions_document, name='generate_questions_document'),
    path('generate-questions/', views.generate_questions, name='generate_questions'),
    path('add-question/', views.add_question_view, name='add_question'),
]
