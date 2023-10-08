from coverage import Coverage
from location import Location

def login(coverage:Coverage):
    coverage.init_service('https://qa-appserver.sunvizion.izzi.mx/Users.AuthenticationWebService/AuthenticationWebService.asmx?wsdl')
    key = coverage.get_api_key("cyber_ideas", "Cy6ER!|>3@s23")
    
    return key

def get_all_coverage(coverage:Coverage, key:int, list_coordinates:list):
    coverage.init_service('https://qa-appserver.sunvizion.izzi.mx/Integration.IZZIWebServices/V1/ResourceOperation.svc?wsdl')
    list_coverage = []
    for coordinates in list_coordinates:
        ca = coverage.get_ca(10, coordinates[0], coordinates[1], key)
        response_coverage = coverage.get_coverage(ca)

        list_coverage.append(response_coverage)

    return list_coverage

if __name__ == '__main__':

    coverage = Coverage()
    key = login(coverage)
    list_coordinates = [(28.7488779, -106.1258333), (28.7488779, -106.1258333)]
    list_coverage = get_all_coverage(coverage, key, list_coordinates)

    print(list_coverage)