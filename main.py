#Variables globales
wnif = ""
#Funciones
def run(nif: str) -> str:
    # TODO
    global wnif
    wnif = nif
    
    #Variables locales
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"

    wnif = letras[nif % 23]
    print(f"Tu NIF es: {nif}{wnif}")
    return wnif 
#Codigo Principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    