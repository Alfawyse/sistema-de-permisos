import os
import django
import random
from faker import Faker
from django.contrib.auth.hashers import make_password

# Configuración del entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tecnical_test_fail_fast.settings')
django.setup()

# Importar modelos
from ERP.models import BranchOffice, CostCenter
from core.models import EntityCatalog, Company
from user.models import PermiUser, PermiRole, Permission, UserCompany
from user.models.user import User
from user.models.role import Role
from user.models.permi_role_record import PermiRoleRecord
from user.models.permi_user_record import PermiUserRecord

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

    # Crear Sucursales y Centros de Costos
    print("Creando Sucursales y Centros de Costos...")
    entity_catalogs = []  # Para almacenar registros de EntityCatalog

    for company in companies:
        # Crear 3 sucursales por compañía
        for i in range(3):
            branch_office = BranchOffice.objects.create(
                company=company,
                broff_name=f"Sucursal {fake.city()}",
                broff_code=f"BR-{random.randint(100, 999)}",
                broff_address=fake.address(),
                broff_city=fake.city(),
                broff_state=fake.state(),
                broff_country=fake.country(),
                broff_phone=fake.phone_number(),
                broff_email=fake.email(),
                broff_active=True
            )
            # Registrar en EntityCatalog
            entity_catalog = EntityCatalog.objects.create(
                entit_name=branch_office.broff_name,
                entit_descrip=f"Sucursal de {company.compa_name}",
                company=company
            )
            entity_catalogs.append(entity_catalog)

        # Crear 2 centros de costos por compañía
        for i in range(2):
            cost_center = CostCenter.objects.create(
                company=company,
                cosce_name=f"Centro de Costos {fake.bs()}",
                cosce_code=f"CC-{random.randint(1000, 9999)}",
                cosce_description=f"Centro de costos de {company.compa_name} relacionado a {fake.catch_phrase()}",
                cosce_budget=random.uniform(1000, 10000),
                cosce_active=True
            )
            # Registrar en EntityCatalog
            entity_catalog = EntityCatalog.objects.create(
                entit_name=cost_center.cosce_name,
                entit_descrip=cost_center.cosce_description,
                company=company
            )
            entity_catalogs.append(entity_catalog)

    print(f"Registros en EntityCatalog: {len(entity_catalogs)}")

    # Crear Permisos
    print("Creando Permisos...")
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

    # Crear Usuarios y Relaciones Usuario-Compañía
    print("Creando Usuarios y Relaciones Usuario-Compañía...")
    user_companies = []

    for i in range(10):
        user = User.objects.create_user(
            user_username=fake.user_name()[:20],
            user_email=fake.unique.email(),
            password="password123",
            user_phone=fake.phone_number()[:20],
            user_is_admin=random.choice([True, False]),
            user_is_active=True
        )
        company = random.choice(companies)
        user_company = UserCompany.objects.create(
            user=user,
            company=company,
            useco_active=True
        )
        user_companies.append(user_company)

    # Crear Roles
    print("Creando Roles...")
    roles = []
    for company in companies:
        role = Role.objects.create(
            role_name=f"Rol {fake.job()}",
            company=company,
            role_description=fake.text(max_nb_chars=50),
            role_active=True
        )
        roles.append(role)

        # Asignar Permisos a Roles
        for permission in permissions:
            PermiRole.objects.create(
                role=role,
                permission=permission,
                entitycatalog=random.choice(entity_catalogs),
                perol_include=True
            )

    # Asignar Permisos a Roles en Registros Específicos
    print("Creando PermiRoleRecord...")
    for role in roles:
        for entity in entity_catalogs:
            for record_id in range(1, 3):  # Crear 2 registros específicos
                permission = random.choice(permissions)
                PermiRoleRecord.objects.create(
                    role=role,
                    permission=permission,
                    entitycatalog=entity,
                    perrc_record=record_id,
                    perrc_include=True
                )

    # Asignar Permisos a Usuarios
    print("Creando PermiUser...")
    for user_company in user_companies:
        for permission in permissions:
            PermiUser.objects.create(
                usercompany=user_company,
                permission=permission,
                entitycatalog=random.choice(entity_catalogs),
                peusr_include=True
            )

    # Asignar Permisos a Usuarios en Registros Específicos
    print("Creando PermiUserRecord...")
    for user_company in user_companies:
        for entity in entity_catalogs:
            for record_id in range(1, 3):  # Crear 2 registros específicos
                permission = random.choice(permissions)
                PermiUserRecord.objects.create(
                    usercompany=user_company,
                    permission=permission,
                    entitycatalog=entity,
                    peusr_record=record_id,
                    peusr_include=True
                )

    print("Datos de prueba creados con éxito.")


if __name__ == '__main__':
    generate_data()
