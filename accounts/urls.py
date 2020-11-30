from django.urls import path
from .views import home, products, customer, createOrder, updateOrder, deleteOrder, registerPage, loginPage, logoutUser, userPage, accountSettings
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('user/', userPage, name='user-page'),
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('customer/<str:pk>/', customer, name='customer'),
    path('account/', accountSettings, name='account'),
    path('create_order/<str:pk>/', createOrder, name='create_order'),
    path('update_order/<str:pk>/', updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', deleteOrder, name='delete_order'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), name= 'password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_complete'),
]