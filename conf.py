#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# MicroPython documentation build configuration file, created by
# sphinx-quickstart on Sun Sep 21 11:42:03 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# SPDX-FileCopyrightText: 2014 MicroPython & CircuitPython contributors (https://github.com/adafruit/circuitpython/graphs/contributors)
#
# SPDX-License-Identifier: MIT

import logging
import os
import re
import subprocess
import sys
import urllib.parse
import time

import recommonmark
from sphinx.transforms import SphinxTransform
from docutils import nodes
from sphinx import addnodes

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('docs'))
sys.path.insert(0, os.path.abspath('.'))

import shared_bindings_matrix

master_doc = 'docs/index'

# Grab the JSON values to use while building the module support matrix
# in 'shared-bindings/index.rst'

# The stubs must be built before we calculate the shared bindings matrix
subprocess.check_output(["make", "stubs"])

#modules_support_matrix = shared_bindings_matrix.support_matrix_excluded_boards()
modules_support_matrix = shared_bindings_matrix.support_matrix_by_board()

html_context = {
    'support_matrix': modules_support_matrix
}

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.3'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinxcontrib.rsvgconverter',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'rstjinja',
    'recommonmark',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# The suffix of source filenames.
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

extensions.append('autoapi.extension')

autoapi_type = 'python'
# Uncomment this if debugging autoapi
autoapi_keep_files = True
autoapi_dirs = [os.path.join('circuitpython-stubs', x) for x in os.listdir('circuitpython-stubs')]
autoapi_add_toctree_entry = False
autoapi_options = ['members', 'undoc-members', 'private-members', 'show-inheritance', 'special-members', 'show-module-summary']
autoapi_template_dir = 'docs/autoapi/templates'
autoapi_python_class_content = "both"
autoapi_python_use_implicit_namespaces = True
autoapi_root = "shared-bindings"

redirects_file = 'docs/redirects.txt'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
#master_doc = 'index'

# Get current date (execution) for copyright year
current_date = time.localtime()

# General information about the project.
project = 'Adafruit CircuitPython'
copyright = f'2014-{current_date.tm_year}, MicroPython & CircuitPython contributors (https://github.com/adafruit/circuitpython/graphs/contributors)'

# These are overwritten on ReadTheDocs.
# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# We don't follow "The short X.Y version" vs "The full version, including alpha/beta/rc tags"
# breakdown, so use the same version identifier for both to avoid confusion.

final_version = ""
git_describe = subprocess.run(
    ["git", "describe", "--dirty", "--tags"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    encoding="utf-8"
)
if git_describe.returncode == 0:
    git_version = re.search(
        r"^\d(?:\.\d){0,2}(?:\-(?:alpha|beta|rc)\.\d+){0,1}",
        str(git_describe.stdout)
    )
    if git_version:
        final_version = git_version[0]
else:
    print("Failed to retrieve git version:", git_describe.stdout)

version = release = final_version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["**/build*",
                    ".git",
                    ".github",
                    ".env",
                    ".venv",
                    ".direnv",
                    "data",
                    "docs/autoapi",
                    "docs/README.md",
                    "drivers",
                    "examples",
                    "extmod",
                    "frozen",
                    "lib",
                    "main.c",
                    "mpy-cross",
                    "ports/*/*.c",
                    "ports/*/*.h",
                    "ports/*/boards",
                    "ports/*/common-hal",
                    "ports/*/supervisor",
                    "ports/atmel-samd/asf4",
                    "ports/atmel-samd/asf4_conf",
                    "ports/atmel-samd/external_flash",
                    "ports/atmel-samd/freetouch",
                    "ports/atmel-samd/peripherals",
                    "ports/atmel-samd/QTouch",
                    "ports/atmel-samd/tools",
                    "ports/cxd56/mkspk",
                    "ports/cxd56/spresense-exported-sdk",
                    "ports/esp32s2/certificates",
                    "ports/esp32s2/esp-idf",
                    "ports/esp32s2/.idf_tools",
                    "ports/esp32s2/peripherals",
                    "ports/litex/hw",
                    "ports/minimal",
                    "ports/mimxrt10xx/peripherals",
                    "ports/mimxrt10xx/sdk",
                    "ports/nrf/device",
                    "ports/nrf/bluetooth",
                    "ports/nrf/modules",
                    "ports/nrf/nrfx",
                    "ports/nrf/peripherals",
                    "ports/nrf/usb",
                    "ports/raspberrypi/sdk",
                    "ports/stm/st_driver",
                    "ports/stm/packages",
                    "ports/stm/peripherals",
                    "ports/stm/ref",
                    "ports/unix",
                    "py",
                    "shared-bindings/util.*",
                    "shared-module",
                    "supervisor",
                    "tests",
                    "tools"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = 'any'

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# Global include files. Sphinx docs suggest using rst_epilog in preference
# of rst_prolog, so we follow. Absolute paths below mean "from the base
# of the doctree".
rst_epilog = """
.. include:: /docs/templates/replace.inc
"""

# -- Options for HTML output ----------------------------------------------

# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    try:
        import sphinx_rtd_theme
        html_theme = 'sphinx_rtd_theme'
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path(), '.']
    except:
        html_theme = 'default'
        html_theme_path = ['.']
else:
    html_theme_path = ['.']

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = ['.']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = '../../logo/trans-logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'docs/static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['docs/static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%d %b %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {"index": "topindex.html"}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'CircuitPythondoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
# Include 3 levels of headers in PDF ToC
'preamble': '\setcounter{tocdepth}{2}',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'CircuitPython.tex', 'CircuitPython Documentation',
   'CircuitPython Contributors', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'CircuitPython', 'CircuitPython Documentation',
     ['CircuitPython contributors'], 1),
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'CircuitPython', 'CircuitPython Documentation',
   'CircuitPython contributors', 'CircuitPython', 'Python for Microcontrollers.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {"cpython": ('https://docs.python.org/3/', None),
                       "bus_device": ('https://circuitpython.readthedocs.io/projects/busdevice/en/latest/', None),
                       "register": ('https://circuitpython.readthedocs.io/projects/register/en/latest/', None)}

