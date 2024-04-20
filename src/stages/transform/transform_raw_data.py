from typing import List, Dict
from src.stages.contracts.extract_contract import ExtractContract
import pandas as pd

class TransformRawData:
    
    def transform(self,  extract_contract: ExtractContract):
        self.__download_raw_data(extract_contract)

    def __download_raw_data(self, extract_contract: ExtractContract) -> List[Dict]:
        data_content = extract_contract.transent_information_content
        
        transformed_data = []

        for data in data_content:
            print(data)
