from django.urls import path 
from sandwhichapp.views import SandwhichappView, IngredientsListView, SandwichGeneratorView, FullMenuView

urlpatterns = [path('', SandwhichappView.asview(), name='sandwhich'),
    path('ingredients/<str:ingredient_type>', IngredientsListView.as_view(), name='ingredients_list'),
    path('random', SandwichGeneratorView.as_view(), name='sandwich_generator'),
    path('Menu', FullMenuView.as_view(), name='menu'),
    ]
