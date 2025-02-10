from openad_plugin_demo.plugin_params import CLAUSES

description = f"""
Visualize one or more molecules by their identifiers by launching the OpenAD molecule viewer in an iframe (Jupyter) or your browser (terminal).

This command can also be run without identifiers as a follow-up command to the <cmd>validate molecule(s)</cmd> commands.

{CLAUSES['supported_identifiers']}


Examples:
- As a follow-up command after validating some molecule identifiers:
    <cmd>demo validate mols [Serotonin,Norepinephrine,Enkephalin,Dynorphin]</cmd>
    <cmd>demo visualize mols</cmd>
- Visualizing a single molecule by its SMILES
    <cmd>demo visualize molecule CC(=O)N1CCC2(CC1)C3=C(C=CC(=C3)C#CC4C(C(C(C(O4)CO)O)O)O)C5=C2C=C(C=C5)C#CC6C(C(C(C(O6)CO)O)O)O</cmd>
- Visualize a list of molecules defined by various types of identifiers
    <cmd>demo visualize mols ['Isoamyl acetate', C1CN2C(C1O)C(C(C2C(=O)O)O)O, PXZAWHSJYIECNQ-UHFFFAOYSA-N, InChI=1S/C20H20O13/c21-5-7-1-9(22)15(26)12(2-7)32-20-18(29)17(28)16(27)13(33-20)6-31-19(30)8-3-10(23)14(25)11(24)4-8/h1-5,13,16-18,20,22-29H,6H2]</cmd>
"""
