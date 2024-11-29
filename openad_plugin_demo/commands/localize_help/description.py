from openad.helpers.general import get_locale  # pylint: disable=import-error
from openad_plugin_demo.plugin_params import CLAUSES

# Default description - English
description = f"""This command demonstrates an alternative way to localize your command desciption in different languages, for cases where your description text has variables that need to be parsed. For example, your desciption may contain a clause that's repeated across multiple commands.

{CLAUSES["example"]["en"]}

Rather than in a text file, this desciption is stored as a formatted string inside a Python file, with the localization logic implemented in the description file itself.
"""

# French description
description_fr = f"""Description en <green>français général</green>.

{CLAUSES["example"]["fr"]}
"""

# Belgian French description
description_fr_BE = f"""Description en <yellow>français belge</yellow>.

{CLAUSES["example"]["fr_BE"]}
"""


# Select the localized description based on the user's locale
def select_localized_description():
    lang = get_locale("lang")
    region = get_locale("region")

    # Try to select the localized language + region description
    try:
        _description = eval(f"description_{lang}_{region}")  # pylint: disable=eval-used
    except Exception:  # pylint: disable=broad-except
        _description = None

    # Try to select the localized language-only description
    if not _description:
        try:
            _description = eval(f"description_{lang}")  # pylint: disable=eval-used
        except Exception:  # pylint: disable=broad-except
            _description = None

    # Fallback to the default description
    if not _description:
        _description = description

    return _description


description = select_localized_description()
