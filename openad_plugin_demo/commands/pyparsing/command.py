import os
import pyparsing as py
import pandas as pd

# OpenAD
from openad.core.help import help_dict_create_v2

# OpenAD tools
# from openad_tools.output import output_error, output_warning, output_text, output_success, output_table
from openad_plugin_demo.commands.pyparsing.output import (
    output_error,
    output_warning,
    output_text,
    output_success,
    output_table,
)
from openad_tools.helpers import description_txt, style_bool
from openad_tools.grammar_def import str_strict, str_catchall

# Plugin
# from openad_plugin_demo.plugin_grammar_def import hello, world
from openad_tools.grammar_def import *
from openad_plugin_demo.commands.pyparsing.description import description, avail_defs, avail_defs_str
from openad_plugin_demo.plugin_params import PLUGIN_NAME, PLUGIN_KEY, PLUGIN_NAMESPACE


class PluginCommand:
    """Hello world demo command"""

    category: str
    index: int
    name: str
    parser_id: str

    def __init__(self):
        self.category = "Intro"  # <-- EDIT: Category under which the command will be listed in help
        self.index = 0  # <-- EDIT: Order in which this command will be listed in help, relative to the categoryy
        self.name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
        self.parser_id = f"plugin_{PLUGIN_KEY}_{self.name}"

    def add_grammar(self, statements: list, grammar_help: list):
        """Create the command definition & documentation"""

        # Command definition
        statements.append(
            py.Forward(
                py.CaselessKeyword(PLUGIN_NAMESPACE)
                + py.CaselessKeyword("pp")
                + str_strict("definition")
                + py.Optional(str_catchall)("input")
            )(self.parser_id)
        )

        # Command help
        grammar_help.append(
            help_dict_create_v2(
                plugin_name=PLUGIN_NAME,
                plugin_namespace=PLUGIN_NAMESPACE,
                category=self.category,
                command=f"{PLUGIN_NAMESPACE} pp <definition> <input string>",
                description=description,
            )
        )

    def exec_command(self, cmd_pointer, parser):
        """Execute the command"""

        # Parse command
        cmd = parser.as_dict()
        definition = cmd["definition"]
        input = " ".join(cmd["input"])

        # Definition not available
        if definition not in avail_defs:
            output_error(f"Definition <yellow>{definition}</yellow> not recignized", pad_top=1)
            output_text("<soft>To see available definitions, run <cmd>demo pp ?</cmd></soft>", pad_btm=1)
            return

        # Parse input with the definition
        try:
            result = py.Forward(eval(definition)(definition)).parse_string(input, parseAll=True)
        except py.ParseException as e:
            result = "<error>Not parsable: </error>" + f"<soft>{e}</soft>"

        output = []
        output.append(f"<h1>{definition}</h1>")
        output.append(f"<yellow>Input:</yellow>  {input}")
        output.append(f"<yellow>Parsed:</yellow> {result}")
        if result and not isinstance(result, str):
            output.append(f"<yellow>Dict:</yellow> {result.as_dict()}")
        output_text("\n".join(output), pad=1)
