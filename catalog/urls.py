from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('add/', views.ProductCreateView.as_view(), name='add_product'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/unpublish/', views.unpublish_product, name='unpublish_product'),
    path('category/<int:category_id>/', views.ProductsByCategoryView.as_view(), name='products_by_category'),
]
