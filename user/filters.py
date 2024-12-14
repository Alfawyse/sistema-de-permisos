import django_filters
from user.models.user import User
from user.models.role import Role

# Filtro para Usuarios
class UserFilter(django_filters.FilterSet):
    user_is_active = django_filters.BooleanFilter(field_name="user_is_active")
    user_is_admin = django_filters.BooleanFilter(field_name="user_is_admin")
    user_username = django_filters.CharFilter(lookup_expr='icontains')  # Búsqueda parcial por nombre de usuario

    class Meta:
        model = User
        fields = ['user_is_active', 'user_is_admin', 'user_username']

# Filtro para Roles
class RoleFilter(django_filters.FilterSet):
    role_active = django_filters.BooleanFilter(field_name="role_active")
    role_name = django_filters.CharFilter(lookup_expr='icontains')  # Búsqueda parcial por nombre de rol

    class Meta:
        model = Role
        fields = ['role_active', 'role_name']
