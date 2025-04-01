from openad_tools.locale import localize
from openad_plugin_demo.plugin_params import SNIPPETS

# Default description - English
description_en = f"""This command demonstrates an alternative way to localize your command desciption in different languages, for cases where your description text has variables that need to be parsed. For example, your desciption may contain a snippet that's repeated across multiple commands.

{SNIPPETS["example"]["en"]}

Rather than in a text file, this description is stored as a formatted string inside a Python file, with the localization logic implemented in the description file itself.
"""

# French description
description_fr = f"""Description en <green>français général</green>.

{SNIPPETS["example"]["fr"]}
"""

# Belgian French description
description_fr_BE = f"""Description en <yellow>français belge</yellow>.

{SNIPPETS["example"]["fr_BE"]}
"""


description = localize(
    {
        "en": description_en,
        "fr": description_fr,
        "fr_BE": description_fr_BE,
    }
)
