from typing import List, Dict


class HtmlCollectorSpy:

    def __init__(self) -> None:
        self.collect_essential_information_atributes = {}

    
    def collect_essential_information(self, html: str) -> List[Dict[str, str]]:

        self.collect_essential_information_atributes["html"] = html
        # Adicionand"o o nome do arquivo e seu caminho na web
        return [{
            "name_file": 'SomeName',
            "link_file": 'https://Link.com'
        }]
