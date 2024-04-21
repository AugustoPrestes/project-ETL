from src.stages.contracts.mocks.extract_contract import extract_contracto_mock
from .transform_raw_data import TransformRawData

def test_transform():
    transform_raw_data = TransformRawData()
    transform_raw_data.transform(extract_contracto_mock)