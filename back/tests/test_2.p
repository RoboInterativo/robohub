import pytest
import json
from robosite.init_db import *
from robosite.api import *
import os
# content of test_sample.py



def test_init_db_local():
    argv=['init_db.py', 'local']
    main(argv)
    assert 1 == 1

def test_api_get_file():
    f=os.listdir('./')
    l=file_atr(f[0]
    assert 1 == 1
