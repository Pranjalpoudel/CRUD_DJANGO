from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='item_list'),
    path('item/new/', views.ItemCreateView.as_view(), name='item_create'),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('item/<int:pk>/edit/', views.ItemUpdateView.as_view(), name='item_update'),
    path('item/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item_delete'),
    path('category/new/', views.CategoryCreateView.as_view(), name='category_create'),
]
