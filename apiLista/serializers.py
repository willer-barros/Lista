from rest_framework import serializers
from .models import Task, User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ("data_criacao",)
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"