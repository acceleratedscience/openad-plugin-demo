import os
import pyparsing as py

# OpenAD
from openad.core.help import help_dict_create_v2

# OpenAD tools
from openad_tools.output import output_error, output_warning, output_text, output_success, output_table
from openad_tools.helpers import description_txt

# Plugin
from openad_plugin_demo.plugin_grammar_def import hello, world  # <-- UPDATE
from openad_plugin_demo.plugin_params import PLUGIN_NAME, PLUGIN_KEY, PLUGIN_NAMESPACE  # <-- UPDATE


class PluginCommand:
    """Hello world demo command"""

    category: str
    index: int
    name: str
    parser_id: str

    def __init__(self):
        self.category = "Intro"  # <-- EDIT: Category under which the command will be listed in help
        self.index = 0  # <-- EDIT: Order in which this command will be listed in help, relative to the categoryy
        self.name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
        self.parser_id = f"plugin_{PLUGIN_KEY}_{self.name}"

    def add_grammar(self, statements: list, grammar_help: list):
        """Create the command definition & documentation"""

        # Command definition
        statements.append(py.Forward(py.CaselessKeyword(PLUGIN_NAMESPACE) + hello + world)(self.parser_id))  # <-- EDIT

        # Command help
        grammar_help.append(
            help_dict_create_v2(
                plugin_name=PLUGIN_NAME,
                plugin_namespace=PLUGIN_NAMESPACE,
                category=self.category,
                command=f"{PLUGIN_NAMESPACE} hello world",  # <-- EDIT
                description_file=description_txt(__file__),
            )
        )

    def exec_command(self, cmd_pointer, parser):
        """Execute the command"""

        cmd = parser.as_dict()
        # print(cmd)

        globe = """
          ________
      ,o88~~88888888o,
    ,~~?8P  88888     8,
   d  d88 d88 d8_88     b
  d  d888888888          b
  8,?88888888  d8.b o.   8
  8~88888888~ ~^8888\ db 8
  ?  888888          ,888P
   ?  `8888b,_      d888P
    `   8888888b   ,888'
      ~-?8888888 _.P-~
           ~~~~~~
"""

        return output_text(f"<yellow>Hello to you too.</yellow>\n- The world\n\n<cyan>{globe}</cyan>", pad=2, edge=True)
