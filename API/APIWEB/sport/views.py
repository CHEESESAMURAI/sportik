
from django.db.migrations import serializer
from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import User, Category
from .serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet): #ReadOnlyModelViewSet - только чтение
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

#переопределение кверисета для более сложных запросов

    # def get_queryset(self):
    #     pk = self.kwargs.get("pk")
    #
    #     if not pk:
    #         return User.objects.all()[:3] #Указать basename в urls
    #
    #     return User.objects.filter(pk=pk)

    @action(methods=['get'], detail = False)
    def ages(self, request):
        users = User.objects.all()
        return Response({'age': [c.age for c in users]})

    @action(methods=['get'], detail=False)
    def categories(self, request):
        users = Category.objects.all()
        return Response({'categories': [c.name for c in users]})

    @action(methods=['get'], detail=True)
    def cats(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

# class UserAPIList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class UserAPIUpdate(generics.UpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class UserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class SportAPIView(APIView):
#     def get(self,requests):
#         u = User.objects.all()
#         return Response({'posts': UserSerializer(u, many=True).data})
#
#     def post(self, requests):
#         serializer = UserSerializer(data = requests.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#     def put(self, requests, *args, **kwargs):
#         pk = kwargs.get("pk",None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = User.objects.get(pk=pk)
#         except:
#             return Response({"error": "Objects does not exists"})
#
#         serializer = UserSerializer(data=requests.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
# def delete(self,requests, *args, **kwargs):
#     pk = kwargs.get("pk",None)
#     if not pk:
#         return Response({"error": "Method DELETED not allowed"})
#
#     return Response({"post": "deleted post"+str(pk)})

# post_new = User.objects.create(
#     id_user = requests.data['id_user'],
#     first_name = requests.data ['first_name'],
#     sur_name = requests.data['sur_name'],
#     last_name = requests.data['last_name'],
#     age = requests.data['age'],
#     lsport_id = requests.data['lsport_id']
# )
# return Response({'post':serializer.data})


# class SportAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
