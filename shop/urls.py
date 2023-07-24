from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_slug>/',
         views.home, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/',
         views.productpage, name='product_detail'),
    path('cart/add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('cart/add/<int:product_id>/', views.direct_add, name='direct_add'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/remove/<int:product_id>/',
         views.cart_remove, name='cart_remove'),
    path('cart/remove_product/<int:product_id>/',
         views.cart_remove_product, name='cart_remove_product'),
    ##path('order_history/', views.orderHistory, name='order_history'),
    ##path('order/<int:order_id>/', views.viewOrder, name='order_detail'),
    path('thankyou/<int:order_id>', views.thanks_page, name='thanks_page'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/dashboard/', views.dashboard, name='dashboard'),
    path('order/<int:order_id>/', views.viewOrder, name='order_detail'),
    path('search/', views.searchResult, name='searchResult'),
]
