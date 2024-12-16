from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import (
    UserListCreateView, UserRetrieveUpdateDestroyView,
    RoleListCreateView, RoleRetrieveUpdateDestroyView,
    PermissionListCreateView, PermissionRetrieveUpdateDestroyView,
    UserPermissionsView, EntityCatalogViewSet, user_info,
    PermiUserViewSet, PermiRoleViewSet, PermiUserRecordViewSet, PermiRoleRecordViewSet
)

# Router para ViewSets
router = DefaultRouter()
router.register(r'permiuser', PermiUserViewSet, basename='permiuser')
router.register(r'permirole', PermiRoleViewSet, basename='permirole')
router.register(r'permiuserrecord', PermiUserRecordViewSet, basename='permiuserrecord')
router.register(r'permirolerecord', PermiRoleRecordViewSet, basename='permirolerecord')

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

    # Rutas para EntityCatalog
    path('entity-catalogs/', EntityCatalogViewSet.as_view({'get': 'list', 'post': 'create'}), name='entity-catalog-list-create'),
    path('entity-catalogs/<int:pk>/', EntityCatalogViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='entity-catalog-detail'),

    # Ruta para información del usuario autenticado
    path('me/', user_info, name='user-info'),

    # Incluir rutas de router
    path('', include(router.urls)),
]
