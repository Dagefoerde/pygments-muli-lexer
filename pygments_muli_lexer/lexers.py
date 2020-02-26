from pygments.lexers.jvm import JavaLexer
from pygments.lexer import inherit
from pygments.token import *

__all__ = ['MuliLexer']

class MuliLexer(JavaLexer):
    name = 'MuliLexer'
    aliases = ['muli']
    filenames = ['*.muli']
    mimetypes = []
    tokens = {
        'root': [
            (r'(fail|free)\b', Keyword),
            inherit,
        ],
    }

