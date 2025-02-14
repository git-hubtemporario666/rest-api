from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_products),
    path('products/<int:pk>/', views.get_product),
    path('products/create/', views.create_product),
    path('products/<int:pk>/update/', views.update_product),
    path('products/<int:pk>/delete/', views.delete_product),

    path('products/<int:product_id>/comments/', views.get_comments),
    path('products/<int:product_id>/comments/create/', views.create_comment),
    path('comments/<int:pk>/update/', views.update_comment),
    path('comments/<int:pk>/delete/', views.delete_comment),

    path('products/<int:product_id>/ratings/', views.get_ratings),
    path('products/<int:product_id>/ratings/create/', views.create_rating),
]
