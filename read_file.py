import pandas as pd

class Data:

    def __init__(self) -> None:
        self.file = 'DF_Gis_Data_Manriquez.csv'
        self.df = pd.read_csv(self.file, encoding='utf-8')
        self.df_new = pd.read_csv('coberturas_izzi.csv', encoding= 'utf-8')
    
    get_address = lambda self: list(self.df['DirecconGis'])

    get_id = lambda self: list(self.df['id_registro'])

    get_coordinates = lambda self: list(self.df['Coordenadas'])

    def save_coordinates(self, list_coordinates:list):

        for i in range(len(list_coordinates)):

            longitude, latitude = list_coordinates[i]

            self.df.loc[i, 'Coordenadas'] = f'{longitude}, {latitude}'
        
        self.df.to_csv(self.file, index= False)
    
    def save_cobertura(self, coverage:str, index:int):

        self.df_new.loc[index, 'Cobertura'] = coverage
        
        self.df_new.to_csv('coberturas_izzi.csv', index= False)

    def save_new_file(self, id, adress, coordinates):

        data = {
            'id_register': id,
            'direccion' : adress,
            'coordenadas' : coordinates
        }

        df = pd.DataFrame(data = data)

        df.to_csv('coberturas_izzi.csv', index=False)





if __name__ == '__main__':
    data = Data()

    # print(data.get_id())

    data.save_new_file(data.get_id(), data.get_address(), data.get_coordinates())