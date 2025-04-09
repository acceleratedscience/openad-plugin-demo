import openad_tools.grammar_def as gd

avail_defs = [df for df in gd.__dict__ if not df.startswith("_") and df != "py"]
avail_defs_str = "- " + "\n- ".join(avail_defs) + ""


def generate_description():
    """Command description and instructions"""

    # Instructions
    instructions = "\n".join(
        [
            "This command is to demonstrate the pyparsing definitions",
            "available to you via the <cmd>openad_tools</cmd> library.",
        ]
    )

    # Examples
    examples = "\n".join(
        [
            "<h1>Examples</h1>",
            #
            #
            # String definitions
            "",
            "<yellow>String definitions:</yellow>",
            "- Catch any number of words containing any character",
            "  <cmd>demo pp <underline>str_catchall</underline> foo bar baz hello@world.com '#$@%' \"A~B\"??!!</cmd>",
            "",
            "- Catch a string containing only alphanumerical characters plus - and _",
            "  <cmd>demo pp <underline>str_strict</underline> hello_world</cmd>",
            "  <cmd>demo pp <underline>str_strict</underline> hello@world</cmd> <soft>// Will fail</soft>",
            "",
            "- Catch a string containing any character",
            "  <cmd>demo pp <underline>str_any</underline> hello@world</cmd>",
            "  <cmd>demo pp <underline>str_any</underline> hello world</cmd> <soft>// Will fail</soft>",
            "",
            "- Catch a suoted string",
            "  <cmd>demo pp <underline>str_quoted</underline> 'hello world'</cmd>",
            "",
            "- Catch a alphanumerical string or quoted string containing any character",
            "  <cmd>demo pp <underline>str_opt_quoted</underline> hello_world</cmd>",
            "  <cmd>demo pp <underline>str_opt_quoted</underline> 'hello world'</cmd>",
            "",
            "- Catch a list of quoted strings",
            "  <cmd>demo pp <underline>list_quoted</underline> ['foo','bar','b@z','#$%!']</cmd>",
            "",
            # Molecules
            "<yellow>Molecules:</yellow>",
            "- Catch the word 'molecule' or 'mol'",
            "  <cmd>demo pp <underline>molecule</underline> molecule</cmd>",
            "  <cmd>demo pp <underline>molecule</underline> mol</cmd>",
            "",
            "- Catch the word 'molecules' or 'mols'",
            "  <cmd>demo pp <underline>molecules</underline> molecules</cmd>",
            "  <cmd>demo pp <underline>molecules</underline> mols</cmd>",
            "",
            "- Catch the words 'molecule' / 'mol' / 'molecules' / 'mols' all at once",
            "  <cmd>demo pp <underline>molecule_s</underline> molecule</cmd>",
            "  <cmd>demo pp <underline>molecule_s</underline> molecules</cmd>",
            "  <cmd>demo pp <underline>molecule_s</underline> mol</cmd>",
            "  <cmd>demo pp <underline>molecule_s</underline> mols</cmd>",
            "",
            "- Catch a molecule identifier",
            "  <cmd>demo pp <underline>molecule_identifier</underline> NC[C@H](O)c1ccc(O)c(O)c1</cmd>",
            "  <cmd>demo pp <underline>molecule_identifier</underline> dopamine</cmd>",
            "  <cmd>demo pp <underline>molecule_identifier</underline> InChI=1S/C7H16NO2/c1-7(9)10-6-5-8(2,3)4/h5-6H2,1-4H3/q+1</cmd>",
            "",
            "- Catch a list of molecule identifiers",
            "  <cmd>demo pp <underline>molecule_identifier_list</underline> [NC[C@H](O)c1ccc(O)c(O)c1,NCCc1c[nH]c2ccc(O)cc12,CC(=O)OCC[N+](C)(C)C]</cmd>",
            "",
            "- Catch both a single or a list of molecule identifiers",
            "  <cmd>demo pp <underline>molecule_identifier_s</underline> NC[C@H](O)c1ccc(O)c(O)c1</cmd>",
            "  <cmd>demo pp <underline>molecule_identifier_s</underline> [NC[C@H](O)c1ccc(O)c(O)c1,NCCc1c[nH]c2ccc(O)cc12,CC(=O)OCC[N+](C)(C)C]</cmd>",
            "",
            "- Catch the @mws keyword to identify the molecule working set",
            "  <cmd>demo pp <underline>molecule_working_set</underline> @mws</cmd>",
        ]
    )

    # Available definitions
    avail_defs_str_title = "\n\n\n<h1>Available definitions</h1>\n" + avail_defs_str

    return "\n".join([instructions + avail_defs_str_title + "\n\n\n" + examples])


description = generate_description()
