from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import predict, ProductSerializer


@api_view(['GET'])
def recommendation_list(request, userId):
    listProduct = predict(userId)
    productSerializers = ProductSerializer(listProduct, many=True)
    return Response(productSerializers.data,)
