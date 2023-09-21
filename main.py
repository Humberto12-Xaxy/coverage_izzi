from zeep import Client

wsdl_url = "https://qa-appserver.sunvizion.izzi.mx/Users.AuthenticationWebService/AuthenticationWebService.asmx?wsdl"

# Crea un cliente Zeep para el servicio SOAP
cliente = Client(wsdl_url)

# Define los parámetros de entrada para el método LoginOrRefreshUserToken
user_token_key_to_refresh = "3211682680"
login_name = "cyber_ideas"
password = "Cy6ER!|>3@s23"

# Llama al método LoginOrRefreshUserToken
respuesta = cliente.service.LoginOrRefreshUserToken(
    userTokenKeyToRefresh=user_token_key_to_refresh,
    loginName=login_name,
    password=password
)

# Extrae e imprime la información relevante de la respuesta
resultado_login = respuesta.loginResult.Result
llave_user_token = respuesta.userToken.Key
sesion = respuesta.userToken.Session

print(f"Resultado del inicio de sesión: {resultado_login}")
print(f"Llave del User Token: {llave_user_token}")
print(f"Sesión: {sesion}")


wsdl_url = "https://qa-appserver.sunvizion.izzi.mx/Integration.IZZIWebServices/V1/ResourceOperation.svc?wsdl"

# Crear un cliente Zeep para el servicio SOAP
cliente = Client(wsdl_url)

# Definir los parámetros de entrada
latitude = 19.4793065776055
longitude = -99.1786767018442
distance = 100
user_token_key = llave_user_token  # Tu token de usuario aquí


# Llame al método GetNearestCA

RequestData=dict(
    Distance=distance,
    Latitude=latitude,
    Longitude=longitude,
)


# Crear el encabezado con el token de usuario
header = cliente.get_element("{http://suntech.pl/technology/v1}Context")
context = header(UserTokenKey=user_token_key)

# Agregar el encabezado al cliente
cliente.set_default_soapheaders([context])

# Realizar la solicitud al servicio SOAP
response = cliente.service.GetNearestCA(RequestData)

# Extraer y mostrar el resultado
ca = response.body.ResponseData.CA
print(f"El CA más cercano es: {ca}")

CA = {
    'CA' : ca
}
response_coverage = cliente.service.GetServiceFlagsForCA(CA)

coverage_data = response_coverage.body.ResponseData

print(f'Los datos de covertura son: {coverage_data}')