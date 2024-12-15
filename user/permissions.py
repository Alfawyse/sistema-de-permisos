from rest_framework.permissions import BasePermission

# Permiso: Solo Administradores Globales
class IsGlobalAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_is_admin

# Permiso: Acceso según Rol
class HasRolePermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        return user.roles.filter(role_name="Gerente de Compañía").exists()

# Permiso: Acceso según Permiso Específico
class HasSpecificPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        # Verifica si el usuario tiene el permiso "Ver Usuarios"
        return user.permissions.filter(name="Ver Usuarios").exists()
