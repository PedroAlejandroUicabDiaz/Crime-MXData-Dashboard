import os


def csv_names(path:str):
    files = os.listdir(path=path)
    files = [path+f for f in files if '.csv' in f]

    names = [f.replace('.csv', '').replace(path, '') for f in files]

    return names, files


if __name__ == '__main__':
    print(csv_names('./data/'))
    
