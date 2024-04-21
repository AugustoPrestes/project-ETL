from numpy import full
from src.stages.contracts.extract_contract import ExtractContract

import os
import wget
import tempfile
from datetime import datetime
import pandas as pd
from zipfile import ZipFile
from typing import List, Dict


class TransformRawData:
    
    def transform(self,  extract_contract: ExtractContract):
        self.__transform_raw_data(extract_contract)

    def __transform_raw_data(self, extract_contract: ExtractContract) -> List[Dict]:
        extraction_content = extract_contract.transent_information_content
        extraction_date = extract_contract.extraction_date
        
        transformed_data = []
        
        
        for data in extraction_content: # Iterando sobre cada valor dentro da extração
            
            transformed_data = None     # Lista que recebera os dados baixados

            link = data['link_file']    # Coletando o caminho para o downloado do arquivo
            full_name = data['name_file'].split('.')    # Coletando o nome do arquivo separando pelo ponto

            name = full_name[0]         # Pegando apenas o nome sem a extenção (.zip)
            
            os.makedirs(f'/workspaces/project-ETL/src/data/bronze/{name}', exist_ok=True)
            print(f"\nNome do arquivo: {name}\nCaminho para o download: {link}")

            transformed_data = self.__download_raw_data(name, link)
            transformed_data['extraction_date'] = extraction_date

            print()
            print(transformed_data)

    def __download_raw_data(self, name: str, link: str)-> Dict: # Retorna o ano, o nome e a quantidade de arquivos
        
        list_tables = []


        with tempfile.TemporaryDirectory(dir='/workspaces/project-ETL/src/data', prefix='temp_',suffix=f'_{name}', ) as tempdir:
            # Baixando o ziped
            wget.download(link, out=tempdir)
            # print("Baixei")
            
            # Abrindo zipe file dentro do temp_dir
            with ZipFile(f"{tempdir}/{name}.zip", 'r') as zip_file:
                # print("Abri o zip")
                # Extraindo todos os arquivos para a temp_dir    
                zip_file.extractall(path=tempdir)
                # print("Extrai tudo do zip")

                # Tratando de cada arquivo
                for f in os.listdir(tempdir):
                    # print("Loop dos arquivos temporarios (.csv)")
                    full_name = f.split('.')
                    f = full_name[0]
                    self.__transform_layer_bronze(file=f, path=tempdir, name=name) # Salvando os arquivos em .parquet na camada bronze
            
                # Retornando os meta dados de cada arquivos
                return {
                    "dir_name": name,
                    "dir_path": f'/workspaces/project-ETL/src/data/bronze/' + name,
                    "list_files": os.listdir(tempdir),
                    "link_origin": link,
                    "transform_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
    def __transform_layer_bronze(self, file, path: str, name: str) -> None:
        """
        file: Nome do arquivo que será transacionado,
        path: Caminho no qual o arquivo se encontra atualmente (temp_dir),
        name: Nome da pasta do ano, utilizada para salvar o .parquet
        """
        # print("função layer_bronze")
        df = pd.read_csv(f"{path}/{file}.csv", sep=';', encoding='latin-1')
        # print("Carreguei o arquivo .csv")

        # print("Criei a pasta da camada bronze ")

        df.to_parquet(f'/workspaces/project-ETL/src/data/bronze/{name}/{file}.parquet')
        
                
