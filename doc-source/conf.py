#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys

from sphinx.locale import _

__version__ = "1.0.0"

project = "LC-MS User Guide"
slug = re.sub(r'\W+', '-', project.lower())
version = __version__
release = __version__
author = u'Dominic Davis-Foster'
copyright = author
language = 'en'

extensions = [
		'sphinx.ext.mathjax',
		'sphinx.ext.viewcode',
		'sphinxcontrib.httpdomain',
		]

templates_path = ['_templates']
source_suffix = '.rst'
exclude_patterns = []

master_doc = 'index'
suppress_warnings = ['image.nonlocal_uri']
pygments_style = 'default'

html_theme = 'sphinx_rtd_theme'
html_theme_options = {'logo_only': False}
html_theme_path = ["../.."]
html_logo = ""
html_show_sourcelink = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
		# Github Settings
		"display_github": False,  # Integrate GitHub
		"github_user": "domdfcoding",  # Username
		"github_repo": "",  # Repo name
		"github_version": "master",  # Version
		"conf_py_path": "/",  # Path in the checkout to the docs root
		}

htmlhelp_basename = slug

latex_documents = [
		('index', '{0}.tex'.format(slug), project, author, 'manual'),
		]

man_pages = [
		('index', slug, project, [author], 1)
		]

texinfo_documents = [
		('index', slug, project, author, slug, project, 'Miscellaneous'),
		]


# Extensions to theme docs
def setup(app):
	from sphinx.domains.python import PyField
	from sphinx.util.docfields import Field
	
	app.add_object_type(
			'confval',
			'confval',
			objname='configuration value',
			indextemplate='pair: %s; configuration value',
			doc_field_types=[
					PyField(
							'type',
							label=_('Type'),
							has_arg=False,
							names=('type',),
							bodyrolename='class'
							),
					Field(
							'default',
							label=_('Default'),
							has_arg=False,
							names=('default',),
							),
					]
			)
