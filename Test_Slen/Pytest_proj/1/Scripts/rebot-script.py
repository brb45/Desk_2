#!c:\users\jsun\documents\py_projects\pytest_proj\01\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'robotframework==3.1.2','console_scripts','rebot'
__requires__ = 'robotframework==3.1.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('robotframework==3.1.2', 'console_scripts', 'rebot')()
    )
