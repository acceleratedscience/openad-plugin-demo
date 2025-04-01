import os
import pyparsing as py

# OpenAD
from openad.core.help import help_dict_create_v2

# OpenAD tools
from openad_tools.grammar_def import (
    molecule_s,
    molecule_identifier_s,
)

# Plugin
from openad_plugin_demo.plugin_grammar_def import visualize, clause_basic
from openad_plugin_demo.plugin_params import PLUGIN_NAME, PLUGIN_KEY, PLUGIN_NAMESPACE
from openad_plugin_demo.commands.visualize_molecules.visualize_molecules import visualize_molecules
from openad_plugin_demo.commands.visualize_molecules.description import description


class PluginCommand:
    """Visualize molecules demo command"""

    category: str  # Category of command
    index: int  # Order in help
    name: str  # Name of command = command dir name
    parser_id: str  # Internal unique identifier

    def __init__(self):
        self.category = "Molecules"
        self.index = 2
        self.name = os.path.dirname(os.path.abspath(__file__))
        self.parser_id = f"plugin_{PLUGIN_KEY}_{self.name}"

    def add_grammar(self, statements: list, grammar_help: list):
        """Create the required command grammar & documentation"""

        # Command definition
        statements.append(
            py.Forward(
                py.CaselessKeyword(PLUGIN_NAMESPACE)
                + visualize
                + molecule_s
                + py.Optional(molecule_identifier_s)
                + clause_basic
            )(self.parser_id)
        )

        # Command help
        grammar_help.append(
            help_dict_create_v2(
                plugin_name=PLUGIN_NAME,
                plugin_namespace=PLUGIN_NAMESPACE,
                category=self.category,
                command=[
                    # Visualize an individual molecule
                    f"{PLUGIN_NAMESPACE} visualize molecule <molecule_identifier> [ basic ]",
                    # Visualize a list of molecules
                    f"{PLUGIN_NAMESPACE} visualize molecules [<molecule_identifier>,<molecule_identifier>,...] [ basic ]",
                ],
                description=description,
            )
        )

    def exec_command(self, cmd_pointer, parser):
        """Execute the command"""

        cmd = parser.as_dict()

        visualize_molecules(cmd_pointer, cmd)
