import json

class CsvPreprocessor:

    def __init__(self, filepath:str):
        self.fp=filepath
        self.token_sep='*<>*'
    
    def process(self):

        with open(self.fp, 'r+',encoding='utf-8') as f:
            self.raw_txt=f.readlines()[0]
        headers = self.raw_txt.split(self.token_sep)[0]
        content = self.raw_txt.split(self.token_sep)[1:]

        with open(f'{self.fp}', 'w') as nf:
            for line in content[:3]:
                print(line)
                nf.write(f'{line}\n')
        
        print(f'{content[0]}\n{content[1]}')


    def meta_raw_txt(self):
        print(len(self.raw_txt))

cp=CsvPreprocessor(r'C:\Users\hassaans studybook\Downloads\_E__Repositories_CloudFlow_data_HolyQuraan_data_1404252127_.csv')
cp.process()
cp.meta_raw_txt()
