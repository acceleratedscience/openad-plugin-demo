import os
import pandas as pd
import pyparsing as py

# Plugin architecture
from openad.core.help import help_dict_create_v2
from openad_grammar_def import molecules, molecule_identifier_list, molecule_identifier
from openad_plugin_demo.plugin_grammar import visualize
from openad_plugin_demo.plugin_params import PLUGIN_NAME, PLUGIN_KEY, CMD_NOTE, PLUGIN_NAMESPACE

# OpenAD tools
from openad.helpers.output import output_error, output_text
from openad.helpers.general import confirm_prompt
from openad.helpers.spinner import spinner
from openad.app.global_var_lib import MEMORY
from openad.smols.smol_functions import find_smol, clear_mws, mws_add, mws_is_empty
from openad.gui.gui_launcher import gui_init


class PluginCommand:
    index: int
    name: str
    parser_id: str

    def __init__(self):
        self.index = 2
        self.name = os.path.dirname(os.path.abspath(__file__))
        self.parser_id = f"plugin_{PLUGIN_KEY}_{self.name}"

    def add_grammar(self, statements: list, grammar_help: list):
        """Create the required command grammar & documentation"""

        # Command definition
        statements.append(
            py.Forward(
                py.Word(PLUGIN_NAMESPACE)
                + visualize
                + molecules
                + py.Optional(molecule_identifier_list("identifiers") | molecule_identifier("identifier"))
            )(self.parser_id)
        )

        # Command help
        # - - -
        # Add 3 separate help entries for the 3 command variations:
        # 1. Follow up command to `validate mols`
        grammar_help.append(
            help_dict_create_v2(
                category=PLUGIN_NAME,
                command=f"  -> {PLUGIN_NAMESPACE} visualize molecules|mols",
                description_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "description.txt"),
                note=CMD_NOTE,
            )
        )
        # 2. Visualize a list of molecules
        grammar_help.append(
            help_dict_create_v2(
                category=PLUGIN_NAME,
                command=f"{PLUGIN_NAMESPACE} visualize molecules|mols [<molecule_identifier>,<molecule_identifier>,...]",
                description_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "description.txt"),
                note=CMD_NOTE,
            )
        )
        # 2. Visualize an individual molecule
        grammar_help.append(
            help_dict_create_v2(
                category=PLUGIN_NAME,
                command=f"{PLUGIN_NAMESPACE} visualize molecule|mol <molecule_identifier>",
                description_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "description.txt"),
                note=CMD_NOTE,
            )
        )

    def exec_command(self, cmd_pointer, parser):
        """Execute the command"""

        # Preserve memory for further follow-up commands
        MEMORY.preserve()

        # If the last command returned table data with output_table(),
        # this data is stored in memory and can be retrieved with MEMORY.get()
        molecules_df = MEMORY.get()

        # Abort if no result was stored in memory
        if not isinstance(molecules_df, pd.DataFrame):
            return output_error("No molecules found in memory")

        # Extract the "identifier" field for every row in the dataframe "molecules"
        identifiers = molecules_df["Identifier"].tolist()

        # Single identifier: open molecule viewer
        if len(identifiers) == 1:
            gui_init(cmd_pointer, "mol/" + identifiers[0])

        # List of identifier: Open molset viewer
        else:
            # Clear your molecule working set
            clear_mws(cmd_pointer, force=False)

            # Give user the chance to abort before we add molecules to the working set
            c_ontinue = (
                True
                if mws_is_empty(cmd_pointer)
                else confirm_prompt("Molecules will be added to your current working set. Do you want to continue?")
            )
            if not c_ontinue:
                return output_error("Action aborted")

            # Add molecule to your molecule working set
            for identifier in identifiers:
                # Start loader
                spinner.start(f"Looking up {identifier}")

                # Create molecule dict.
                # Set basic to True for basic RDKit molecule withour PubChem lookup
                smol = find_smol(cmd_pointer, identifier, basic=False)

                # Stop loader
                spinner.stop()

                mws_add(cmd_pointer, smol, force=True)

            # Open your molecule working set
            gui_init(cmd_pointer, "my-mols")

            return output_text(
                "\n".join(
                    [
                        "To save the result to your workspace, use the GUI or run follow-up commands:",
                        "    <cmd>result save</cmd>",
                        "    <cmd>result save as 'demo_molecules.molset.json'</cmd> <soft># Save as molset</soft>",
                        "    <cmd>result save as 'demo_molecules.smi'</cmd> <soft># Save as list of smiles</soft>",
                    ]
                ),
                pad_btm=1,
            )
