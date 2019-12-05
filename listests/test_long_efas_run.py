import os
import sys
import uuid
import subprocess
import unittest
from pathlib import Path

from bs4 import BeautifulSoup
import pytest

from lisfloodutilities.compare import NetCDFComparator, TSSComparator

from listests import logger


"""
How to run:

pytest test_long_efas_run.py -L /workarea/lisflood_versions/lf_first_merged/lisf1.py -R /workarea/EFAS/ \
  -M /workarea/EFAS/EFAS_forcings/ -O /workarea/lf_results/1_e5eb9f03 -s 
  -P /workarea/virtualenvs/lisflood27/bin/python -I /workarea/lf_results/reference/EFAS/InitSafe/
"""

@pytest.mark.usefixtures("options")
class TestLongRun:

    @classmethod
    def setup_class(cls):
        # run lisflood
        pybin = cls.options['python']
        lisflood_py = cls.options['lisflood']
        pathout = cls.options['PathOut']
        if not lisflood_py:
            if not pathout:
                raise ValueError('You must set --pathout to point to existing LISFLOOD results, '
                                 'if not setting --lisflood option to run a simulation with a specific version')
            return
        cls.settings_xml = cls.get_settings()
        cell = cls.settings_xml.select('lfuser textvar[name="MaskMap"]')[0]
        cls.mask_map = cell.attrs['value'].replace('$(PathRoot)', str(cls.options['pathroot']))
        uid = uuid.uuid4()
        filename = f'./efas_day_{uid}.xml'
        logger.info(f'>>>>Generated {filename}\n')
        with open(filename, 'w') as dest:
            dest.write(cls.settings_xml.prettify())
        cls.settings_filepath = Path(filename).absolute()
        logger.info(f'>>>>Executing....:\n{pybin} {lisflood_py} {cls.settings_filepath}\n')
        logger.info(' =============== START OF LISFLOOD OUTPUT ===============')
        lisflood_cmd = ' '.join((pybin.as_posix(), lisflood_py.as_posix(), cls.settings_filepath.as_posix()))
        p = subprocess.Popen(args=(lisflood_cmd,),
                             stdout=subprocess.PIPE, shell=True,
                             stderr=subprocess.STDOUT, universal_newlines=True)
        # Poll process for new output until finished
        while True:
            nextline = p.stdout.readline()
            if nextline == '' and p.poll() is not None:
                break
            sys.stdout.write(nextline)
            sys.stdout.flush()
        logger.info(' =============== END OF LISFLOOD OUTPUT ===============')

        if p.returncode:
            raise subprocess.CalledProcessError(p.returncode, (pybin, lisflood_py, cls.settings_filepath))

    @classmethod
    def teardown_class(cls):
        os.remove(cls.settings_filepath)

    @classmethod
    def get_settings(cls):
        tpl = open('./settings_full_efas_day.xml')
        soup = BeautifulSoup(tpl, 'lxml-xml')
        for textvar in ('PathRoot', 'PathMeteo', 'PathOut', 'PathStatic', 'PathInit'):
            for tag in soup.find_all("textvar", {'name': textvar}):
                logger.info(tag['value'])
                logger.info('Replacing with %s', cls.options[textvar.lower()])
                tag['value'] = cls.options[textvar.lower()]
        return soup

    def test_rep_maps(self):
        # check all nc. maps in output folder
        comparator = NetCDFComparator(self.mask_map)
        diffs = comparator.compare_dirs(self.options['reference'], self.options['pathout'])
        assert not diffs

    def test_tss(self):
        # check all TSS in output folder
        comparator = TSSComparator()
        diffs = comparator.compare_dirs(self.options['reference'], self.options['pathout'])
        assert not diffs

    def test_state_end_maps(self):
        # 1. check if repEndMaps is True. If so, check that end maps were written
        # 2. check if repStateMaps is True. If so, check that state maps were written
        # 3. If both were written, last step in state maps must be identical to the unique step in end maps
        pass
    #     # comparator = NetCDFComparator(self.mask_map)
    #     # res = comparator.compare_dirs(self.options['pathout'], self.options['reference'])
