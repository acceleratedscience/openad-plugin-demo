import os
import pyparsing as py

# OpenAD
from openad.core.help import help_dict_create_v2

# OpenAD tools
from openad_tools.output import output_error, output_warning, output_text, output_success, output_table
from openad_tools.helpers import description_txt
from openad_tools.ascii_type import ascii_type

# Plugin
from openad_plugin_demo.plugin_grammar_def import output, styles
from openad_plugin_demo.plugin_params import PLUGIN_NAME, PLUGIN_KEY, PLUGIN_NAMESPACE


class PluginCommand:
    """Hello world demo command"""

    category: str
    index: int
    name: str
    parser_id: str

    def __init__(self):
        self.category = "Intro"
        self.index = 0
        self.name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
        self.parser_id = f"plugin_{PLUGIN_KEY}_{self.name}"

    def add_grammar(self, statements: list, grammar_help: list):
        """Create the command definition & documentation"""

        # Command definition
        statements.append(py.Forward(py.CaselessKeyword(PLUGIN_NAMESPACE) + output + styles)(self.parser_id))

        # Command help
        grammar_help.append(
            help_dict_create_v2(
                plugin_name=PLUGIN_NAME,
                plugin_namespace=PLUGIN_NAMESPACE,
                category=self.category,
                command=f"{PLUGIN_NAMESPACE} output styles",
                description_file=description_txt(__file__),
            )
        )

    def exec_command(self, cmd_pointer, parser):
        """Execute the command"""
        sep = "<soft>----------------------</soft>"

        output_text("Simple print", return_val=False)
        output_success("I'm a success message in green", return_val=False)
        output_error("I'm an error in red", return_val=False)
        output_text(
            "We have XML style tags for <red>red</red>, <green>green</green>, <blue>blue</blue>, <yellow>yellow</yellow>, <cyan>cyan</cyan>, <magenta>magenta</magenta> and also <soft>soft</soft> and <bold>bold</bold>.",
            return_val=False,
        )
        output_text(
            "Whenever describing commands, we use special <cmd>cmd</cmd> tag, which displays the command in cyan,\nbut also automatically styles command parameters. For example: <cmd>demo hello <subject></cmd>",
            return_val=False,
        )
        output_text(sep)
        output_text("I have one empty line on top", return_val=False, pad_top=1)
        output_text(sep)
        output_text("I have one empty line below", return_val=False, pad_btm=1)
        output_text(sep)
        output_text("I have one empty line on top and below", return_val=False, pad=1)
        output_text(sep)
        output_text("I have three empty lines on top and below", return_val=False, pad=3)
        output_text(sep)
        output_text(
            "<h1>This is a Header</h1>\nBelow some regular text.\nDisplayed inset with an edge.",
            return_val=False,
            pad=1,
            edge=True,
        )
        lipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut tortor gravida, placerat urna sed, lobortis tortor. Etiam tempor laoreet quam, sit amet ultrices nulla lacinia ac. Curabitur fringilla fringilla rutrum. Maecenas tincidunt ex massa, non molestie libero convallis eget. Vestibulum eu nisi ultrices, ultricies massa non, laoreet leo. Cras porttitor ante lacus, vitae pretium libero dictum sit amet. Pellentesque ac lorem ut ante imperdiet placerat sit amet vel metus. Curabitur ut leo lobortis, eleifend erat sed, ultrices est. Maecenas venenatis commodo erat, in scelerisque dolor finibus eu. Pellentesque sagittis eros ut ultrices euismod. Mauris vel volutpat ante, in convallis nisl. Proin hendrerit facilisis commodo. Nullam sagittis nisi risus, id porta massa lobortis quis. Morbi varius sapien ac scelerisque auctor. Fusce blandit non erat vel mollis. Duis eu lacus lacus. Duis mauris tortor, consectetur ac ornare at, consectetur at dolor. Nunc porttitor enim ac mauris pulvinar, at suscipit ex lobortis. Quisque eleifend nisi at massa rutrum bibendum non id purus. Praesent id condimentum mauris, sed luctus elit. Morbi molestie orci at rutrum ullamcorper."""
        output_text(
            " ".join(
                [
                    "<yellow>By default, text in the terminal wraps at 150 characters or the terminal width, whicever is smallest.</yellow>",
                    lipsum,
                ]
            ),
            return_val=False,
            pad=1,
        )
        output_text(
            " ".join(
                [
                    "<yellow>You can disable wrapping.</yellow>",
                    lipsum,
                ]
            ),
            return_val=False,
            nowrap=True,
            pad=1,
        )
        output_text(
            " ".join(
                [
                    "<yellow>You can also set a custum width</yellow>",
                    lipsum,
                ]
            ),
            return_val=False,
            width=50,
            pad=1,
        )
        output_text("<soft>Also this:</soft>\n" + ascii_type("hello world"), return_val=False, pad=1)
