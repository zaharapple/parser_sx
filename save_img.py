import numpy as np
import pandas as pd
from io import BytesIO
from PIL import Image
import requests


class GetPhoto:

    def __init__(self, path):
        self.path = path
        self.df = pd.read_excel(source, sheet_name='TDSheet').replace(
            {np.nan: None})
        self.PATH = '/home/romanz/learning/parcer_for_sx/tmp/imgs'

    def get_images(self, item):

        my_list = []
        for value in self.df['Фото'][item].split():
            if value[-1] == ';':
                my_list.append(value[:-1])
            else:
                my_list.append(value)
        return my_list

    def open_img(self):

        rows = self.df.count()['Артикул']
        count = 0
        err = 0
        for item in range(0, rows):
            urls = self.get_images(item)
            for url in urls:
                response = requests.get(url)
                img = Image.open(BytesIO(response.content))
                path = self.PATH + '/' + response.url.split("/")[-1]
                try:
                    img.save(path)
                    img.close()
                except OSError as e:
                    err += 1
                    print(f'{err} :error {e}')
                    print(f"don't download: {url} ")
                    continue
                count += 1

        print(count)

source = r'~/learning/parcer_for_sx/tmp/import.xls'

a = GetPhoto(source).open_img()
