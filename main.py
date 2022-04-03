### I M P O R T S
from helpers import *
from menu_class import *
from input_email import *

#
#   F U N C I O N E S
#
def test_email():
      while True:
            email = eMailInput("Dime un eMail (<Intro> para finalizar)")
            if email[0] == None:
                  break

            if email[0]:
                  mostrar_resultado("Email Valido", email[1])
            else:
                  mostrar_resultado("*** Email INVALIDO ***", email[1])
            
            print()


#
#   I N I C I O    P R O G R A M A
#
helpers.clear()  # Limpia la terminal

mi_menu.addOption("Validar email con expresiones regulares", test_email)

mi_menu.start()