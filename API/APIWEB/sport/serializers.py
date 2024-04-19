from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import User


#
# class UserModel:
#     def __int__(self, id_user, first_name, sur_name, last_name, age):
#         self.id_user = id_user
#         self.first_name = first_name
#         self.sur_name = sur_name
#         self.last_name = last_name
#         self.age = age
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        # ("id_user", "first_name", "sur_name", "last_name", "age", "lsport")
    # id_user = serializers.IntegerField()
    # first_name = serializers.CharField(max_length=15)
    # sur_name = serializers.CharField(max_length=15)
    # last_name = serializers.CharField(max_length=15)
    # age = serializers.CharField(max_length=10)
    # time_create = serializers.DateTimeField(read_only=True)
    # time_update = serializers.DateTimeField(read_only=True)
    # lsport_id = serializers.IntegerField()
    #
    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.id_user = validated_data.get("id_user",instance.id_user)
    #     instance.first_name = validated_data.get("first_name", instance.first_name)
    #     instance.sur_name = validated_data.get("sur_name", instance.sur_name)
    #     instance.last_name = validated_data.get("last_name", instance.last_name)
    #     instance.age = validated_data.get("age", instance.age)
    #     instance.time_create = validated_data.get("time_create", instance.time_create)
    #     instance.time_update = validated_data.get("time_update", instance.time_update)
    #     instance.lsport_id = validated_data.get("lsport_id", instance.lsport_id)
    #     instance.save()
    #     return instance
#
# def encode():
#     model = UserModel()
#     model_sr = UserSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
