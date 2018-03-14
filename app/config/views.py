from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.compat import authenticate
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser, AllowAny

from post.models import Post
from post.serializers import PostSerializer

from rest_framework import generics, mixins


# 믹스인 순서가 중요해요, 다른것 상관업슨ㄴ데 항상 제너릭ㄴ이 끝에 와야되요.
class PostList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        AllowAny,
    )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



    #그래서 에러가 뜨면 안되요.
# 만약에 못찾는다 그러면 이런게 와야되요.
# not found
# 그런데 웬만한거는 얘가 다해줘요