from django.shortcuts import render
from django.contrib.auth import get_user_model
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Post
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializers, UserSerializers
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly

class PostViewsSet(ModelViewSet):    #post uchun
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class UserViewsSet(ModelViewSet):    # foydalanuvchilar uchun
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers



# class ListPost(ListCreateAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers

# class DetailPost(RetrieveUpdateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers

# class UserList(ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializers

# class UserDetail(RetrieveUpdateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializers



