from django.contrib import admin
from django.urls import path
from .views import deleteBookData,updateBookData
from .views import getBookData, deleteBook
urlpatterns = [

   path('api/',getBookData.as_view(), name ="Get Data"),
   path('api/<int:id>',deleteBook.as_view(),name="Delete Data")
   # path('api/<int:id>',deleteBookData,name="Delete Data"),
   # path('api/update/<int:id>',updateBookData,name="Update Book Data")

]
