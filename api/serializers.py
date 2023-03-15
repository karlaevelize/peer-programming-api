from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=30)
    active = serializers.BooleanField()
    avatar_url = serializers.CharField(default='https://uploads-ssl.webflow.com/6198a2e43048192ebafec2cc/63d221403d9cfe4ced015d95_yxRQH9s6VEU6gldnFhl3PDigUW31MIHSSqavg8i9s24.png', max_length=15)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.active = validated_data.get('active', instance.active)
        instance.avatar_url = validated_data.get('language', instance.avatar_url)
        instance.save()
        return instance
