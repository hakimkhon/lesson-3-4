from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Post
from .serializers import PostSerializers
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly

class ListPost(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class DetailPost(RetrieveUpdateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers



