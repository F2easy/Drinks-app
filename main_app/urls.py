from django.urls import path
from . import views 


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('index/', views.drinks_index, name='drinks_index'),
  path('show/<int:id_drink>', views.show_page, name='show'),
  path('add_to_shopping_list/<str:ingredient_name>/', views.add_to_shopping_list, name='add_to_shopping_list'),
  path('ShoppingList/', views.ShoppingList, name ='ShoppingList'),
  path('delete_from_shopping_list/<int:ingredient_id>/', views.delete_from_shopping_list, name='delete_from_shopping_list')
]