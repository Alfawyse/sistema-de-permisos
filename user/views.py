from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from user.models.user import User
from user.models.role import Role
from user.models.permission import Permission
from user.serializers import UserSerializer, RoleSerializer, PermissionSerializer
from user.filters import UserFilter, RoleFilter
from user.permissions import IsGlobalAdmin, HasRolePermission, HasSpecificPermission  # Importa permisos personalizados

# Vista para Usuarios con Filtros, Paginación y Permisos
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Solo autenticados pueden acceder

# Vista para Roles con Filtros, Paginación y Permisos
class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoleFilter
    permission_classes = [IsAdminUser]  # Solo administradores pueden acceder

class RoleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdminUser]  # Solo administradores pueden acceder

# Vista para Permisos con Restricción Personalizada
class PermissionListCreateView(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [HasSpecificPermission]  # Permiso personalizado

class PermissionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [HasSpecificPermission]  # Permiso personalizado
