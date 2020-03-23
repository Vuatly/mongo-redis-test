from rest_framework import serializers

from .models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text']


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'user', 'title', 'body', 'tags', 'comments']
        read_only_fields = ['comments']

    def to_representation(self, instance):
        representation = super(AdSerializer, self).to_representation(instance)
        representation['tags'] = TagSerializer(instance.tags.all(), many=True).data
        representation['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return representation
