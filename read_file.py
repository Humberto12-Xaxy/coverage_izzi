import pandas as pd

class Data:

    def __init__(self) -> None:
        self.file = 'DF_Gis_Data_Manriquez.csv'
        self.df = pd.read_csv(self.file, encoding='utf-8', low_memory= False)
    
    get_address = lambda self: list(self.df['DirecconGis'])

    get_id = lambda self: list(self.df['id_registro'])

    get_coordinates = lambda self: list(self.df['Coordenadas'])

    def save_coordinates(self, latitude:float, longitude:float, index:int):

        coordinate_complete = f'{latitude}, {longitude}'
        self.df.loc[index, 'Coordenadas'] = f'{latitude}, {longitude}'
        
        self.df.to_csv(self.file, index= False)

        return coordinate_complete
    
    def save_cobertura(self, coverage:str, index:int):

        self.df_new.loc[index, 'Cobertura'] = coverage
        
        self.df_new.to_csv('coberturas_izzi.csv', index= False)

    def save_new_file(self, id, address, coordinates):

        data = {
            'id_register': id,
            'direccion' : address,
            'coordenadas' : coordinates
        }

        df = pd.DataFrame(data = data)

        df.to_csv('coberturas_izzi.csv', index=False)





if __name__ == '__main__':
    data = Data()

    print(data.get_id())

    data.save_new_file(data.get_id(), data.get_address(), data.get_coordinates())