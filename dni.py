import requests
import json

print('\033[96m')
def mostrar_menu(opciones):
    print('Seleccione una opción:')
    print("")
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
	   
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
	  
    opciones = {
        
        '1': ('\033[96mTOKEN PREMIUM', accion1),
        '2': ('\033[96mTOKEN FREE', accion2),
        '3': ('\033[96mSALIR', salir)
    }

    generar_menu(opciones, '3')


def accion1():
    dni = input('\033[92mINGRESA EL DNI: \033[93m')
    token = input('\033[92mINGRESA TU TOKEN: \033[93m')

    response = requests.get("https://apiperu.dev/api/dni/" + dni + "?api_token=" + token)

    numero = response.json()['data']['numero']
    nombre_completo = response.json()['data']['nombre_completo']
    nombres = response.json()['data']['nombres']
    apellido_paterno = response.json()['data']['apellido_paterno']
    apellido_materno = response.json()['data']['apellido_materno']
    codigo_verificacion = response.json()['data']['codigo_verificacion']
    fecha_nacimiento = response.json()['data']['fecha_nacimiento']
    sexo = response.json()['data']['sexo']
    estado_civil = response.json()['data']['estado_civil']
    departamento = response.json()['data']['departamento']
    provincia = response.json()['data']['provincia']
    distrito = response.json()['data']['distrito']
    direccion = response.json()['data']['direccion']
    direccion_completa = response.json()['data']['direccion_completa']
    ubigeo_reniec = response.json()['data']['ubigeo_reniec']
    ubigeo_sunat = response.json()['data']['ubigeo_sunat']
    ubigeo = response.json()['data']['ubigeo']
    
    print("")
    print("\033[91mDNI: \033[94m" + numero)
    print("\033[91mNOMBRE COMPLETO: \033[94m" + nombre_completo)
    print("\033[91mNOMBRES: \033[94m" + nombres)
    print("\033[91mAPELLIDO PATERNO: \033[94m" + apellido_paterno)
    print("\033[91mAPELLI: \033[94m" + apellido_materno)
    print("\033[91mCODIGO VERIFICACION: \033[94m" + str(codigo_verificacion))
    print("\033[91mFECHA NACIMIENTO: \033[94m" + fecha_nacimiento)
    print("\033[91mSEXO: \033[94m" + sexo)
    print("\033[91mESTADO CIVIL: \033[94m" + estado_civil)
    print("\033[91mDEPARTAMENTO: \033[94m" + departamento)
    print("\033[91mPROVINCIA: \033[94m" + provincia)
    print("\033[91mDISTRITO: \033[94m" + distrito)
    print("\033[91mDIRECCION: \033[94m" + direccion)
    print("\033[91mDIRECCION COMPLETA: \033[94m" + direccion_completa)
    print("\033[91mUBIGEO RENIEC: \033[94m" + ubigeo_reniec)
    print("\033[91mUBIGEO SUNAT: \033[94m" + ubigeo_sunat)
    print("\033[91mUBIGEO: \033[94m" + str(ubigeo))
    print('\033[96m')    
 
def accion2():

   dni = input('\033[92mINGRESA EL DNI: \033[93m')
   token = input('\033[92mINGRESA TU TOKEN: \033[93m')

   response = requests.get("https://apiperu.dev/api/dni/" + dni + "?api_token=" + token)

   numero = response.json()['data']['numero']
   nombre_completo = response.json()['data']['nombre_completo']
   nombres = response.json()['data']['nombres']
   apellido_paterno = response.json()['data']['apellido_paterno']
   apellido_materno = response.json()['data']['apellido_materno']
   ubigeo_sunat = response.json()['data']['ubigeo_sunat']
   ubigeo = response.json()['data']['ubigeo']
   print("")
   print("\033[91mDNI: \033[94m" + numero)
   print("\033[91mNOMBRE COMPLETO: \033[94m" + nombre_completo)
   print("\033[91mNOMBRES: \033[94m" + nombres)
   print("\033[91mAPELLIDO PATERNO: \033[94m" + apellido_paterno)
   print("\033[91mAPELLIDO MATERNO: \033[94m" + apellido_materno)
   print('\033[96m')

def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()
