from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Comment, Rating
from .serializers import ProductSerializer, CommentSerializer, RatingSerializer

# Produto: Listar todos os produtos
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# Produto: Detalhar um produto específico
@api_view(['GET'])
def get_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product)
    return Response(serializer.data)

# Produto: Criar um novo produto
@api_view(['POST'])
def create_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Produto: Atualizar um produto
@api_view(['PUT'])
def update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Produto: Deletar um produto
@api_view(['DELETE'])
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Comentário: Listar comentários de um produto
@api_view(['GET'])
def get_comments(request, product_id):
    comments = Comment.objects.filter(product_id=product_id)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

# Comentário: Criar um comentário para um produto
@api_view(['POST'])
def create_comment(request, product_id):
    if request.method == 'POST':
        data = request.data
        data['product'] = product_id
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Comentário: Atualizar um comentário
@api_view(['PUT'])
def update_comment(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Comentário: Deletar um comentário
@api_view(['DELETE'])
def delete_comment(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Avaliação: Listar avaliações de um produto
@api_view(['GET'])
def get_ratings(request, product_id):
    ratings = Rating.objects.filter(product_id=product_id)
    serializer = RatingSerializer(ratings, many=True)
    return Response(serializer.data)

# Avaliação: Criar uma avaliação para um produto
@api_view(['POST'])
def create_rating(request, product_id):
    if request.method == 'POST':
        data = request.data
        data['product'] = product_id
        serializer = RatingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

