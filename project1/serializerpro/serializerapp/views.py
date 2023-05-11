from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Comment
from .serializers import CommentSerializer
# Create your views here.

class Checking(APIView):
    def get(self, request, format=None):
        snippet = Comment.objects.all()
        serializer = CommentSerializer(snippet, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckingDetail(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        # id=request.GET["id"]
        snippet = self.get_object(pk)
        serializer = CommentSerializer(snippet)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        titlle_new = request.data["title"]
        snippet.title = titlle_new
        snippet.save()
        serializer = CommentSerializer(snippet)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CommentSerializer(snippet)
        snippet.delete()
        return Response(serializer.data)