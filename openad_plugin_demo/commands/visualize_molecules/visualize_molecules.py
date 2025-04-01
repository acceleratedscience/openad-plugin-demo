import pandas as pd

# OpenAD
from openad.app.global_var_lib import MEMORY
from openad.smols.smol_functions import find_smol, clear_mws, mws_add
from openad.gui.gui_launcher import gui_init

# OpenAD tools
from openad_tools.helpers import confirm_prompt
from openad_tools.output import output_error, output_text
from openad_tools.style_parser import strip_ansi


def visualize_molecules(cmd_pointer, cmd):
    """Execute the visualize molecules command"""

    # 1. Parse identifiers
    # - - -

    # From the command
    # Note: if no identifiers are passed, the 'basic' clause will
    # be parsed as an identifier, so we have to check for this
    if "identifiers" in cmd and cmd.get("identifiers")[0] != "basic":
        identifiers = cmd.get("identifiers")

    # From memory
    else:
        identifiers = fetch_identifiers_from_memory()

        # No identifiers provided, abort
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

    # 2. Process identifiers
    # - - -

    # Single identifier: open molecule viewer
    if len(identifiers) == 1:
        gui_init(cmd_pointer, "mol/" + identifiers[0])

    # List of identifier: open molset viewer
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

        # Clear your molecule working set,
        # skip confirmation since we already asked the user
        clear_mws(cmd_pointer, force=True)

        # Add molecule to your molecule working set
        basic = "basic" in cmd or (cmd.get("identifiers") and "basic" in cmd.get("identifiers"))
        for identifier in identifiers:
            # Create molecule dictionary:
            # - basic = create with RDKit (fast, but only works with SMILES and InChI)
            # - default = Fetch data from PubChem (slow)
            smol = find_smol(cmd_pointer, identifier, basic=basic, show_spinner=True)

            # Add molecule to working set
            mws_add(cmd_pointer, smol, force=True)

        # Open your molecule working set
        gui_init(cmd_pointer, "my-mols")


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
