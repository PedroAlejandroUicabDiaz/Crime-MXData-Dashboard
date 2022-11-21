import pandas as pd
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn.metrics import classification_report

class pd_logistic_rg:
    def __init__(self, df:'pd.DataFrame', group:str, drop:list[str], evaluator:str, featured_cols:list[str]) -> 'pd.DataFrame':
        new_df = df.groupby(group).sum()
        new_df = new_df.reset_index()
        new_df.drop(drop, axis=1, inplace=True)
        new_df[evaluator] = new_df.sum(axis=1)
        self.sum_cont = new_df[evaluator]
        self.min = new_df[evaluator].min()
        self.max = new_df[evaluator].max()
        
        self.group = group
        self.drop = drop
        self.evaluator = evaluator
        self.feature_cols = featured_cols
        self.df = new_df

    def fit_model(self, ):
        X = self.df[self.feature_cols] # Features
        y = self.df.tag_crime # Target variable

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=1)

        # Create Decision Tree classifer object
        self.clf:'DecisionTreeClassifier' = DecisionTreeClassifier()

        # Train Decision Tree Classifer
        self.clf = self.clf.fit(X_train,y_train)

        #Predict the response for test dataset
        y_pred = self.clf.predict(X_test)

        self.report = classification_report(y_test, y_pred)
    
    def predict_data(self, data:list[list[float|int]]) -> str:
        return None


class logistic_cdmx(pd_logistic_rg):
    def __init__(self, df:'pd.DataFrame', group:str, drop:list[str], evaluator:str, target:str, classes:dict[int, str], featured_cols:list[str]):
        super().__init__(df=df, group=group, drop=drop, evaluator=evaluator, featured_cols=featured_cols)

        self.df[target] = self.df[evaluator].apply(self.__crime_class)
        self.classes = classes

        self.fit_model()
    
    def predict_data(self, data:list[list[float|int]]) -> str:
        prediction = self.clf.predict(data)
        return self.classes[prediction[0]]
    
    def __crime_class(y, x):
        if x <= 2300:
            return 1
        elif x >2300 and x<3800:
            return 2
        else:
            return 3
