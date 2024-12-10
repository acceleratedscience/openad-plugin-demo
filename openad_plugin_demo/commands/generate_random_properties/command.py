import os
import pandas as pd

# OpenAD
from openad.smols.smol_functions import valid_identifier
from openad.helpers.spinner import spinner
from openad.helpers.general import style_bool
from openad.helpers.output import output_error, output_warning, output_text, output_success, output_table

# Plugin
from openad_grammar_def import *
from openad_plugin_demo.plugin_grammar_def import *
from openad_plugin_demo.plugin_params import PLUGIN_NAME, PLUGIN_KEY, CMD_NOTE, PLUGIN_NAMESPACE


class PluginCommand:
    """Generate random properties demo command"""

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

        # statements.append(
        #     Forward(
        #         py.Word(NAMESPACE)
        #         + test
        #         + (
        #             (molecules + molecule_identifier_list("identifiers"))
        #             | (molecule + molecule_identifier("identifier"))
        #         )
        #     )(self.parser_id)
        # )

        # # Sometimes it's more clear to create separate help entries for command variations:
        # grammar_help.append(
        #     help_dict_create(
        #         category=PLUGIN_NAME,
        #         command=f"{NAMESPACE} validate molecule|mol <molecule_identifier>",
        #         description_file=f"{self.name}/description_single.txt",
        #         note=CMD_NOTE,
        #     )
        # )
        # grammar_help.append(
        #     help_dict_create(
        #         category=PLUGIN_NAME,
        #         command=f"{NAMESPACE} validate molecules|mols [<molecule_identifier>,<molecule_identifier>,...]",
        #         description_file=f"{self.name}/description_list.txt",
        #         note=CMD_NOTE,
        #     )
        # )

    def exec_command(self, cmd_pointer, parser):
        cmd = parser.as_dict()
        # print(cmd, "\n---\n\n")

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
