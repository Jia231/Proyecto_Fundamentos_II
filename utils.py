def ingresar_valor(prompt, esTexto = True):
    while True:
        try:
            if esTexto:
                texto = input(prompt)
                if len(texto.strip()) == 0:
                    raise Exception()
                else: 
                    return texto 
            else:
                texto = float(input(prompt)) 
                return texto  
        except Exception:
            print("Ingrese un texto valido")
        except ValueError:      
            print("Ingrese un numero valido")