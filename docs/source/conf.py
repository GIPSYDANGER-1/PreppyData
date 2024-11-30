# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PreppyData'
copyright = '2024, yoominji'
author = 'yoominji'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions에 myst_parser 추가
extensions = [] 


# 헤더에 앵커 추가 (h1, h2, h3까지 지원)
myst_heading_anchors = 3



templates_path = ['_templates']
exclude_patterns = []

language = 'python'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # 사용 중인 테마
html_theme_options = {
    'canonical_url': 'https://yourproject.readthedocs.io/',
    'logo_only': True,
    # 'display_version': True,  # 이 줄을 제거하거나 주석 처리합니다.
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
}
html_static_path = ['_static']
