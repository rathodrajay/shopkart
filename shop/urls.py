from django.urls import path
from .import views as v
urlpatterns = [
    path('',v.home,name="home"),
    path('register',v.register,name="register"),
    path('login',v.login_page,name="login"),
    path('logout',v.logout_page,name="logout"),
    path('cart',v.cart_page,name="cart"),
    path('remove_cart/<int:cid>',v.remove_cart,name="remove_cart"),
    path('remove_fav/<str:fid>',v.remove_fav,name="remove_fav"),
    path('favviewpage',v.favviewpage,name="favviewpage"),
    path('fav',v.fav_page,name="fav"),
    path('collections',v.collections,name="collections"),
    path('collectionsfav',v.collectionsfav,name="collectionsfav"),
    path('collections/<str:name>',v.collectionsview,name="collections"),
    path('collections/<str:cname>/<str:pname>',v.product_details,name="product_details"),
    path('addtocart',v.add_to_cart,name="addtocart"),
]