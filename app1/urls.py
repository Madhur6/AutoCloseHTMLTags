from django.urls import path
from . import views

app_name = "newapp"
urlpatterns = [
    path('', views.index, name='index'),
    path('checkpost/<int:post_id>', views.CheckPost, name='CheckPost'),
    path('display/', views.display, name='display'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('download_word_doc/<int:post_id>', views.download_word_doc, name='download_word_doc'),
]
