from django.urls import path
from . import views 


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('show/<int:id_drink>', views.show_page, name='show'),
  path('random/', views.random_index, name='random'),
  path('shopping_guide/', views.ShoppingGuideList.as_view(), name='shopping_index'),
  path('shopping_guide/<int:pk>/', views.ShoppingGuideDetail.as_view(), name='shopping_detail'),
  path('shopping_guide/<int:pk>/update/', views.ShoppingGuideUpdate.as_view(), name='shopping_update'),
  path('shopping_guide/create/', views.create_shopping_guide, name='shopping_create'),
  path('shopping_guide/delete/', views.ShoppingGuideDelete.as_view(), name='shopping_delete'),
  path('accounts/signup/', views.signup, name='signup'),

  
]