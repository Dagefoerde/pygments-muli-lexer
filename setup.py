# -*- coding: utf-8 -*-
""" 
Pygments support for Muli

""" 
from setuptools import setup, find_packages

setup( 
    name         = 'pygments-muli-lexer',
    version      = '1.0',
    description  = __doc__,
    author       = "Jan C. Dageförde",
    install_requires = ['pygments'],
    packages     = find_packages(),
    entry_points = '''
    [pygments.lexers]
    mulilexer = pygments_muli_lexer.lexers:MuliLexer
    '''
)
