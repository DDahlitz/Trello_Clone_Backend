from django.urls import path, include
from .views import BoardDetail, BoardList, ItemList, ItemDetail, ListList, ListDetail

urlpatterns = [
    path('api/board', BoardList.as_view(), name='board_list'),
    path('api/board/<int:pk>/', BoardDetail.as_view(), name='board_detail'),
    path('api/items/', ItemList.as_view(), name='item_list'),
    path('api/items/<int:pk>/', ItemDetail.as_view(), name='item_detail'),
    path('api/lists/', ListList.as_view(), name='list_list'),
    path('api/lists/<int:pk>/', ListDetail.as_view(), name='list_detail'),
]