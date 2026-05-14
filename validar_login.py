import bcrypt
import requests
from config import SUPABASE_URL, HEADERS


def verifica_login(usuario, clave):
    res = requests.get(
        f"{SUPABASE_URL}/rest/v1/usuarios",
        headers={**HEADERS, "Accept": "application/json"},
        params={"nombre_usuario": f"eq.{usuario}", "select": "*"}
    )

    datos = res.json()

    if not isinstance(datos, list) or len(datos) == 0:
        return "no_usuario"

    clave_hash = datos[0]["clave"]

    if bcrypt.checkpw(clave.encode("utf-8"), clave_hash.encode("utf-8")):
        return "exito"
    else:
        return "no_clave"
