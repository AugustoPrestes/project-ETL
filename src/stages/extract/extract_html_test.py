from src.drivers.tests.http_requester import HttpRequesterSpy   # Utilizando uma classe Spy para não gerar um requisição
from src.drivers.tests.html_collector import HtmlCollectorSpy   # Utilizando uma classe Spy para não gerar um requisição
from src.stages.contracts.extract_contract import ExtractContract

from src.errors.extract_error import ExtractError
from .extract_html import ExtractHtml

def test_extract():
    http_requester = HttpRequesterSpy()
    html_collector = HtmlCollectorSpy()

    extract_html = ExtractHtml(http_requester, html_collector)
    response = extract_html.extract()


    # Bloco de Confirmações
    assert isinstance(response, ExtractContract)
    assert http_requester.request_from_page_count == 1
    assert 'html' in html_collector.collect_essential_information_atributes  

def test_extract_error():
    http_requester = 'Erro'                 # Str adicionada para que possamos ter o retorno do Erro
    html_collector = HtmlCollectorSpy()

    extract_html = ExtractHtml(http_requester, html_collector)

    try:
        extract_html.extract()

    except Exception as exception:
        # Bloco de Confirmações
        assert isinstance(exception, ExtractError)
    