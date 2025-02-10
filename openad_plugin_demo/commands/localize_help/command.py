import os
import datetime
import pandas as pd
import pyparsing as py

# OpenAD
from openad.core.help import help_dict_create_v2

# OpenAD tools
from openad_tools.output import output_error, output_warning, output_text, output_success, output_table
from openad_tools.helpers import description_txt

# Plugin
from openad_plugin_demo.plugin_grammar_def import localize, a, b
from openad_plugin_demo.plugin_params import PLUGIN_NAME, PLUGIN_KEY, PLUGIN_NAMESPACE
from openad_plugin_demo.commands.localize_help.description import description


class PluginCommand:
    """Localization demo command"""

    category: str  # Category of command
    index: int  # Order in help
    name: str  # Name of command = command dir name
    parser_id: str  # Internal unique identifier

    def __init__(self):
        self.category = "Language localization"
        self.index = 3
        self.name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
        self.parser_id = f"plugin_{PLUGIN_KEY}_{self.name}"

    def add_grammar(self, statements: list, grammar_help: list):
        """Create the command definition & documentation"""

        # Command definition
        statements.append(py.Forward(py.CaselessKeyword(PLUGIN_NAMESPACE) + localize + a)(self.parser_id))
        statements.append(py.Forward(py.CaselessKeyword(PLUGIN_NAMESPACE) + localize + b)(self.parser_id))

        # Command help
        grammar_help.append(
            help_dict_create_v2(
                plugin_name=PLUGIN_NAME,
                plugin_namespace=PLUGIN_NAMESPACE,
                category=self.category,
                command=f"{PLUGIN_NAMESPACE} localize a",
                description_file=description_txt(__file__),
            )
        )
        grammar_help.append(
            help_dict_create_v2(
                plugin_name=PLUGIN_NAME,
                plugin_namespace=PLUGIN_NAMESPACE,
                category=self.category,
                command=f"{PLUGIN_NAMESPACE} localize b",
                description=description,  # <-- desciption string
            )
        )

    def exec_command(self, cmd_pointer, parser):
        """Execute the command"""

        cmd = parser.as_dict()
        print(cmd)

        return output_warning(
            "Append this command with a question mark to see the localized help.\n<cmd>demo localize a ?</cmd>"
        )
