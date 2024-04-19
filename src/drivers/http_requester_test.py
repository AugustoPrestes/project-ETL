from .http_requester import HttpRequester

def test_request_from_page(requests_mock):
    # Criando o URL mock
    url = 'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/'
    requests_mock.get(url, status_code=200, text='Mock Request')

    # Criando o objeto da request
    http_requester = HttpRequester()

    # Armazenando o retorno da requisição
    request_response = http_requester.request_from_page()

    # Testando o retorno da função
    assert 'status_code' in request_response
    assert 'html' in request_response
    assert request_response['status_code'] == 200
                                  