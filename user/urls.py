from django.urls import path
from user.views import (
    UserListCreateView, UserRetrieveUpdateDestroyView,
    RoleListCreateView, RoleRetrieveUpdateDestroyView,
    PermissionListCreateView, PermissionRetrieveUpdateDestroyView,
    UserPermissionsView, EntityCatalogListCreateView, EntityCatalogRetrieveUpdateDestroyView
)


urlpatterns = [
    # Rutas para Usuarios
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),

    # Rutas para Roles
    path('roles/', RoleListCreateView.as_view(), name='role-list-create'),
    path('roles/<int:pk>/', RoleRetrieveUpdateDestroyView.as_view(), name='role-detail'),

    # Rutas para Permisos
    path('permissions/', PermissionListCreateView.as_view(), name='permission-list-create'),
    path('permissions/<int:pk>/', PermissionRetrieveUpdateDestroyView.as_view(), name='permission-detail'),
    path('permissions/user/', UserPermissionsView.as_view(), name='user-permissions'),

    path('entity-catalogs/', EntityCatalogListCreateView.as_view(), name='entity-catalog-list-create'),
    path('entity-catalogs/<int:pk>/', EntityCatalogRetrieveUpdateDestroyView.as_view(), name='entity-catalog-detail'),
]
