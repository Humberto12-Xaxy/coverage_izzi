from coverage import Coverage
from location import Location
from read_file import Data

def login(coverage:Coverage):
    coverage.init_service('https://qa-appserver.sunvizion.izzi.mx/Users.AuthenticationWebService/AuthenticationWebService.asmx?wsdl')
    key = coverage.get_api_key("cyber_ideas", "Cy6ER!|>3@s23")
    
    return key

def get_all_coverage(coverage:Coverage, key:int, list_coordinates:list):

    coverage.init_service('https://qa-appserver.sunvizion.izzi.mx/Integration.IZZIWebServices/V1/ResourceOperation.svc?wsdl')

    for index, coordinates in enumerate(list_coordinates):
        try:
            coordinates = coordinates.split(',')
            if coordinates[0] != 'error':
                ca = coverage.get_ca(10, float(coordinates[0]), float(coordinates[1]), key)
                if ca['CA'] != None:
                    response_coverage = coverage.get_coverage(ca)
                    
                    print(index ,f'AXTEL: {response_coverage["AXTEL"]} CA: {response_coverage["CA"]} DNS: {response_coverage["DNS"]} DOCSIS: {response_coverage["DOCSIS"]} FTTH: {response_coverage["FTTH"]} GPON: {response_coverage["GPON"]} HFC: {response_coverage["HFC"]} ORZ: {response_coverage["ORZ"]}')
                    data.save_cobertura(f'AXTEL: {response_coverage["AXTEL"]} CA: {response_coverage["CA"]} DNS: {response_coverage["DNS"]} DOCSIS: {response_coverage["DOCSIS"]} FTTH: {response_coverage["FTTH"]} GPON: {response_coverage["GPON"]} HFC: {response_coverage["HFC"]} ORZ: {response_coverage["ORZ"]}', index)
                    # list_coverage.append(f'AXTEL: {response_coverage["AXTEL"]}, CA: {response_coverage["CA"]}, DNS: {response_coverage["DNS"]}, DOCSIS: {response_coverage["DOCSIS"]}, FTTH: {response_coverage["FTTH"]}, GPON: {response_coverage["GPON"]}, HFC: {response_coverage["HFC"]}, ORZ: {response_coverage["ORZ"]}')
                else:
                    print(index, 'No hay cobertura')
                    data.save_cobertura('No hay cobertura', index)
                    # list_coverage.append('No hay cobertura')
            else:
                print(index, 'No se encontró la ubicación')
                data.save_cobertura('No se encontró la ubicación', index)
        except Exception as e:
            print(f'Error: {e}')
            data.save_cobertura(f'Error: {e}', index)


if __name__ == '__main__':

    coverage = Coverage()
    location = Location()
    data = Data()

    list_coordinates = data.get_coordinates()

    key = login(coverage)
    print(key)
    get_all_coverage(coverage, key, list_coordinates)