from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from user.models.role import Role
from user.models.permission import Permission
from user.serializers import UserSerializer, RoleSerializer, PermissionSerializer, EntityCatalogSerializer
from user.filters import UserFilter, RoleFilter
from user.permissions import IsGlobalAdmin, HasRolePermission, HasSpecificPermission  # Importa permisos personalizados

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db import connection
from user.permissions import HasSpecificPermission
from user.models.user import User
from core.models.entity_catalog import EntityCatalog

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

# Vista para listar y crear EntityCatalog
class EntityCatalogListCreateView(generics.ListCreateAPIView):
    queryset = EntityCatalog.objects.all()
    serializer_class = EntityCatalogSerializer
    permission_classes = [IsAuthenticated]

# Vista para detalles, actualización y eliminación de EntityCatalog
class EntityCatalogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EntityCatalog.objects.all()
    serializer_class = EntityCatalogSerializer
    permission_classes = [IsAuthenticated]

# Función de utilidad para llamar al procedimiento almacenado
def obtener_permisos_usuario(user_id, entity_id):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM get_user_permissions(%s, %s);
        """, [user_id, entity_id])
        filas = cursor.fetchall()
    return [
        {
            "nombre_permiso": fila[0],
            "puede_crear": fila[1],
            "puede_leer": fila[2],
            "puede_actualizar": fila[3],
            "puede_eliminar": fila[4],
        }
        for fila in filas
    ]

# Nueva vista para obtener permisos del usuario en una entidad específica
class UserPermissionsView(APIView):
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

    def get(self, request):
        user_id = request.query_params.get('user_id')
        entity_id = request.query_params.get('entity_id')

        if not user_id or not entity_id:
            return Response(
                {"error": "Se requieren los parámetros 'user_id' y 'entity_id'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            permisos = obtener_permisos_usuario(int(user_id), int(entity_id))
            return Response({"permisos": permisos}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)