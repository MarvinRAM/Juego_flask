from flask import Flask, request, render_template_string, session, jsonify, redirect, url_for
import os
import random

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "cambia-esta-clave")

# -----------------------------
# Utilidades de estado (por sesión)
# -----------------------------

# Función 1: Asegura que las variables de sesión estén inicializadas (puntos, intentos, número secreto, estado del juego)
# Autor: Marvin Rafael
def ensure_session_state():
    session.setdefault("points", 0)
    session.setdefault("tries", 0)
    session.setdefault("secret", random.randint(1, 100))
    session.setdefault("game_over", False)

# Función 2: Genera un nuevo número secreto aleatorio entre 1 y 100
# Autor: Leandro Demian
def new_secret():
    session["secret"] = random.randint(1, 100)