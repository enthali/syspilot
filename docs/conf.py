# Configuration file for the Sphinx documentation builder.
# syspilot sphinx-needs configuration
#
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Project information -----------------------------------------------------

project = 'syspilot'
copyright = '2025-2026, syspilot Contributors'
author = 'syspilot Contributors'
release = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.graphviz',
    'sphinx_needs',
    'myst_parser',
]

html_show_sourcelink = False

templates_path = ['_templates']
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '.venv',
    'venv',
    'changes/*',
]

# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'
html_static_path = ['_static']
html_title = 'syspilot'
html_logo = '../assets/syspilot-logo.svg'

html_theme_options = {
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/enthali/syspilot",
            "html": '<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>',
            "class": "",
        },
    ],
}

html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
        "github-link.html",
    ],
}

# -- Sphinx-Needs Configuration ----------------------------------------------
# https://sphinx-needs.readthedocs.io/

needs_types = [
    # User Stories - WHY (Stakeholder perspective)
    dict(
        directive="story",
        title="User Story",
        prefix="US_",
        color="#E8D5B7",
        style="node"
    ),
    # Requirements - WHAT (System behavior)
    dict(
        directive="req",
        title="Requirement",
        prefix="REQ_",
        color="#BFD8D2",
        style="node"
    ),
    # Design Specifications - HOW (Technical approach)
    dict(
        directive="spec",
        title="Design Specification",
        prefix="SPEC_",
        color="#FEDCD2",
        style="node"
    ),
    # Implementation - WHERE (Code location)
    dict(
        directive="impl",
        title="Implementation",
        prefix="IMPL_",
        color="#DF744A",
        style="node"
    ),
    # Test Cases - VERIFY (Validation)
    dict(
        directive="test",
        title="Test Case",
        prefix="TEST_",
        color="#DCB239",
        style="node"
    ),
]

# Extra options for needs
needs_extra_options = [
    "priority",
    "rationale",
    "acceptance_criteria",
]

# Status options
needs_statuses = [
    dict(name="draft", description="Draft - Work in progress"),
    dict(name="open", description="Open - Identified but not yet started"),
    dict(name="approved", description="Approved - Ready for implementation"),
    dict(name="implemented", description="Implemented - Code exists"),
    dict(name="verified", description="Verified - Tested and validated"),
    dict(name="deprecated", description="Deprecated - No longer used"),
]

# Priority options  
needs_priority = [
    dict(name="mandatory", description="Must have - Critical requirement"),
    dict(name="high", description="Should have - Important requirement"),
    dict(name="medium", description="Could have - Nice to have"),
    dict(name="low", description="Won't have this time - Future consideration"),
]

# Require explicit IDs
needs_id_required = True

# Configure needs file output
needs_build_json = True
needs_build_json_per_id = True

# Use Graphviz for needflow diagrams
needs_flow_engine = "graphviz"

# Configure needflow to use SVG
needs_flow_configs = {
    'needflow': {
        'engine': 'dot',
        'format': 'svg',
    }
}

# -- MyST Parser Configuration -----------------------------------------------
# https://myst-parser.readthedocs.io/

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
]

# -- Intersphinx Configuration -----------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- Todo Extension Configuration --------------------------------------------

todo_include_todos = True
