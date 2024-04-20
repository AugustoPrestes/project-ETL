from bs4 import BeautifulSoup
from typing import List, Dict
from .interfaces.html_collector import HtmlCollectorInterface

class HtmlCollector(HtmlCollectorInterface):

    
    def collect_essential_information(self, html: str) -> List[Dict[str, str]]:
        # Instanciando o bs4
        soup = BeautifulSoup(html, 'html.parser')

        # Localizando todos os links da pagina
        file_list = soup.findAll('a')

        dfp_list = []
        for f in file_list:
            if '.zip' in f.get('href'):
                name_file = f.contents[0]   # Nome do arquivo
                link_file = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/" + f.get('href')  # Caminho do arquivo

                # Adicionando o nome do arquivo e seu caminho na web
                dfp_list.append({
                    "name_file": name_file,
                    "link_file": link_file
                })
        
        return dfp_list

