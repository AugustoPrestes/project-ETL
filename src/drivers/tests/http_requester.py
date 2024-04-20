from typing import Dict
  
class HttpRequesterSpy:

    def __init__(self) -> None:
        self.request_from_page_count = 0 

    def request_from_page(self) -> Dict[int, str]:

        self.request_from_page_count +=1 

        return {
            "status_code": 200,
            "html": "<a>Retorno masked para o teste</a>"
        }
