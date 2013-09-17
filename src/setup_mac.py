"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
import os

APP = ['main.py']

PACKAGES = ['lxml']

INCLUDES = ['sip']

OPTIONS = {'argv_emulation': False,
           'packages': PACKAGES,
           'includes': INCLUDES,
           'plist': 'Info.plist'}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
