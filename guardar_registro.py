import bcrypt
import requests
from config import SUPABASE_URL, HEADERS


def registro_usuario(nombre_usuario, clave):

    res = requests.get(
        f"{SUPABASE_URL}/rest/v1/usuarios",
        headers={**HEADERS, "Accept": "application/json"},
        params={"nombre_usuario": f"eq.{nombre_usuario}", "select": "*"}
    )
    datos = res.json()
    if isinstance(datos, list) and len(datos) > 0:
        print("ERROR: Ese nombre de usuario ya existe.")
        return False

    clave_hash = bcrypt.hashpw(clave.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    res = requests.post(
        f"{SUPABASE_URL}/rest/v1/usuarios",
        headers={**HEADERS, "Accept": "application/json"},
        json={"nombre_usuario": nombre_usuario, "clave": clave_hash}
    )

    if res.status_code == 201:
        print("Registro completado con éxito.")
        return True
    else:
        print(f"Error al registrar: {res.text}")
        return False
