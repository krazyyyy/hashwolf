from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('products', views.products, name="products")
    # path('howitswork', views.how, name="how"),
    # path('about', views.about, name='about'),
    # path('product/<str:pk>/', views.product, name="product")
]