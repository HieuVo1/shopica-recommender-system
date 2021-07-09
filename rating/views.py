from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CommentSerializer, generate_model
from .models import Comment
# Create your views here.


@api_view(['GET'])
def getListComment(request):
    generate_model()
    comments = Comment.objects.filter(productId__isnull=False)
    commentSerializers = CommentSerializer(comments, many=True)
    return Response(commentSerializers.data)
