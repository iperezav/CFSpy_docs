# conf.py — safe overrides for a Jupyter‑Book project

# ------------------------------------------------------------
# Extra Sphinx extensions (added on top of Jupyter‑Book defaults)
# ------------------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    'sphinx.ext.graphviz',
    "sphinxcontrib.mermaid",
]

# ------------------------------------------------------------
# Custom static assets (CSS/JS)
# ------------------------------------------------------------
def setup(app):
    # Add custom CSS without overriding the theme
    app.add_css_file("assets/css/custom.css")
    # app.add_js_file("assets/js/custom.js")  # optional

# ------------------------------------------------------------
# Theme‑compatible overrides
# ------------------------------------------------------------
# These options *extend* the Jupyter‑Book theme rather than replace it.
# They are merged with the auto‑generated config.
html_theme_options = {
    # Keep Jupyter‑Book’s structure but add enhancements
    "use_download_button": True,
    "navigation_depth": 4,
}

# ------------------------------------------------------------
# Strictness options (optional)
# ------------------------------------------------------------
# Turn on if you want broken links to fail the build
nitpicky = False

# Example: custom substitutions usable in Markdown/RST
rst_epilog = """
.. |project| replace:: CFSpy
"""