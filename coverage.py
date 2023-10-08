from zeep import Client

class Coverage:

    def __init__(self):
        self.key = '3211682680'

    def init_service(self, wsdl_url:str):
        self.cliente = Client(wsdl_url)

    def get_api_key(self, username:str, password:str): 

        if self.key == '3211682680':
            response = self.cliente.service.LoginOrRefreshUserToken(
                userTokenKeyToRefresh= self.key,
                loginName = username,
                password = password
            )

            self.key = response.userToken.Key
            return self.key
        
        return self.key
        
    
    def get_ca(self, distance:int, latitude:int, longitude:int, key:int):

        request_data = {
            'Distance' : distance,
            'Latitude' : latitude,
            'Longitude' : longitude
        }
        
        header = self.cliente.get_element("{http://suntech.pl/technology/v1}Context")
        context = header(UserTokenKey=key)
        self.cliente.set_default_soapheaders([context])

        response = self.cliente.service.GetNearestCA(request_data)

        return {'CA' : response.body.ResponseData.CA}
    
    def get_coverage(self, ca:int):

        response = self.cliente.service.GetServiceFlagsForCA(ca)
        coverage_data = response.body.ResponseData
        
        return coverage_data


if __name__ == '__main__':
    
    coverage = Coverage()

    coverage.init_service("https://qa-appserver.sunvizion.izzi.mx/Users.AuthenticationWebService/AuthenticationWebService.asmx?wsdl")
    key = coverage.get_api_key("cyber_ideas", "Cy6ER!|>3@s23")
    coverage.init_service("https://qa-appserver.sunvizion.izzi.mx/Integration.IZZIWebServices/V1/ResourceOperation.svc?wsdl")
    ca = coverage.get_ca(100, 19.4793065776055, -99.1786767018442, key)
    coverage = coverage.get_coverage(ca)
    print(coverage)