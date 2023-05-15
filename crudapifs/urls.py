from .views import post_list, consultar
# from .views import consultaapi

from django.urls import path
# from  import formulario
urlpatterns = [
    path('consulta/', consultar, name='consultar'),
    path('posts/', post_list, name='post_list'),
]
