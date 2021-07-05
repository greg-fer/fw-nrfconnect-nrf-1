# Matter documentation build configuration file

from pathlib import Path
import sys
import os
from sphinx.config import eval_config_file


# Paths ------------------------------------------------------------------------

NRF_BASE = Path(__file__).absolute().parent / ".." / ".."

MATTER_BASE = os.environ.get("MATTER_BASE")
if not MATTER_BASE:
    raise FileNotFoundError("MATTER_BASE not defined")
MATTER_BASE = Path(MATTER_BASE)

MATTER_BUILD = os.environ.get("MATTER_BUILD")
if not MATTER_BUILD:
    raise FileNotFoundError("MATTER_BUILD not defined")
MATTER_BUILD = Path(MATTER_BUILD)

sys.path.insert(0, str(NRF_BASE / "doc" / "_utils"))
import utils

# pylint: disable=undefined-variable

# General ----------------------------------------------------------------------

# Import Matter configuration, override as needed later
conf = eval_config_file(str(MATTER_BASE / "docs" / "conf.py"), tags)
locals().update(conf)

sys.path.insert(0, str(NRF_BASE / "doc" / "_extensions"))
extensions.extend(["external_content", "doxyrunner"])

# Options for HTML output ------------------------------------------------------

html_static_path.append(str(NRF_BASE / "doc" / "_static"))
html_theme_options = {"docsets": utils.get_docsets("matter")}

# -- Options for doxyrunner ----------------------------------------------------

doxyrunner_doxygen = os.environ.get("DOXYGEN_EXECUTABLE", "doxygen")
doxyrunner_doxyfile = NRF_BASE / "doc" / "matter" / "matter.doxyfile.in"
doxyrunner_outdir = MATTER_BUILD / "doxygen"
doxyrunner_fmt = True
doxyrunner_fmt_vars = {
    "MATTER_BASE": str(MATTER_BASE),
    "OUTPUT_DIRECTORY": str(doxyrunner_outdir),
}

# Options for breathe ----------------------------------------------------------

breathe_projects = {"matter": str(doxyrunner_outdir / "xml")}

# Options for external_content -------------------------------------------------

from external_content import DEFAULT_DIRECTIVES
directives = DEFAULT_DIRECTIVES + ("mdinclude", )

external_content_directives = directives
external_content_contents = [
    (NRF_BASE / "doc" / "matter", "*.rst"),
    (MATTER_BASE / "docs", "*.md"),
    (MATTER_BASE / "docs" / "guides", "*.md"),
]

# pylint: enable=undefined-variable


def setup(app):
    app.add_css_file("css/common.css")
    app.add_css_file("css/matter.css")
