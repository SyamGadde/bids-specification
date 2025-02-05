"""This package is used to build elements in the bids-specification schema into
MarkDown format for the specification text.

Functions decorated in "define_env()" are callable throughout the
specification and are run/rendered with the mkdocs plugin "macros".
"""
import os
import sys

schemacode_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(schemacode_path)
from schemacode import macros


def define_env(env):
    """Define variables, macros and filters for the mkdocs-macros plugin.

    Parameters
    ----------
    env : :obj:`macros.plugin.MacrosPlugin`
        An object in which to inject macros, variables, and filters.

    Notes
    -----
    "variables" are the dictionary that contains the environment variables
    "macro" is a decorator function, to declare a macro.

    Macro aliases must start with "MACROS___", for compatibility with the PDF
    build code.
    """
    env.macro(macros.make_filename_template, "MACROS___make_filename_template")
    env.macro(macros.make_entity_table, "MACROS___make_entity_table")
    env.macro(
        macros.make_entity_definitions,
        "MACROS___make_entity_definitions"
    )
    env.macro(
        macros.make_metadata_table,
        "MACROS___make_metadata_table"
    )

    @env.macro
    def make_suffix_table(suffixes):
        return None
