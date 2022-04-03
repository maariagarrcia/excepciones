# Reglas de la sintaxis de una eMail ................ https://help.returnpath.com/hc/en-us/articles/220560587-What-are-the-rules-for-email-address-syntax-
# Como validar un email con expresiones regulares ... https://parzibyte.me/blog/2018/12/04/comprobar-correo-electronico-python/

### I M P O R T S
import re

# Valida si un cadena contiene un eMail válido
# 
def eMailTest(cadena):
    # La expresión la he copiado de la página arriba indicada -> No entiendo muy bien las expresiones regulares  :-0)
    # Pero le he hecho un apaño para que admita mayusculas en nombre y dominio sino solo funcionaba con minusculas!!!!!!!
    expresion_regular = r"(?:[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[A-Za-z0-9-]*[A-Za-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, cadena) is not None

def eMailInput(descripcion):
    while (True):
        # Lee una cadena por la consola
        inputUsuario = input('· ' + descripcion + '? ')

        if (inputUsuario == ''):
            # Permite finalizar para poder salir del programa si introducir un email válido
            return None, None

        elif (eMailTest(inputUsuario)):
            # eMail válido
            return True, inputUsuario

        else:
            # eMail incorrecto
            return False, inputUsuario

