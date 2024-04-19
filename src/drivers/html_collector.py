import urllib3
from bs4 import BeautifulSoup
from typing import List, Dict
from .interfaces.html_collector import HtmlCollectorInterface

class HtmlCollector(HtmlCollectorInterface):
    def collect_essential_information(self, html: str) -> List[Dict[str, str]]:
        # Instanciando o bs4
        soup = BeautifulSoup(html, 'html.parser')
        url2 = 'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/'
        dfp_list = []
        urls = []
        names = []
        # Iterando sobre os arquivos .zip
        for i, file_link in enumerate(soup.find_all('a')):
            full_url = url2 + file_link.get('href')    # Pegando o caminho do arquivo 
            if full_url.endswith('.zip'):      # Salvando apenas os arquivos .zip 
                urls.append(full_url)
                names.append(soup.select('a')[i].attrs['href'])
                
        names_url = zip(names, urls)

        for name, url in names_url:
            print(url)
            rq = urllib3.Request(url)
            res = urllib3.urlopen(rq)
            csv = open('dfp/' + name, 'wb')
            csv.write(res.read())
            
            dfp_list.append({
                "name": name,  # Salvando o nome do arquivo 
                "content": csv   # Salvando o complemento do arquivo 
            })
            csv.close()

            

        return dfp_list