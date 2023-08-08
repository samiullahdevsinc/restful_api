from django.shortcuts import render, redirect
from .serializers import BookSerializer
from .models import book
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class getBookData(APIView):
	def get(self,request):
		books = book.objects.all()
		bookSerializer = BookSerializer(books,many=True)
		return Response(bookSerializer.data)
	def post(self,request):
		serializer = BookSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializers)
		else:
			return Response(serializer.errors)
class deleteBook(APIView):
	def get(self,request,id):
		deleteBook = book.objects.get(id=id)
		serial = BookSerializer(deleteBook)
		return Response(serial.data)
	def delete(self, request, id):
		deleteBook = book.objects.get(id=id)
		deleteBook.delete()
		return Response("Book has been deleted")


# @csrf_exempt
# def getBookData(request):
# 	if request.method == "GET":
# 		books = book.objects.all()
# 		bookSerializer = BookSerializer(books,many=True)
# 		return JsonResponse(bookSerializer.data,safe=False)
# 	elif request.method == "POST":
# 		data = JSONParser().parse(request)
# 		serialize = BookSerializer(data=data)
# 		if serialize.is_valid():
# 			serialize.save()
# 			return JsonResponse(serialize.data,status = 201)
# 		return JsonResponse(serialize.error, status = 400)

@csrf_exempt
def deleteBookData(request,id):
	bookd = book.objects.get(id=id)
	bookd.delete()
	return redirect('/api')

@csrf_exempt
def updateBookData(request,id):
	booku = book.objects.get(id = id)
	data=JSONParser().parse(request)
	serialize = BookSerializer(booku, data=data)
	if serialize.is_valid():
		serialize.save()
		return JsonResponse(serialize.data)
	else:
		return JsonResponse(serialize.error)