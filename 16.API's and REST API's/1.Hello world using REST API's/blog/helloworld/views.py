from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from helloworld.serialazers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from helloworld.models import Post
from rest_framework.permissions import IsAuthenticated
from helloworld.permissions import IsPostPossessor
from rest_framework import filters
from helloworld.filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class HelloworldView(APIView):
    def get(self, request):
        return Response({'Message': 'Hello World'})

class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter , filters.OrderingFilter]
    ordering_fields = ['id']
    filter_class =PostFilter # Fix typo in filter_backends
    search_fields = ['title', 'content']

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)
