from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializers, CommentSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated] 
    authentication_classes = [TokenAuthentication]
    #permission_classes = [permissions.AllowAny]

    #filto por autor
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['id_author']
    
    serializer_class = PostSerializers
    
    def perform_create(self, serializer):
        serializer.save(id_author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated] 
    authentication_classes = [TokenAuthentication]
    #permission_classes = [permissions.AllowAny]

    #filto por autor
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['id_author','post']
    
    serializer_class = CommentSerializers

    def perform_create(self, serializer):
        serializer.save(id_author=self.request.user)
    


    
        