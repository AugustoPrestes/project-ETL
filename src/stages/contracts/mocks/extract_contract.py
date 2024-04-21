from datetime import datetime
from src.stages.contracts.extract_contract import ExtractContract

extract_contracto_mock = ExtractContract(
        transent_information_content= [
            {'name_file': 'dfp_cia_aberta_2010.zip', 'link_file': 'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2010.zip'}, 
            {'name_file': 'dfp_cia_aberta_2011.zip', 'link_file': 'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2011.zip'}, 
            {'name_file': 'dfp_cia_aberta_2012.zip', 'link_file': 'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2012.zip'},
            {'name_file': 'dfp_cia_aberta_2013.zip', 'link_file': 'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2013.zip'}
        ],
        transent_information_length= 4,
        extraction_date= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)