# Adapted from sphinxcontrib-redirects
from sphinx.builders import html as builders

TEMPLATE = """<html>
  <head><meta http-equiv="refresh" content="0; url=%s"/></head>
</html>
"""


def generate_redirects(app):
    path = os.path.join(app.srcdir, app.config.redirects_file)
    if not os.path.exists(path):
        logging.error("Could not find redirects file at '%s'" % path)
        return

    if not isinstance(app.builder, builders.StandaloneHTMLBuilder):
        logging.warn("The 'sphinxcontib-redirects' plugin is only supported "
                 "by the 'html' builder and subclasses. Skipping...")
        logging.warn(f"Builder is {app.builder.name} ({type(app.builder)})")
        return

    with open(path) as redirects:
        for line in redirects.readlines():
            from_path, to_path = line.rstrip().split(' ')

            logging.debug("Redirecting '%s' to '%s'" % (from_path, to_path))

            from_path = os.path.splitext(from_path)[0] + ".html"
            to_path_prefix = '..%s' % os.path.sep * (
                len(from_path.split(os.path.sep)) - 1)
            to_path = to_path_prefix + to_path

            redirected_filename = os.path.join(app.builder.outdir, from_path)
            redirected_directory = os.path.dirname(redirected_filename)
            if not os.path.exists(redirected_directory):
                os.makedirs(redirected_directory)

            with open(redirected_filename, 'w') as f:
                f.write(TEMPLATE % urllib.parse.quote(to_path, '#/'))


class CoreModuleTransform(SphinxTransform):
    default_priority = 870

    def _convert_first_paragraph_into_title(self):
        title = self.document.next_node(nodes.title)
        paragraph = self.document.next_node(nodes.paragraph)
        if not title or not paragraph:
            return
        if isinstance(paragraph[0], nodes.paragraph):
            paragraph = paragraph[0]
        if all(isinstance(child, nodes.Text) for child in paragraph.children):
            for child in paragraph.children:
                title.append(nodes.Text(" \u2013 "))
                title.append(child)
            paragraph.parent.remove(paragraph)

    def _enable_linking_to_nonclass_targets(self):
        for desc in self.document.traverse(addnodes.desc):
            for xref in desc.traverse(addnodes.pending_xref):
                if xref.attributes.get("reftype") == "class":
                    xref.attributes.pop("refspecific", None)

    def apply(self, **kwargs):
        docname = self.env.docname
        if docname.startswith(autoapi_root) and docname.endswith("/index"):
            self._convert_first_paragraph_into_title()
            self._enable_linking_to_nonclass_targets()


def setup(app):
    app.add_css_file("customstyle.css")
    app.add_config_value('redirects_file', 'redirects', 'env')
    app.connect('builder-inited', generate_redirects)
    app.add_transform(CoreModuleTransform)
