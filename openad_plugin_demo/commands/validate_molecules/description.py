from openad_plugin_demo.plugin_params import SNIPPETS

description = f"""
A demo on how to capture and validate molecule input in a command.

{SNIPPETS['supported_identifiers']}


Examples:
- <cmd>demo validate mol nanoputian</cmd>
- <cmd>demo validate molecule CC1=CC(=O)C=C(C1(C)C)C</cmd>
- <cmd>demo validate mols [nanoputian, dopamine, invalid_molecule]</cmd>
- <cmd>demo validate molecules [CC1=CC(=O)C=C(C1(C)C)C, InChI=1S/C12H7Cl3/c13-8-5-6-12(15)10(7-8)9-3-1-2-4-11(9)14/h1-7H, RWCCWEUUXYIKHB-UHFFFAOYSA-N]</cmd>
"""
