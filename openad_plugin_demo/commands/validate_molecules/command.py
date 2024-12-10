import os
import pandas as pd
import pyparsing as py

# OpenAD
from openad.core.help import help_dict_create_v2
from openad.smols.smol_functions import valid_identifier
from openad.helpers.output import output_table
from openad.helpers.general import style_bool
from openad.helpers.spinner import spinner

# Plugin
from openad_grammar_def import molecule, molecules, molecule_identifier, molecule_identifier_list
from openad_plugin_demo.plugin_grammar_def import validate
from openad_plugin_demo.plugin_params import PLUGIN_NAME, PLUGIN_KEY, CMD_NOTE, PLUGIN_NAMESPACE


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

        statements.append(
            py.Forward(
                py.Word(PLUGIN_NAMESPACE)
                + validate
                + (
                    (molecules + molecule_identifier_list("identifiers"))
                    | (molecule + molecule_identifier("identifier"))
                )
            )(self.parser_id)
        )

        # Sometimes it's more clear to create separate help entries for command variations:
        grammar_help.append(
            help_dict_create_v2(
                plugin_name=PLUGIN_NAME,
                plugin_namespace=PLUGIN_NAMESPACE,
                category=self.category,
                command=[
                    f"{PLUGIN_NAMESPACE} validate molecule|mol <molecule_identifier>",
                    f"{PLUGIN_NAMESPACE} validate molecules|mols [<molecule_identifier>,<molecule_identifier>,...]",
                ],
                description_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "description_single.txt"),
                note=CMD_NOTE,
            )
        )

    def exec_command(self, cmd_pointer, parser):
        """Execute the command"""

        cmd = parser.as_dict()

        # Start loader
        spinner.start("Validating")

        # Parse list of identifiers
        identifiers = [cmd["identifier"]] if "identifier" in cmd else cmd["identifiers"]

        # Validate identifiers and return table
        table = []
        for identifier in identifiers:
            spinner.start(f"Validating {identifier}")
            table.append(
                {
                    "Identifier": identifier,
                    "valid InChI/SMILES": style_bool(valid_identifier(identifier)),
                    "valid other": style_bool(valid_identifier(identifier, rich=True)),
                }
            )
        table = pd.DataFrame(table)

        # Stop loader
        spinner.stop()

        return output_table(table, pad=1)
