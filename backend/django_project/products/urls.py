from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProdductMixinView.as_view()),
    path('<int:pk>/update/', views.ProdductMixinView.as_view()),
    path('<int:pk>/delete/', views.ProdductMixinView.as_view()),
    path('<int:pk>/', views.ProdductMixinView.as_view())

]



