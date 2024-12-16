from rest_framework import serializers
from user.models.user import User
from user.models.role import Role
from user.models.permission import Permission
from core.models.entity_catalog import EntityCatalog
from user.models import PermiUser, PermiRole, PermiUserRecord, PermiRoleRecord

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

# PermiUser Serializer
class PermiUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermiUser
        fields = '__all__'

# PermiRole Serializer
class PermiRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermiRole
        fields = '__all__'

# PermiUserRecord Serializer
class PermiUserRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermiUserRecord
        fields = '__all__'

# PermiRoleRecord Serializer
class PermiRoleRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermiRoleRecord
        fields = '__all__'

# Serializador para Permisos
class PermissionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='id_permi', read_only=True)

    class Meta:
        model = Permission
        fields = ['id', 'name', 'description', 'can_create', 'can_read', 'can_update', 'can_delete', 'can_import', 'can_export']

from rest_framework import serializers
from core.models import EntityCatalog

class EntityCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityCatalog
        fields = "__all__"

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id_permi', 'name', 'description', 'can_create', 'can_read',
                  'can_update', 'can_delete', 'can_import', 'can_export']