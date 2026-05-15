import requests
from config import SUPABASE_URL, HEADERS

def guardar_contrasena(nombre_usuario, app, contrasena):
    if not app and not contrasena:
        return False
    res = requests.post(
        f"{SUPABASE_URL}/rest/v1/contrasenas",
        headers=HEADERS,
        json={"nombre_usuario": nombre_usuario, "usuario": app, "contrasena": contrasena}
    )
    return res.status_code == 201

def mostrar_contrasenas(nombre_usuario):
    res = requests.get(
        f"{SUPABASE_URL}/rest/v1/contrasenas",
        headers=HEADERS,
        params={"nombre_usuario": f"eq.{nombre_usuario}", "select": "*"}
    )
    return res.json()

def editar_contrasena(nombre_usuario, id_contrasena, nueva_contrasena):
    res = requests.patch(
        f"{SUPABASE_URL}/rest/v1/contrasenas",
        headers=HEADERS,
        params={"id": f"eq.{id_contrasena}", "nombre_usuario": f"eq.{nombre_usuario}"},
        json={"contrasena": nueva_contrasena}
    )
    return res.status_code == 204

def eliminar_contrasena(nombre_usuario, id_contrasena):
    res = requests.delete(
        f"{SUPABASE_URL}/rest/v1/contrasenas",
        headers=HEADERS,
        params={"id": f"eq.{id_contrasena}", "nombre_usuario": f"eq.{nombre_usuario}"}
    )
    return res.status_code == 204

def eliminar_todas_contrasenas(nombre_usuario):
    res = requests.delete(
        f"{SUPABASE_URL}/rest/v1/contrasenas",
        headers={**HEADERS, "Prefer": "return=minimal"},
        params={"nombre_usuario": f"eq.{nombre_usuario}"}
    )
    return res.status_code == 204
