from django.urls import path
from bookapp import views

urlpatterns=[
    path('',views.index),
    path('addbook',views.addBook),
    path('delete/<bookid>',views.deleteBook),
    path('update/<bookid>',views.updateBook,name='update')
] 