import pandas as pd
from libs.df_article import Article
from utils.files import csv_names
from ml_models.model import logistic_cdmx

rules_models:dict[str, dict[str | int,str] | None | list[str]] = {
    'MX-DATA-UPDATED':{
        'group': 'MUNICIPIO',
        'drop': ['LATITUDE', 'LONGITUDE'],
        'evaluator': 'total_crimes',
        'target':'tag_crime',
        'classes': {1:'safe',2:'Medium', 3: 'Danger'},
        'featured_cols':['HOMICIDIO DOLOSO', 'LESIONES POR ARMA DE FUEGO', 'ROBO A BORDO DE METRO C.V.', 'ROBO A BORDO DE MICROBUS C.V.','ROBO A BORDO DE MICROBUS S.V.','ROBO A BORDO DE TAXI C.V.',
                'ROBO A CASA HABITACION C.V.', 'ROBO A CUENTAHABIENTE C.V.', 'ROBO A NEGOCIO C.V.', 'ROBO A REPARTIDOR C.V.', 'ROBO A REPARTIDOR S.V.',
                'ROBO A TRANSEUNTE C.V.', 'ROBO A TRANSPORTISTA C.V.', 'ROBO A TRANSPORTISTA S.V.', 'ROBO DE VEHICULO AUTOMOTOR C.V.', 'ROBO DE VEHICULO AUTOMOTOR S.V.',
                'SECUESTRO', 'VIOLACION'],
    }, 
    'MX_CRIME_DATA_INEGI_P1':None
}

class FdfArticles:
    def __init__(self, path:str='./data/'):
        self.path = path
        names, files_names = csv_names(self.path)
        # print(names, files_names)

        self.names:str = names
        self.files_names:str = files_names

        self.articles:dict[str, Article] = self.__read_articles()
        self.__train_models()
    
    def __train_models(self, ) -> None:
        for article in self.articles:
            art = self.articles[article]
            if rules_models[article] != None:
                rules = rules_models[article]
                rules['df'] = art.df
                art.model = logistic_cdmx(**rules)
    
    def __read_articles(self, ) -> dict[str, Article]:
        articles = {self.names[i]:Article(pd.read_csv(name)) for i, name in enumerate(self.files_names)}

        return articles


if __name__ == '__main__':
    FdfArticles()
