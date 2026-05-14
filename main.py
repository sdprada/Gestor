from guardar_registro import registro_usuario
from validar_login import verifica_login
from gestor_contrasenas import (
    guardar_contrasena,
    mostrar_contrasenas,
    editar_contrasena,
    eliminar_contrasena,
    eliminar_todas_contrasenas
)


def menu_registro():
    print("--- REGISTRO ---")
    nombre = input("Nombre de usuario: ").strip()
    clave = input("Contraseña: ").strip()
    registro_usuario(nombre, clave)


def menu_login():
    print("--- ACCESO ---")
    usuario = input("Nombre de usuario: ").strip()
    clave = input("Contraseña: ").strip()
    resultado = verifica_login(usuario, clave)

    if resultado == "exito":
        print("Login finalizado con éxito.")
        menu_principal()
    elif resultado == "no_clave":
        print("ERROR: Contraseña incorrecta.")
    elif resultado == "no_usuario":
        print("ERROR: Usuario no encontrado.")


def menu_principal():
    while True:
        print("--- MENÚ PRINCIPAL ---")
        print("1. Agregar nueva contraseña")
        print("2. Mostrar contraseñas guardadas")
        print("3. Editar una contraseña")
        print("4. Eliminar una contraseña")
        print("5. Eliminar todas las contraseñas")
        print("6. Salir")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            usuario = input("Usuario o aplicación: ").strip()
            contrasena = input("Contraseña: ").strip()
            guardar_contrasena(usuario, contrasena)

        elif opcion == "2":
            mostrar_contrasenas()

        elif opcion == "3":
            mostrar_contrasenas()
            id_c = input("\nID de la contraseña a editar: ").strip()
            nueva = input("Nueva contraseña: ").strip()
            editar_contrasena(id_c, nueva)

        elif opcion == "4":
            mostrar_contrasenas()
            id_c = input("\nID de la contraseña a eliminar: ").strip()
            eliminar_contrasena(id_c)

        elif opcion == "5":
            confirmar = input("¿Seguro que quieres eliminar todo? (s/n): ").strip().lower()
            if confirmar == "s":
                eliminar_todas_contrasenas()

        elif opcion == "6":
            break

        else:
            print("Opción no válida.")


def main():
    while True:
        print("\n=== GESTOR DE CONTRASEÑAS ===")
        print("1. Acceder")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Escoja su opción: ").strip()

        if opcion == "1":
            menu_login()
        elif opcion == "2":
            menu_registro()
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
