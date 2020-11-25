from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('products', views.products, name="products"),
    path('blogs', views.blog_page, name="blogs"),
    path('blog/<str:pk>', views.blog_single, name="blog"),
    path('login', views.login_view, name="login"),
    path('register', views.register_view, name="register"),
    path('logout', views.logout_view, name="logout")
    # path('howitswork', views.how, name="how"),
    # path('about', views.about, name='about'),
    # path('product/<str:pk>/', views.product, name="product")
]