from django.db import connection

def obtener_permisos_usuario(user_id, entity_id):
    """
    Llama a la función almacenada de PostgreSQL 'get_user_permissions'.
    """
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM get_user_permissions(%s, %s);
        """, [user_id, entity_id])
        filas = cursor.fetchall()

    # Formatea los resultados como una lista de diccionarios
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
