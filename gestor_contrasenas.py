import requests
from config import SUPABASE_URL, HEADERS


def guardar_contrasena(usuario, contrasena):
    if not usuario and not contrasena:
        return False

    res = requests.post(
        f"{SUPABASE_URL}/rest/v1/contrasenas",
        headers=HEADERS,
        json={"usuario": usuario, "contrasena": contrasena}
    )
    return res.status_code == 201


def mostrar_contrasenas():
    res = requests.get(
        f"{SUPABASE_URL}/rest/v1/contrasenas",
        headers=HEADERS
    )
    return res.json()


def editar_contrasena(id_contrasena, nueva_contrasena):
    res = requests.patch(
        f"{SUPABASE_URL}/rest/v1/contrasenas",
        headers=HEADERS,
        params={"id": f"eq.{id_contrasena}"},
        json={"contrasena": nueva_contrasena}
    )
    return res.status_code == 204


def eliminar_contrasena(id_contrasena):
    res = requests.delete(
        f"{SUPABASE_URL}/rest/v1/contrasenas",
        headers=HEADERS,
        params={"id": f"eq.{id_contrasena}"}
    )
    return res.status_code == 204


def eliminar_todas_contrasenas():
    res = requests.delete(
        f"{SUPABASE_URL}/rest/v1/contrasenas",
        headers={**HEADERS, "Prefer": "return=minimal"},
        params={"id": "gte.0"}
    )
    return res.status_code == 204
