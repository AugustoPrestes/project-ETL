import requests
from typing import Dict

class HttpRequester:
    def __init__(self) -> None:
        self.__url =  'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/'
        # self.__url =  'https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm' # URL para acessar o site utilizado no projeto original

    def request_from_page(self) -> Dict[int, str]: 
        resposnse = requests.get(self.__url)
        
        return {
            "status_code": resposnse.status_code,
            "html": resposnse.text
        }
     