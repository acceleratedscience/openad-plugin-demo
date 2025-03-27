import os
import pyparsing as py

# OpenAD
from openad.core.help import help_dict_create_v2

# OpenAD tools
from openad_tools.output import output_error, output_warning, output_text, output_success, output_table
from openad_tools.helpers import description_txt

# Plugin
from openad_plugin_demo.plugin_grammar_def import hello, world
from openad_plugin_demo.plugin_params import PLUGIN_NAME, PLUGIN_KEY, PLUGIN_NAMESPACE


class PluginCommand:
    """Hello world demo command"""

    category: str  # Category of command
    index: int  # Order in help
    name: str  # Name of command = command dir name
    parser_id: str  # Internal unique identifier

    def __init__(self):
        self.category = "_Intro"
        self.index = 0
        self.name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
        self.parser_id = f"plugin_{PLUGIN_KEY}_{self.name}"

    def add_grammar(self, statements: list, grammar_help: list):
        """Create the command definition & documentation"""

        # Command definition
        statements.append(py.Forward(py.CaselessKeyword(PLUGIN_NAMESPACE) + hello + world)(self.parser_id))

        # Command help
        grammar_help.append(
            help_dict_create_v2(
                plugin_name=PLUGIN_NAME,
                plugin_namespace=PLUGIN_NAMESPACE,
                category=self.category,
                command=f"{PLUGIN_NAMESPACE} hello world",
                description_file=description_txt(__file__),
            )
        )

    def exec_command(self, cmd_pointer, parser):
        """Execute the command"""

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
