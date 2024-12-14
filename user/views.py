from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from user.models.user import User
from user.models.role import Role
from user.models.permission import Permission
from user.serializers import UserSerializer, RoleSerializer, PermissionSerializer
from user.filters import UserFilter, RoleFilter

# Vista para Usuarios con Filtros y Paginación
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Vista para Roles con Filtros y Paginación
class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoleFilter

class RoleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

# Vista para Permisos (sin filtros por ahora)
class PermissionListCreateView(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class PermissionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
