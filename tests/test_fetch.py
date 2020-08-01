# -*- coding: utf-8 -*-
import json
from unittest.mock import MagicMock
from .context import TWCB
import pandas as pd
from pathlib import Path

USE_MOCK = True

class TestFetch:
    """Basic test cases."""
    
    def test_fetch_single_sheet(self,monkeypatch):
        fake_fetch_single_sheet_page = MagicMock()
        monkeypatch.setattr('TWCB.fetch.fetch_single_sheet_page',fake_fetch_single_sheet_page)

        for tb_name in ['BP01D01','BPF4Y01','BPP2Q01','EG21M01','EG41M01','FL01_cn']:
            with open(Path('tests/test_cases/{}.json'.format(tb_name)),'r',encoding="utf-8") as f:
                test_json = json.load(f)

                fake_fetch_single_sheet_page.return_value = eval(test_json)
                result = TWCB.fetch.fetch_single_sheet(tb_name)
                assert isinstance(result,(pd.DataFrame))
                assert result.shape[0] > 0
                assert result.shape[1] > 0
