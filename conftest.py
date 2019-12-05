import os
from pathlib import Path
from itertools import chain

import pytest

from listests import logger


def pytest_addoption(parser):
    parser.addoption('-P', '--python', type=lambda p: Path(p), help='Path to python binary', default='python')
    parser.addoption('-L', '--lisflood', type=lambda p: Path(p).absolute(), help='Path to main lisf1.py script')
    parser.addoption('-R', '--pathroot', type=lambda p: Path(p).absolute(), help='Path to Lisflood root directory')
    parser.addoption('-S', '--pathstatic', type=lambda p: Path(p).absolute(), help='Path to Lisflood static data (e.g. maps)')
    parser.addoption('-M', '--pathmeteo', type=lambda p: Path(p).absolute(), help='Path to Lisflood meteo forcings')
    parser.addoption('-I', '--pathinit', type=lambda p: Path(p).absolute(), help='Path to Lisflood init data')
    parser.addoption('-O', '--pathout', type=lambda p: Path(p).absolute(), help='Path to Lisflood results')
    parser.addoption('-X', '--reference', type=lambda p: Path(p).absolute(), help='Path to Lisflood oracle results', required=True)


@pytest.fixture(scope='class', autouse=True)
def options(request):
    options = dict()
    options['python'] = request.config.getoption('--python')
    options['lisflood'] = request.config.getoption('--lisflood')
    options['pathroot'] = request.config.getoption('--pathroot')
    options['pathmeteo'] = request.config.getoption('--pathmeteo') or options['pathroot']
    options['pathstatic'] = request.config.getoption('--pathstatic') or options['pathroot']
    options['pathout'] = request.config.getoption('--pathout') or options['pathroot']
    options['pathinit'] = request.config.getoption('--pathinit') or options['pathroot']
    options['reference'] = request.config.getoption('--reference')
    if options['pathout'].exists():
        logger.warning('Removing older results from %s', options['pathout'].as_posix())
        for f in chain(options['pathout'].glob('*.nc'), options['pathout'].glob('*.tss'), options['pathout'].glob('*.end')):
            logger.warning('removing %s', f.as_posix())
            os.unlink(f)
        logger.info('End of removing old results')
    else:
        options['pathout'].mkdir()
    request.cls.options = options
    return options
