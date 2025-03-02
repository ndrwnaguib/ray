# -*- coding: utf-8 -*-
#
# Ray documentation build configuration file, created by
# sphinx-quickstart on Fri Jul  1 13:19:58 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import glob
import shutil
import sys
import os

sys.path.insert(0, os.path.abspath("."))
from custom_directives import *
from datetime import datetime

# These lines added to enable Sphinx to work without installing Ray.
import mock


class ChildClassMock(mock.Mock):
    @classmethod
    def __getattr__(cls, name):
        return mock.Mock


for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()

sys.modules["tensorflow"].VERSION = "9.9.9"

for mod_name in CHILD_MOCK_MODULES:
    sys.modules[mod_name] = ChildClassMock()

assert (
    "ray" not in sys.modules
), "If ray is already imported, we will not render documentation correctly!"

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath("../../python/"))

import ray

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_click.ext",
    # "sphinx_panels",
    "sphinx_tabs.tabs",
    "sphinx-jsonschema",
    "sphinx_gallery.gen_gallery",
    "sphinxemoji.sphinxemoji",
    "sphinx_copybutton",
    "sphinxcontrib.yt",
    "versionwarning.extension",
    "sphinx_sitemap",
    "myst_parser",
    # "myst_nb",
    "sphinx.ext.doctest",
    "sphinx.ext.coverage",
    "sphinx_external_toc",
]

external_toc_exclude_missing = False
external_toc_path = '_toc.yml'

# There's a flaky autodoc import for "TensorFlowVariables" that fails depending on the doc structure / order
# of imports.
# autodoc_mock_imports = ["ray.experimental.tf_utils"]

# This is used to suppress warnings about explicit "toctree" directives.
suppress_warnings = ["etoc.toctree"]

versionwarning_admonition_type = "note"
versionwarning_banner_title = "Join the Ray Discuss Forums!"

FORUM_LINK = "https://discuss.ray.io"
versionwarning_messages = {
    # Re-enable this after Ray Summit.
    # "latest": (
    #     "This document is for the latest pip release. "
    #     'Visit the <a href="/en/master/">master branch documentation here</a>.'
    # ),
    "master": (
        "<b>Got questions?</b> Join "
        f'<a href="{FORUM_LINK}">the Ray Community forum</a> '
        "for Q&A on all things Ray, as well as to share and learn use cases "
        "and best practices with the Ray community."),
}

versionwarning_body_selector = "#main-content"

sphinx_gallery_conf = {
    # Example sources are taken from these folders:
    "examples_dirs": [
        "ray-core/_examples",
        "tune/_tutorials",
        "data/_examples",
    ],
    # and then generated into these respective target folders:
    "gallery_dirs": ["ray-core/examples", "tune/tutorials", "data/examples"],
    "ignore_pattern": "ray-core/examples/doc_code/",
    "plot_gallery": "False",
    "min_reported_time": sys.maxsize,
    # "filename_pattern": "tutorial.py",
    # "backreferences_dir": "False",
    # "show_memory': False,
}

for i in range(len(sphinx_gallery_conf["examples_dirs"])):
    gallery_dir = sphinx_gallery_conf["gallery_dirs"][i]
    source_dir = sphinx_gallery_conf["examples_dirs"][i]
    try:
        os.mkdir(gallery_dir)
    except OSError:
        pass

    # Copy rst files from source dir to gallery dir.
    for f in glob.glob(os.path.join(source_dir, "*.rst")):
        shutil.copy(f, gallery_dir)

    # Copy inc files from source dir to gallery dir.
    for f in glob.glob(os.path.join(source_dir, "*.inc")):
        shutil.copy(f, gallery_dir)

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Ray"
copyright = str(datetime.now().year) + ", The Ray Team"
author = "The Ray Team"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
from ray import __version__ as version

# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]
exclude_patterns += sphinx_gallery_conf["examples_dirs"]

# If "DOC_LIB" is found, only build that top-level navigation item.
build_one_lib = os.getenv("DOC_LIB")

all_toc_libs = [
    f.path for f in os.scandir(".") if f.is_dir() and "ray-" in f.path
]
all_toc_libs += [
    "cluster", "tune", "data", "raysgd", "train", "rllib", "serve", "workflows"
]
if build_one_lib and build_one_lib in all_toc_libs:
    all_toc_libs.remove(build_one_lib)
    exclude_patterns += all_toc_libs

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "lovelace"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Do not check anchors for links because it produces many false positives
# and is slow (it needs to download the linked website).
linkcheck_anchors = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_book_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "repository_url": "https://github.com/ray-project/ray",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "path_to_docs": "doc/source",
    "home_page_in_toc": False,
    "show_navbar_depth": 0,
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = f"Ray {release}"

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "images/ray_logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# TODO: this adds algolia search. can activate this once sphinx-tabs has been
# replaced by sphinx-panels.
# html_css_files = [
#     "https://cdn.jsdelivr.net/npm/docsearch.js@2/dist/cdn/docsearch.min.css",
# ]
#
# html_js_files = [
#     (
#         "https://cdn.jsdelivr.net/npm/docsearch.js@2/dist/cdn/docsearch.min.js",
#         {"defer": "defer"},
#     ),
#     ("docsearch.sbt.js", {"defer": "defer"}),
# ]
html_static_path = ["_static"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {'**': ['index.html']}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = "Raydoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "Ray.tex", "Ray Documentation", author, "manual"),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "ray", "Ray Documentation", [author], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False

# -- Options for Texinfo output -------------------------------------------
# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "Ray",
        "Ray Documentation",
        author,
        "Ray",
        "Ray provides a simple, universal API for building distributed applications.",
        "Miscellaneous",
    ),
]

# Python methods should be presented in source code order
autodoc_member_order = "bysource"


def setup(app):
    app.connect("html-page-context", update_context)
    # Custom CSS
    app.add_css_file("css/custom.css")
    # Custom Sphinx directives
    app.add_directive("customgalleryitem", CustomGalleryItemDirective)
    # Custom docstring processor
    app.connect("autodoc-process-docstring", fix_xgb_lgbm_docs)
