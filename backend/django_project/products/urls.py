from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProductListCreateApiView.as_view(),name = 'product-list'),
    path('<int:pk>/update/', views.ProductUpdateApiView.as_view(),name = 'product-edit'),
    path('<int:pk>/delete/', views.ProductDeleteApiView.as_view()),
    path('<int:pk>/', views.ProductDetailApiView.as_view(),name = 'product-detail')

]



