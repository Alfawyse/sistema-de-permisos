# Prueba Técnica: Sistema de Permisos

### Requisitos Técnicos Obligatorios:
- **Base de Datos:** PostgreSQL
- **Backend:** Django Rest Framework
- **Frontend:** React.js

### Objetivo
El objetivo de esta prueba técnica es desarrollar un sistema de permisos que permita asignar privilegios a usuarios, ya sea por entidad o por registro individual. Este sistema gestionará los permisos de manera flexible, asociándolos tanto a roles como a usuarios específicos.

### Modelos Implementados
Para lograr esta funcionalidad, se han creado los siguientes modelos:

- **PermiUser:** Gestiona los permisos asignados a un usuario.
- **PermiRole:** Gestiona los permisos asignados a un rol.
- **PermiUserRecord:** Asigna permisos a un usuario sobre registros específicos.
- **PermiRoleRecord:** Asigna permisos a un rol sobre registros específicos.
- **Permission:** Define la combinatoria de permisos que pueden ser otorgados a usuarios o roles.

### Funcionalidad del Sistema de Permisos
El sistema permite asignar permisos tanto a nivel de entidad como a nivel de registro individual dentro de una entidad. Esto proporciona una mayor granularidad en el control de acceso, ya que se pueden combinar distintos permisos según las necesidades del usuario o del rol.

### Entidades Para Pruebas
En la aplicación ERP de ejemplo, se gestionan dos entidades principales:

- **Sucursal (Branch Office):** Representa una oficina de la empresa.
- **Centro de Costos (Cost Center):** Representa una unidad dentro de la empresa a la que se le asignan costos.

Cada una de estas entidades puede tener permisos específicos asociados, tanto a nivel de entidad como a nivel de registros individuales dentro de ellas.

### Entregables

1. **Frontend Dinámico:**
   - Desarrollo de un frontend en React.js que muestre diferentes entidades (Branch Office y Cost Center) o registros dentro de estas entidades, dependiendo de los permisos del usuario autenticado. 
   - El sistema debe asegurarse de que los usuarios solo puedan ver las entidades o registros a los que tengan acceso, según sus permisos asignados.

2. **CRUD de Permisos en el Frontend:**
   - Implementación de un sistema de gestión de permisos desde el frontend para realizar las operaciones **CRUD** (Crear, Leer, Actualizar, Eliminar) sobre los siguientes modelos:
     - **PermiUser**
     - **PermiRole**
     - **PermiUserRecord**
     - **PermiRoleRecord**
   - A través de una interfaz intuitiva, los administradores podrán asignar y gestionar los permisos de usuarios y roles, así como especificar permisos a nivel de registro.

### Consideraciones Técnicas

- **Implementación en Django:**
   - Toda la lógica de permisos puede ser implementada en el backend utilizando Django. 
   - **Puntos extra:** Si alguna parte de la lógica del sistema, especialmente la relacionada con la gestión de permisos y la consulta de entidades/registros, se implementa utilizando funciones y procedimientos almacenados de **PostgreSQL**, se considerará un valor añadido.

### Formato de Entrega

- **Repositorio GitHub:** 
   - El entregable debe ser un enlace a uno o varios repositorios de GitHub que contengan el código del backend (Django) y del frontend (React.js).
  
- **Video de Demostración:** 
   - Junto con el enlace al repositorio, se debe entregar un video que muestre el sistema en funcionamiento. El video debe incluir:
     - La demostración del frontend mostrando las entidades o registros visibles para diferentes usuarios según sus permisos.
     - La funcionalidad completa del sistema **CRUD** de permisos en el frontend.
     - Ejemplos de la lógica de permisos, tanto a nivel de entidad como de registro individual.
