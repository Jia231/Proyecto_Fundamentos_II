NOMBRE_DE_USUARIO = "python"
PASS = "python123"

def validar_usuario(usuario, contrasena):
    """
        Esta funcion valida el usuario y contasena digitado por el administrador 
         Args:
            usuario (str): Usuario del administrador
            contrasena (str): Contrasena del administrador

        Returns:
            bool: Si el usuario esta autenticado
    """  
    if usuario != NOMBRE_DE_USUARIO or contrasena != PASS:
        return False
    
    return True