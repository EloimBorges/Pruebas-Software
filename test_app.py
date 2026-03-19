from app import autenticar_usuario
import time

def test_cp01_login_exitoso():
    r = autenticar_usuario("admin", "1234")
    assert r["success"] == True
    assert r["message"] == "Acceso concedido"

def test_cp02_usuario_vacio():
    r = autenticar_usuario("", "1234")
    assert r["success"] == False
    assert r["message"] == "Usuario y contraseña son requeridos"

def test_cp03_contrasena_vacia():
    r = autenticar_usuario("admin", "")
    assert r["success"] == False
    assert r["message"] == "Usuario y contraseña son requeridos"

def test_cp04_usuario_inexistente():
    r = autenticar_usuario("pedro", "1234")
    assert r["success"] == False
    assert r["message"] == "Usuario no existe"

def test_cp05_contrasena_incorrecta():
    r = autenticar_usuario("admin", "9999")
    assert r["success"] == False
    assert r["message"] == "Contraseña incorrecta"

def test_cp06_tiempo():
    r = autenticar_usuario("admin", "1234")
    assert r["response_time_ms"] > 0

def test_cp07_estructura():
    r = autenticar_usuario("admin", "1234")
    assert "success" in r
    assert "message" in r
    assert "response_time_ms" in r

def test_tiempo_real():
    inicio = time.perf_counter()
    r = autenticar_usuario("admin", "1234")
    fin = time.perf_counter()

    tiempo_ms = (fin - inicio) * 1000

    assert r["success"] == True
    assert tiempo_ms < 500

def test_tiempo_sistema():
    r = autenticar_usuario("admin", "1234")
    assert r["response_time_ms"] < 500


    # -----------Pruebas Exploratorias-------------------

def test_exploratoria_usuario_con_espacios():
    r = autenticar_usuario(" admin ", "1234")
    assert r["success"] == False

def test_exploratoria_usuario_en_mayusculas():
    r = autenticar_usuario("ADMIN", "1234")
    assert r["success"] == False

def test_exploratoria_caracteres_especiales():
    r = autenticar_usuario("admin!", "1234")
    assert r["success"] == False

def test_exploratoria_ambos_campos_vacios():
    r = autenticar_usuario("", "")
    assert r["success"] == False
    assert r["message"] == "Usuario y contraseña son requeridos"

def test_exploratoria_password_con_espacios():
    r = autenticar_usuario("admin", " 1234 ")
    assert r["success"] == False