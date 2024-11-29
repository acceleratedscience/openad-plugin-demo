# Displayed above the list of library commands in the help.
# - - -
# Keep this as short as possible, as it is also used to
# list the commands of your library, eg. `plugin demo ?`
PLUGIN_NAME = "Plugin Demo"

# Snake case name of the library, only used internally.
# - - -
# Avoid to use the word "plugin" to prevent redundancy.
PLUGIN_KEY = "the_demo"

# Namespace for your plugin commands
# - - -
# A short word that will be required in front of every command.
# Can be left blank but this is not recommended.
PLUGIN_NAMESPACE = "demo"

# Optional: A note that will display at the bottom of your command's help description.
# - - -
# This can either be a string, or a dictionary with localized strings.
CMD_NOTE = "<reverse> i </reverse> To see all available demo commands, run <cmd>demo plugin ?</cmd>"
CMD_NOTE = {
    "en": "<reset><reverse> i </reverse></reset> To see all available demo commands, run <cmd>demo plugin ?</cmd>",
    "fr": "<reset><reverse> i </reverse></reset> Pour voir toutes les commandes de démonstration disponibles, exécutez <cmd>demo plugin ?</cmd>",
    "fr_BE": "<reset><reverse> i </reverse></reset> T'veux voir toutes les commandes de démo? Tape juste <cmd>demo plugin ?</cmd> dans ta console, mon pote.",
}

# Clauses that are repeated across the descriptions of multiple commands.
CLAUSES = {
    "example": {
        "en": "[ This is a clause than can be repeated in the description of multiple commands. ]",
        "fr": "[ Ceci est la clause en français général. ]",
        "fr_BE": "[ Ceci est la clause en français belge. ]",
    }
}
