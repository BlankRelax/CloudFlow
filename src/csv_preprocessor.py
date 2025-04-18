import json

class CsvPreprocessor:

    def __init__(self, filepath:str):
        self.fp=filepath
        self.token_sep='<*>'
    
    def process(self):

        with open(self.fp, 'r+',encoding='utf-8') as f:
            self.raw_txt=f.readlines()[0]
        headers = self.raw_txt.split(self.token_sep)[0]
        content = self.raw_txt.split(self.token_sep)[1:]

        clean_fp=''.join(self.fp.split('.')[:-1]+['.txt'])
        with open(f'{clean_fp}', 'w', encoding='utf-8') as nf:
            nf.write(f'{headers}\n')
            for line in content:
                print(line)
                nf.write(f'{line}\n')
        


    def meta_raw_txt(self):
        print(len(self.raw_txt))

cp=CsvPreprocessor(r"C:\Users\hassa\Downloads\_E__Repositories_CloudFlow_data_HolyQuraan_data_1804252159_.csv")
cp.process()
cp.meta_raw_txt()
