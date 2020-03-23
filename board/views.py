from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Ad, Comment, Tag
from .serializers import AdSerializer, CommentSerializer, TagSerializer


class AdListView(generics.ListCreateAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]


class AdDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]


class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [IsAuthenticated]


class TagCreateView(generics.CreateAPIView):
    serializer_class = TagSerializer
    queryset = TagSerializer
    permission_classes = [IsAuthenticated]