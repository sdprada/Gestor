from flask import Flask, request, jsonify
from flask_cors import CORS
from guardar_registro import registro_usuario
from validar_login import verifica_login
from gestor_contrasenas import (
    guardar_contrasena,
    mostrar_contrasenas,
    editar_contrasena,
    eliminar_contrasena,
    eliminar_todas_contrasenas
)

app = Flask(__name__)
CORS(app)


# ── REGISTRO ──────────────────────────────────────────
@app.route("/registro", methods=["POST"])
def registro():
    datos = request.json
    nombre = datos.get("nombre_usuario")
    clave = datos.get("clave")

    if not nombre or not clave:
        return jsonify({"error": "Faltan campos"}), 400

    resultado = registro_usuario(nombre, clave)
    if resultado:
        return jsonify({"mensaje": "Registro exitoso"}), 201
    else:
        return jsonify({"error": "El usuario ya existe"}), 409


# ── LOGIN ─────────────────────────────────────────────
@app.route("/login", methods=["POST"])
def login():
    datos = request.json
    usuario = datos.get("nombre_usuario")
    clave = datos.get("clave")

    if not usuario or not clave:
        return jsonify({"error": "Faltan campos"}), 400

    resultado = verifica_login(usuario, clave)

    if resultado == "exito":
        return jsonify({"mensaje": "Login exitoso"}), 200
    elif resultado == "no_clave":
        return jsonify({"error": "Contraseña incorrecta"}), 401
    elif resultado == "no_usuario":
        return jsonify({"error": "Usuario no encontrado"}), 404


# ── CONTRASEÑAS ───────────────────────────────────────
@app.route("/contrasenas", methods=["GET"])
def listar():
    datos = mostrar_contrasenas()
    return jsonify(datos), 200


@app.route("/contrasenas", methods=["POST"])
def agregar():
    datos = request.json
    usuario = datos.get("usuario")
    contrasena = datos.get("contrasena")

    if not usuario or not contrasena:
        return jsonify({"error": "Faltan campos"}), 400

    guardar_contrasena(usuario, contrasena)
    return jsonify({"mensaje": "Guardado"}), 201


@app.route("/contrasenas/<int:id_c>", methods=["PATCH"])
def editar(id_c):
    datos = request.json
    nueva = datos.get("contrasena")

    if not nueva:
        return jsonify({"error": "Falta la nueva contraseña"}), 400

    editar_contrasena(id_c, nueva)
    return jsonify({"mensaje": "Actualizado"}), 200


@app.route("/contrasenas/<int:id_c>", methods=["DELETE"])
def eliminar(id_c):
    eliminar_contrasena(id_c)
    return jsonify({"mensaje": "Eliminado"}), 200


@app.route("/contrasenas", methods=["DELETE"])
def eliminar_todas():
    eliminar_todas_contrasenas()
    return jsonify({"mensaje": "Todas eliminadas"}), 200


# ── INICIO ────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)
