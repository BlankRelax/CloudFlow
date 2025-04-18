import pandas as pd
from pytube import YouTube

class YoutubeToMp3:

    def __init__(self, fp:str):
        self.df:pd.DataFrame = ''
        self.fp=fp

    def _load_data(self):
        df = pd.read_csv(self.fp,
                          sep=';',
                          )
        self.df = df
        return True
    
    def _download_link(self, link):
        YouTube(link).streams.filter().first.download()
    
    def chain_exc(self):
        self._load_data()
        self._download_link(self.df['Link'][1])

if __name__=='__main__':
    transformer = YoutubeToMp3(r"C:\Users\hassa\Downloads\_E__Repositories_CloudFlow_data_HolyQuraan_data_1804252159_.txt")
    transformer.chain_exc()