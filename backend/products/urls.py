from django.urls import path

from .views import product_detail_view,product_update_view, product_list_create_view, product_delete_view

urlpatterns = [
    path("", product_list_create_view ),
    path("<int:pk>/update" , product_update_view),
    path("<int:pk>/delete" , product_delete_view),
    path("<int:pk>/" , product_detail_view)
]