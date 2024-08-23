"""
    pygments.lexers.chatml
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexers for OpenAI Chat markup language.

    :copyright: Copyright 2006-2024 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexers.html import XmlLexer
from pygments.lexers.javascript import JavascriptLexer
from pygments.lexers.css import CssLexer
from pygments.lexers.lilypond import LilyPondLexer
from pygments.lexers.data import JsonLexer

from pygments.lexer import RegexLexer, DelegatingLexer, include, bygroups, \
    using, this, do_insertions, default, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Generic, Other, Whitespace, Literal
from pygments.util import get_bool_opt, ClassNotFound

__all__ = ['ChatMLLexer']


class ChatMLLexer(RegexLexer):
    """
    For ChatML markup.
    """
    name = 'ChatML'
    url = 'https://daringfireball.net/projects/markdown/'
    aliases = ['chatml']
    filenames = ['*.chatml']
    mimetypes = ["text/x-markdown"]
    version_added = '2.2'
    flags = re.MULTILINE

    tokens = {
        'root': [
            # Start special tokens
            (r'(^<\|im_start\|>)(.+)(\n)', bygroups(Keyword, Generic.Heading, Text)),
            # End special tokens
            (r'(<\|im_end\|>)(\s*?)(\n)', bygroups(Keyword, Whitespace, Text)),

            (r'<\|im_start\|>', Keyword),
            (r'(\")({.+})(\")', bygroups(Text, String, Text)),
            (r'{.+}', String),
            # # task list
            # (r'^(\s*)([*-] )(\[[ xX]\])( .+\n)',
            # bygroups(Whitespace, Keyword, Keyword, using(this, state='inline'))),
            # # bulleted list
            # (r'^(\s*)([*-])(\s)(.+\n)',
            # bygroups(Whitespace, Keyword, Whitespace, using(this, state='inline'))),
            # # numbered list
            # (r'^(\s*)([0-9]+\.)( .+\n)',
            # bygroups(Whitespace, Keyword, using(this, state='inline'))),
            # # quote
            # (r'^(\s*>\s)(.+\n)', bygroups(Keyword, Generic.Emph)),
            # # code block fenced by 3 backticks
            # (r'^(\s*```\n[\w\W]*?^\s*```$\n)', String.Backtick),
            # include('inline'),
            # general text, must come last!
            (r'[^\\\s<\|>]+', Text),
            (r'.', Text),
        ],
        # 'inline': [
        #     # escape
        #     (r'\\.', Text),
        #     # inline code
        #     (r'([^`]?)(`[^`\n]+`)', bygroups(Text, String.Backtick)),
        #     # warning: the following rules eat outer tags.
        #     # eg. **foo _bar_ baz** => foo and baz are not recognized as bold
        #     # bold fenced by '**'
        #     (r'([^\*]?)(\*\*[^* \n][^*\n]*\*\*)', bygroups(Text, Generic.Strong)),
        #     # bold fenced by '__'
        #     (r'([^_]?)(__[^_ \n][^_\n]*__)', bygroups(Text, Generic.Strong)),
        #     # italics fenced by '*'
        #     (r'([^\*]?)(\*[^* \n][^*\n]*\*)', bygroups(Text, Generic.Emph)),
        #     # italics fenced by '_'
        #     (r'([^_]?)(_[^_ \n][^_\n]*_)', bygroups(Text, Generic.Emph)),
        #     # strikethrough
        #     (r'([^~]?)(~~[^~ \n][^~\n]*~~)', bygroups(Text, Generic.Deleted)),
        #     # mentions and topics (twitter and github stuff)
        #     (r'[@#][\w/:]+', Name.Entity),
        #     # (image?) links eg: ![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)
        #     (r'(!?\[)([^]]+)(\])(\()([^)]+)(\))',
        #      bygroups(Text, Name.Tag, Text, Text, Name.Attribute, Text)),
        #     # reference-style links, e.g.:
        #     #   [an example][id]
        #     #   [id]: http://example.com/
        #     (r'(\[)([^]]+)(\])(\[)([^]]*)(\])',
        #      bygroups(Text, Name.Tag, Text, Text, Name.Label, Text)),
        #     (r'^(\s*\[)([^]]*)(\]:\s*)(.+)',
        #      bygroups(Text, Name.Label, Text, Name.Attribute)),

        #     # general text, must come last!
        #     (r'[^\\\s]+', Text),
        #     (r'.', Text),
        # ],
    }

    def __init__(self, **options):
        RegexLexer.__init__(self, **options)
