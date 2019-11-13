from pathlib import Path

import pytest


def pytest_addoption(parser):
    parser.addoption('-P', '--python', type=lambda p: Path(p).absolute(), help='Path to python binary')
    parser.addoption('-L', '--lisflood', type=lambda p: Path(p).absolute(), help='Path to main lisf1.py script')
    parser.addoption('-R', '--pathroot', type=lambda p: Path(p).absolute(), help='Path to Lisflood root directory')
    parser.addoption('-S', '--pathstatic', type=lambda p: Path(p).absolute(), help='Path to Lisflood static data (e.g. maps)')
    parser.addoption('-M', '--pathmeteo', type=lambda p: Path(p).absolute(), help='Path to Lisflood meteo forcings')
    parser.addoption('-I', '--pathinit', type=lambda p: Path(p).absolute(), help='Path to Lisflood init data')
    parser.addoption('-O', '--pathout', type=lambda p: Path(p).absolute(), help='Path to Lisflood results')


@pytest.fixture(scope='class', autouse=True)
def options(request):
    options = dict()
    options['python'] = request.config.getoption('--python')
    options['lisflood'] = request.config.getoption('--lisflood')
    options['meteopath'] = request.config.getoption('--pathmeteo')
    options['staticpath'] = request.config.getoption('--pathstatic')
    options['initpath'] = request.config.getoption('--pathinit')
    options['rootpath'] = request.config.getoption('--pathroot')
    options['pathout'] = request.config.getoption('--pathout')
    request.cls.options = options
    return options
