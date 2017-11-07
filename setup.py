from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    windows = ["fairy_kingdom.py"],
    zipfile = None,
    options = {
				'py2exe': {
						'dll_excludes': ['numpy-atlas.dll',
										 # don't include system .dll's
										 'OLEAUT32.dll',
										 'USER32.dll',
										 'IMM32.dll',
										 'SHELL32.dll',
										 'ole32.dll',
										 'COMDLG32.dll',
										 'COMCTL32.dll',
										 'ADVAPI32.dll',
										 'msvcrt.dll',
										 'WS2_32.dll',
										 'GDI32.dll',
										 'WINMM.dll',
										 'KERNEL32.dll',
										],
						'bundle_files': 1,
				
				
				}
				
	},
)