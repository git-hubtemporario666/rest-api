from rest_framework import serializers
from .models import Product, Comment, Rating

# Serializador para Produto
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock']

# Serializador para Comentário
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'product', 'author', 'text', 'created_at', 'updated_at', 'likes', 'dislikes']

# Serializador para Avaliação
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'product', 'author', 'rating', 'created_at']
