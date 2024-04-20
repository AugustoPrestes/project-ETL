from src.stages.contracts.extract_contract import ExtractContract
from .transform_raw_data import TransformRawData

def test_transform():
    transform_raw_data = TransformRawData()
    transform_raw_data.transform(ExtractContract)