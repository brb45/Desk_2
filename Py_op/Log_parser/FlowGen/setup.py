from distutils.core import setup
import py2exe

setup(
    console=['flowGen.py'],
    options = {'py2exe': {'bundle_files': 1,
                          'dll_excludes': ['w9xpopen.exe']}},
    zipfile = None,
    )

