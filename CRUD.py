import psycopg2
print("DANIELA LOPEZ, JUAN PARDO, DIEGO VARGAS")
# Función para conectar a la base de datos
def conectar():
    try:
        conn = psycopg2.connect(
            host="nubediego123-14028.7tt.aws-us-east-1.cockroachlabs.cloud",
            port="26257",
            user="vargastrigos_2003_gm",
            password="WbWcC1LHesRfKL7-duKYiA",
            database="hola"
        )
        return conn
    except psycopg2.Error as e:
        print("Ocurrió un error durante la conexión a la base de datos:", e)
        return None
    

# Operación Create
def crear_usuario(conn):
    try:
        documento = input("Ingrese el documento del usuario: ")
        nombre = input("Ingrese el nombre del usuario: ")
        apellido = input("Ingrese el apellido del usuario: ")

        cur = conn.cursor()
        cur.execute("INSERT INTO usuario (documento, nombre, apellido) VALUES (%s, %s, %s)", (documento, nombre, apellido))
        conn.commit()
        cur.close()
        print("Usuario creado exitosamente.")
    except psycopg2.Error as e:
        print("Error al crear usuario:", e)

# Operación Read
def obtener_usuarios(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM usuario")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
    except psycopg2.Error as e:
        print("Error al obtener usuarios:", e)

# Operación Update
def actualizar_usuario(conn):
    try:
        documento_viejo = input("Ingrese el documento del usuario que desea actualizar: ")
        documento_nuevo = input("Ingrese el nuevo documento: ")
        nombre = input("Ingrese el nuevo nombre: ")
        apellido = input("Ingrese el nuevo apellido: ")

        cur = conn.cursor()
        cur.execute("UPDATE usuario SET documento = %s, nombre = %s, apellido = %s WHERE documento = %s", (documento_nuevo, nombre, apellido, documento_viejo))
        conn.commit()
        cur.close()
        print("Usuario actualizado exitosamente.")
    except psycopg2.Error as e:
        print("Error al actualizar usuario:", e)

# Operación Delete
def eliminar_usuario(conn):
    try:
        documento = input("Ingrese el documento del usuario que desea eliminar: ")

        cur = conn.cursor()
        cur.execute("DELETE FROM usuario WHERE documento = %s", (documento,))
        conn.commit()
        cur.close()
        print("Usuario eliminado exitosamente.")
    except psycopg2.Error as e:
        print("Error al eliminar usuario:", e)

# Ejemplo de uso
conn = conectar()
if conn:
    while True:
        print("\n1. Crear usuario")
        print("2. Obtener usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        opcion = input("Ingrese el número de la operación que desea realizar: ")

        if opcion == "1":
            crear_usuario(conn)
        elif opcion == "2":
            obtener_usuarios(conn)
        elif opcion == "3":
            actualizar_usuario(conn)
        elif opcion == "4":
            eliminar_usuario(conn)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

    conn.close()
