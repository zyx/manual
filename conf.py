
project = 'VCV Rack'
copyright = '2019, VCV'
author = 'VCV'

source_encoding = 'utf-8'

extensions = [
    'sphinx.ext.mathjax',
]

from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

templates_path = ['_templates']

master_doc = 'index'

language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# Theme

html_favicon = "favicon.png"

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    'logo_only': True,  # if we have a html_logo below, this shows /only/ the logo with no title text
    'collapse_navigation': False,  # Collapse navigation (False makes it tree-like)
}

html_context = {
    "display_github": True,
    "github_user": "VCVRack",
    "github_repo": "manual",
    "github_version": "master",
    "conf_py_path": "/",
}

html_logo = 'images/logo.png'

html_static_path = ['_static']

html_show_sphinx = False
html_show_copyright = False

htmlhelp_basename = 'VCVRackdoc'


latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'VCVRack.tex', 'VCV Rack Manual Documentation',
     'VCV', 'manual'),
]


epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']


def setup(app):
    app.add_stylesheet("overrides.css")
    app.add_config_value('recommonmark_config', {
        'enable_math': True,
        'enable_inline_math': True,
    }, True)
