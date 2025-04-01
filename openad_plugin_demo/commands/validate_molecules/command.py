import os
import pandas as pd
import pyparsing as py

# OpenAD
from openad.core.help import help_dict_create_v2
from openad.smols.smol_functions import valid_identifier
from openad.app.global_var_lib import MEMORY

# OpenAD tools
from openad_tools.spinner import spinner
from openad_tools.output import output_text, output_error, output_table
from openad_tools.helpers import style_bool
from openad_tools.grammar_def import molecule_s, molecule_identifier_s

# Plugin
from openad_plugin_demo.plugin_grammar_def import validate
from openad_plugin_demo.plugin_params import PLUGIN_NAME, PLUGIN_KEY, PLUGIN_NAMESPACE
from openad_plugin_demo.commands.validate_molecules.description import description


class PluginCommand:
    """Validate molecules demo command"""

    category: str  # Category of command
    index: int  # Order in help
    name: str  # Name of command = command dir name
    parser_id: str  # Internal unique identifier

    def __init__(self):
        self.category = "Molecules"
        self.index = 1
        self.name = os.path.dirname(os.path.abspath(__file__))
        self.parser_id = f"plugin_{PLUGIN_KEY}_{self.name}"

    def add_grammar(self, statements: list, grammar_help: list):
        """Create the required command grammar & documentation"""

        # Command parser
        statements.append(
            py.Forward(py.CaselessKeyword(PLUGIN_NAMESPACE) + validate + molecule_s + molecule_identifier_s)(
                self.parser_id
            )
        )

        # Command documentation
        grammar_help.append(
            help_dict_create_v2(
                plugin_name=PLUGIN_NAME,
                plugin_namespace=PLUGIN_NAMESPACE,
                category=self.category,
                command=[
                    f"{PLUGIN_NAMESPACE} validate mol <molecule_identifier>",
                    f"{PLUGIN_NAMESPACE} validate mols [<molecule_identifier>,<molecule_identifier>,...]",
                ],
                description=description,
            )
        )

    def exec_command(self, cmd_pointer, parser):
        """Execute the command"""

        cmd = parser.as_dict()

        # Parse & display list of identifiers
        identifiers = cmd.get("identifiers")
        if not identifiers:
            output_error("No identifiers provided")
            return
        output_text(
            "Identified molecules:\n" + "- <yellow>" + "</yellow>\n- <yellow>".join(identifiers) + "</yellow>", pad=1
        )

        # Start loader
        spinner.start("Validating")

        # Validate identifiers and store results in dataframe
        table = []
        for identifier in identifiers:
            spinner.start(f"Validating {identifier}")
            table.append(
                {
                    "Identifier": identifier,
                    "Valid InChI/SMILES": style_bool(valid_identifier(identifier)),
                    "Valid other": style_bool(valid_identifier(identifier, rich=True)),
                }
            )
        table = pd.DataFrame(table)

        # Stop loader
        spinner.stop()

        # Store identifiers in memory
        # This allows a follow-up command to use the data: `demo visualize mols`
        # See visualize_molecules.py for implementation
        MEMORY.store(table)

        # Display results
        output_table(table, pad_btm=1, return_val=False, is_data=False)
        output_text("<soft>To visualize the result, run: <cmd>demo visualize mols</cmd></soft>", pad_btm=1)
