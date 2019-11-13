import subprocess

import pytest


@pytest.mark.usefixtures("options")
class TestLongRun:
    @classmethod
    def setup_class(cls):
        # run lisflood
        pybin = cls.options['python']
        lisflood_py = cls.options['lisflood']
        settings_xml = cls.get_settings()
        subprocess.run(args=(pybin, lisflood_py, settings_xml), capture_output=True)

    @classmethod
    def get_settings(cls):


    def test_test(self):
        assert 0, self.options
