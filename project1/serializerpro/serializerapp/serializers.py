from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    def create(self, validated_data):
        return Comment(**validated_data)