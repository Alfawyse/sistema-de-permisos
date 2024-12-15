from rest_framework import serializers
from user.models.user import User
from user.models.role import Role
from user.models.permission import Permission

# Serializador para Usuarios
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id_user', 'user_username', 'user_email', 'user_phone', 'user_is_admin', 'user_is_active']

# Serializador para Roles
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id_role', 'role_name', 'role_description', 'role_active', 'company']

# Serializador para Permisos

class PermissionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='id_permi', read_only=True)

    class Meta:
        model = Permission
        fields = ['id', 'name', 'description', 'can_create', 'can_read', 'can_update', 'can_delete', 'can_import', 'can_export']
