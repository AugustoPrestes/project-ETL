import requests
from typing import Dict

class HttpRequester:
    def __init__(self) -> None:
        self.__url =  'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/'

    def request_from_page(self) -> Dict: 
        resposnse = requests.get(self.__url)
        
        return {
            "status_code": resposnse.status_code,
            "html": resposnse.text
        }
     