import pandas as pd

class YoutubeToMp3:

    def __init__(self):
        pass

    def load_data(self):
        df = pd.read_csv(r'C:\Users\hassaans studybook\Downloads\_E__Repositories_CloudFlow_data_HolyQuraan_data_1404252128_.csv',
                          sep=';',
                          )
        # df = pd.read_csv(r'C:\Users\hassaans studybook\Downloads\test.csv', sep=';')
        print(df.shape)

if __name__=='__main__':
    YoutubeToMp3().load_data()