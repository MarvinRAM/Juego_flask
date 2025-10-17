from flask import Flask, request, render_template_string, session, jsonify, redirect, url_for
import os
import random

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "cambia-esta-clave")

# -----------------------------
# Utilidades de estado (por sesión)
# -----------------------------

def ensure_session_state():
    session.setdefault("points", 0)
    session.setdefault("tries", 0)
    session.setdefault("secret", random.randint(1, 100))
    session.setdefault("game_over", False)


def new_secret():
    session["secret"] = random.randint(1, 100)
