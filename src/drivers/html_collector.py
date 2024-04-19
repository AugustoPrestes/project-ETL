from bs4 import BeautifulSoup
from zipfile import ZipFile
from typing import List, Dict
from .interfaces.html_collector import HtmlCollectorInterface

class HtmlCollector(HtmlCollectorInterface):
    def collect_essential_information(self, html: str) -> List[Dict[str, str]]:
        # Instanciando o bs4
        soup = BeautifulSoup(html, 'html.parser')

        # Armazenando os arquivos .zip
        file_ziped = soup.find_all('a')

        # Iterando sobre os arquivos .zip
        dfp_list = []
        for file in file_ziped:
            
            file_name = file.contents[0] # Pegando o nome do arquivo
            link = file.get('href')      # Pegando o link do arquivo 
            
            if '.zip' in link:      # Salvando apenas os arquivos .zip
                dfp_list.append({
                    "file": file_name,  # Salvando o nome do arquivo 
                    "link": link        # Salvando o complemento do arquivo 
                })
 

        return dfp_list