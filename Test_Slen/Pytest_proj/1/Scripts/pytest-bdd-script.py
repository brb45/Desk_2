#!c:\users\jsun\documents\py_projects\pytest_proj\01\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pytest-bdd==3.1.1','console_scripts','pytest-bdd'
__requires__ = 'pytest-bdd==3.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pytest-bdd==3.1.1', 'console_scripts', 'pytest-bdd')()
    )
