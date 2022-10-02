from django.urls import path
from . import views

urlpatterns = [
    path('api/board', views.BoardList.as_view(), name='board_list'),
    path('api/board/<int:pk>', views.BoardDetail.as_view(), name='board_detail'),
    path('api/items/', views.ItemList.as_view(), name='item_list'),
    path('api/items/<int:pk>', views.ItemDetail.as_view(), name='item_detail'),
    path('api/lists/', views.ListList.as_view(), name='list_list'),
    path('api/lists/<int:pk>', views.ListDetail.as_view(), name='list_detail'),
]