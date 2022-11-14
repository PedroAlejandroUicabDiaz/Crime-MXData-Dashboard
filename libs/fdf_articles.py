import pandas as pd
from libs.df_article import Article
from utils.files import csv_names

class FdfArticles:
    def __init__(self, path:str='./data/'):
        self.path = path
        names, files_names = csv_names(self.path)
        # print(names, files_names)

        self.names:str = names
        self.files_names:str = files_names

        self.articles:dict[str, Article] = self.__read_articles()

    
    def __read_articles(self, ) -> dict[str, Article]:
        articles = {self.names[i]:Article(pd.read_csv(name)) for i, name in enumerate(self.files_names)}

        return articles


if __name__ == '__main__':
    FdfArticles()
