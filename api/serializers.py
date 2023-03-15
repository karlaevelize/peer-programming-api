from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Project

class UserSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'projects']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'image_url', 'user_id']
        user_id = serializers.ReadOnlyField(source='user_id.id')
