#!c:\users\jsun\documents\py_projects\pytest_proj\pytest_02\env_3.7\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'tasks','console_scripts','tasks'
__requires__ = 'tasks'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('tasks', 'console_scripts', 'tasks')()
    )
