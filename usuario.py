NOMBRE_DE_USUARIO = "python"
PASS = "python123"

def validar_usuario(usuario, contrasena):
    if usuario != NOMBRE_DE_USUARIO or contrasena != PASS:
        return False
    
    return True