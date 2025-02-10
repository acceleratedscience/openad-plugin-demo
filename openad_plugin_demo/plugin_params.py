import os
import yaml


# Load metadata from file
plugin_metadata = {}
try:
    metadata_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plugin_metadata.yaml")
    with open(metadata_file, "r", encoding="utf-8") as f:
        plugin_metadata = yaml.safe_load(f)
except Exception:  # pylint: disable=broad-except
    pass


PLUGIN_NAME = plugin_metadata.get("name")
PLUGIN_KEY = PLUGIN_NAME.lower().replace(" ", "_")
PLUGIN_NAMESPACE = plugin_metadata.get("namespace")
CLAUSES = {
    "example": {
        "en": "[ This is a clause than can be repeated in the description of multiple commands. ]",
        "fr": "[ Ceci est la clause en français général. ]",
        "fr_BE": "[ Ceci est la clause en français belge. ]",
    },
    "supported_identifiers": "Supported identifiers are SMILES, InChI, InChIKey, or name.",
}
