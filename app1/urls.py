from django.urls import path
from . import views

app_name = "newapp"
urlpatterns = [
    path('', views.index, name='index'),
    path('checkpost/<int:post_id>', views.CheckPost, name='CheckPost'),
    path('download_word_doc/<int:post_id>', views.download_word_doc, name='download_word_doc'),
]
