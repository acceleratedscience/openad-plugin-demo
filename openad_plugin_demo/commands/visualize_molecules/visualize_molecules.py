import pandas as pd

# OpenAD
from openad.app.global_var_lib import MEMORY
from openad.smols.smol_functions import find_smol, clear_mws, mws_add, mws_is_empty
from openad.gui.gui_launcher import gui_init

# OpenAD tools
from openad_tools.spinner import spinner
from openad_tools.helpers import confirm_prompt
from openad_tools.output import output_error, output_text
from openad_tools.style_parser import strip_ansi


def visualize_molecules(cmd_pointer, cmd):
    """Execute the visualize molecules command"""

    # Parse identifiers from the command
    if "identifiers" in cmd:
        identifiers = cmd.get("identifiers")

    # Parse identifiers from memory
    else:
        identifiers = fetch_identifiers_from_memory()
        if not identifiers:
            output_error(
                "\n".join(
                    [
                        "No molecules found in memory",
                        "<yellow>Please re-run this command with defined molecule identifiers,",
                        "or first run the <cmd>validate molecules</cmd> command</yellow>",
                    ]
                )
            )
            return

    # Single identifier: open molecule viewer
    if len(identifiers) == 1:
        gui_init(cmd_pointer, "mol/" + identifiers[0])

    # List of identifier: Open molset viewer
    else:

        # Give user the chance to abort before we add molecules to the working set
        mws_count = len(cmd_pointer.molecule_list)
        warning_soft = "<yellow>Molecules will be added to your current working set.</yellow>"
        warning_hard = [
            f"<error>Warning: Molecules will be added to your working set and your currently stored molecules <yellow>({mws_count})</yellow> will be cleared.</error>",
            "To see your stored molecules, run <cmd>show mols</cmd>",
        ]
        output_text(warning_soft if mws_count == 0 else warning_hard)
        c_ontinue = confirm_prompt("Do you wish to continue?")
        if not c_ontinue:
            return output_error("Action aborted")

        # Clear your molecule working set
        clear_mws(cmd_pointer, force=bool(mws_count == 0))

        # Add molecule to your molecule working set
        for identifier in identifiers:
            # Start loader
            spinner.start(f"Looking up {identifier}")

            # Create molecule dict.
            # Set basic to True for basic RDKit molecule withour PubChem lookup
            smol = find_smol(cmd_pointer, identifier, basic=False)

            # Stop loader
            spinner.stop()

            # Add molecule to working set
            mws_add(cmd_pointer, smol, force=True)

        # Open your molecule working set
        gui_init(cmd_pointer, "my-mols")

        # Store the results in memory so they can be accessed by follow-up commands
        # Doesn't work yet, current Memory only supports dataframes which is not ideal here.
        # MEMORY.store(cmd_pointer.molecule_list)
        # return output_text(
        #     "\n".join(
        #         [
        #             "To save the result to your workspace, use the GUI or run follow-up commands:",
        #             "    <cmd>result save</cmd>",
        #             "    <cmd>result save as 'demo_molecules.molset.json'</cmd> <soft># Save as molset</soft>",
        #             "    <cmd>result save as 'demo_molecules.smi'</cmd> <soft># Save as list of smiles</soft>",
        #         ]
        #     ),
        #     pad_btm=1,
        # )


def fetch_identifiers_from_memory():
    """
    When no identifiers are provided, we'll look for them in the memory.

    Any command can store data into the memory, and output_table() will by default always store the data in the memory for any follow up commands.
    """

    # Preserve memory for further follow-up commands
    MEMORY.preserve()

    # If the last command returned table data with output_table(),
    # this data is stored in memory and can be retrieved with MEMORY.get()
    molecules_df = MEMORY.get()

    # Abort if no result was stored in memory
    if not isinstance(molecules_df, pd.DataFrame):
        return None

    # Extract the "identifier" field for every row in the dataframe "molecules"
    identifiers = molecules_df["Identifier"].tolist()

    # Remove invalid molecules
    identifiers = [
        identifier for i, identifier in enumerate(identifiers) if strip_ansi(molecules_df["Valid other"][i]) == "True"
    ]

    return identifiers
