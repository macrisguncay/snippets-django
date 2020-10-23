from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.urls import path, include

from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)


# para trabajar con vistas basadas en clases
# Si vamos a tener una API con Hyperlinked, debemos asegurarnos de nombrar nuestros patrones de URL.
# urlpatterns = [
#     path('', views.api_root),
#     path('snippets/',
#         views.SnippetList.as_view(),
#         name='snippet-list'),
#     path('snippets/<int:pk>/',
#         views.SnippetDetail.as_view(),
#         name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/',
#         views.SnippetHighlight.as_view(),
#         name='snippet-highlight'),
#     path('users/',
#         views.UserList.as_view(),
#         name='user-list'),
#     path('users/<int:pk>/',
#         views.UserDetail.as_view(),
#         name='user-detail')
# ]

# urlpatterns += [
#     # puede ser cualquier URL que desee utilizar.
#     path('api-auth/', include('rest_framework.urls')),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)


# vincular las url de forma explicita con viewsets
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

# con los viewset no se necesita configurar las rutas eso lo puede hacer el router
urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])

urlpatterns += [
    # puede ser cualquier URL que desee utilizar.
    path('api-auth/', include('rest_framework.urls')),
]

# Create a router and register our viewsets with it.
# La DefaultRouterclase que estamos usando también crea automáticamente la vista raíz de la API para nosotros, por lo que ahora podemos eliminar el api_rootmétodo de nuestro viewsmódulo.
# router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)
# router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]