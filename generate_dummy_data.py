import os
import django
import random
from faker import Faker
from django.contrib.auth.hashers import make_password

# Configuración del entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tecnical_test_fail_fast.settings')
django.setup()

# Importar modelos
from core.models import EntityCatalog, Company
from user.models import PermiUser, PermiRole, Permission, UserCompany
from user.models.user import User
from user.models.role import Role

# Inicializar Faker
fake = Faker()

def generate_data():
    # Crear Compañías
    print("Creando Compañías...")
    companies = []
    for i in range(3):  # Crear 3 compañías
        company = Company.objects.create(
            compa_name=fake.company(),
            compa_tradename=fake.company_suffix(),
            compa_doctype='NI',
            compa_docnum=fake.unique.random_number(digits=10),
            compa_address=fake.address(),
            compa_city=fake.city(),
            compa_state=fake.state(),
            compa_country=fake.country(),
            compa_industry=fake.bs(),
            compa_phone=fake.phone_number(),
            compa_email=fake.company_email(),
            compa_website=fake.url(),
            compa_active=True
        )
        companies.append(company)

    # Crear Entidades
    print("Creando Sucursales y Centros de Costos...")
    branch_offices = []
    cost_centers = []

    for company in companies:
        # Crear 3 sucursales por compañía
        for i in range(3):
            branch_office = EntityCatalog.objects.create(
                entit_name=f"Sucursal {fake.city()} - {company.compa_name}",
                entit_descrip=f"Sucursal de {company.compa_name} en {fake.city()}"
            )
            branch_offices.append(branch_office)

        # Crear 2 centros de costos por compañía
        for i in range(2):
            cost_center = EntityCatalog.objects.create(
                entit_name=f"Centro de Costos {fake.bs()} - {company.compa_name}",
                entit_descrip=f"Centro de costos de {company.compa_name} para {fake.catch_phrase()}"
            )
            cost_centers.append(cost_center)

    # Crear Permisos Descriptivos
    print("Creando Permisos Descriptivos...")
    permissions = []
    permission_data = [
        {"name": "Ver Usuarios", "can_read": True},
        {"name": "Crear Usuarios", "can_create": True},
        {"name": "Editar Usuarios", "can_update": True},
        {"name": "Eliminar Usuarios", "can_delete": True},
        {"name": "Ver Compañías", "can_read": True},
        {"name": "Editar Compañías", "can_update": True},
        {"name": "Acceso a Sucursales", "can_read": True},
        {"name": "Acceso a Centros de Costos", "can_read": True},
    ]

    for perm_data in permission_data:
        perm = Permission.objects.create(
            name=perm_data["name"],
            can_read=perm_data.get("can_read", False),
            can_create=perm_data.get("can_create", False),
            can_update=perm_data.get("can_update", False),
            can_delete=perm_data.get("can_delete", False)
        )
        permissions.append(perm)

    # Crear Roles Descriptivos
    print("Creando Roles Descriptivos...")
    roles = []
    role_data = [
        {"role_name": "Administrador Global", "description": "Acceso completo al sistema."},
        {"role_name": "Gerente de Compañía", "description": "Gestión de la compañía y usuarios."},
        {"role_name": "Usuario Regular", "description": "Acceso limitado a funcionalidades básicas."}
    ]

    for role_data in role_data:
        company = random.choice(companies)
        role = Role.objects.create(
            role_name=role_data["role_name"],
            company=company,
            role_description=role_data["description"],
            role_active=True
        )
        roles.append(role)

    # Asignar Permisos a Roles
    print("Asignando Permisos a Roles...")
    for role in roles:
        if role.role_name == "Administrador Global":
            for permission in permissions:
                entity = random.choice(branch_offices + cost_centers)  # Seleccionar una entidad válida
                PermiRole.objects.create(
                    role=role,
                    permission=permission,
                    entitycatalog=entity,  # Asignar una entidad válida
                    perol_include=True
                )
        elif role.role_name == "Gerente de Compañía":
            selected_permissions = [
                permissions[0],  # Ver Usuarios
                permissions[1],  # Crear Usuarios
                permissions[4],  # Ver Compañías
                permissions[5]  # Editar Compañías
            ]
            for permission in selected_permissions:
                entity = random.choice(branch_offices)  # Seleccionar una sucursal específica
                PermiRole.objects.create(
                    role=role,
                    permission=permission,
                    entitycatalog=entity,  # Asignar una entidad válida
                    perol_include=True
                )
        elif role.role_name == "Usuario Regular":
            selected_permissions = [
                permissions[0],  # Ver Usuarios
                permissions[6],  # Acceso a Sucursales
                permissions[7]  # Acceso a Centros de Costos
            ]
            for permission in selected_permissions:
                entity = random.choice(cost_centers)  # Seleccionar un centro de costos
                PermiRole.objects.create(
                    role=role,
                    permission=permission,
                    entitycatalog=entity,  # Asignar una entidad válida
                    perol_include=True
                )

        # Crear Usuarios y Relaciones Usuario-Compañía
        print("Creando Usuarios y Relaciones Usuario-Compañía...")
        user_companies = []

        for i in range(10):  # Crear 10 usuarios
            # Usar el manager para crear el usuario correctamente
            user = User.objects.create_user(
                user_username=fake.user_name()[:20],  # Trunca a 20 caracteres
                user_email=fake.unique.email(),
                password="password123",  # Contraseña segura por defecto
                user_phone=fake.phone_number()[:20],  # Trunca a 20 caracteres
                user_is_admin=random.choice([True, False]),
                user_is_active=True
            )

            # Asociar usuario a una compañía
            company = random.choice(companies)
            user_company = UserCompany.objects.create(
                user=user,
                company=company,
                useco_active=True
            )
            user_companies.append(user_company)

            print(f"Usuario {user.user_username} asociado a la compañía {company.compa_name}")

        # Asignar roles aleatorios a usuarios
        assigned_role = random.choice(roles)
        print(f"Usuario {user.user_username} asignado al rol {assigned_role.role_name} en la compañía {company.compa_name}")

    # Crear Permisos de Usuario
    print("Creando Permisos de Usuario...")
    for i in range(10):  # Crear 10 Permisos de Usuario
        user_company = random.choice(user_companies)
        permission = random.choice(permissions)
        entity = random.choice(branch_offices + cost_centers)

        if not PermiUser.objects.filter(usercompany=user_company, permission=permission, entitycatalog=entity).exists():
            PermiUser.objects.create(
                usercompany=user_company,
                permission=permission,
                entitycatalog=entity,
                peusr_include=random.choice([True, False])
            )

    print("Datos de prueba creados con éxito.")

if __name__ == '__main__':
    generate_data()

