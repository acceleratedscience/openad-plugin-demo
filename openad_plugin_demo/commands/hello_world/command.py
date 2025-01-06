import os
import datetime
import pandas as pd
import pyparsing as py

# OpenAD
from openad.core.help import help_dict_create_v2
from openad.helpers.output import output_error, output_warning, output_text, output_success, output_table

# Plugin
from openad_plugin_demo.plugin_grammar_def import hello, subject, subject_list
from openad_plugin_demo.plugin_params import PLUGIN_NAME, PLUGIN_KEY, PLUGIN_NAMESPACE
from openad_plugin_demo.commands.hello_world.ascii_art import globe


class PluginCommand:
    """Hello world demo command"""

    category: str  # Category of command
    index: int  # Order in help
    name: str  # Name of command = command dir name
    parser_id: str  # Internal unique identifier

    def __init__(self):
        self.category = "Intro"
        self.index = 0
        self.name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
        self.parser_id = f"plugin_{PLUGIN_KEY}_{self.name}"

    def add_grammar(self, statements: list, grammar_help: list):
        """Create the command definition & documentation"""

        # Command definition
        statements.append(
            py.Forward(py.CaselessKeyword(PLUGIN_NAMESPACE) + hello + (subject_list | subject)("subject"))(
                self.parser_id
            )
        )

        # Command help
        grammar_help.append(
            help_dict_create_v2(
                plugin_name=PLUGIN_NAME,
                plugin_namespace=PLUGIN_NAMESPACE,
                category=self.category,
                command=f"{PLUGIN_NAMESPACE} hello world | <planet_name> | <subject> | <subject>,<subject>,...",
                description_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "description.txt"),
            )
        )

    def exec_command(self, cmd_pointer, parser):
        """Execute the command"""

        cmd = parser.as_dict()

        # Parse subject(s)
        the_subject = cmd["subject"]
        the_subject = the_subject[0].lower() if isinstance(the_subject, list) and len(the_subject) == 1 else the_subject

        # Subject "world"
        if the_subject in ["world", "earth"]:
            return output_text(
                f"<yellow>Hello to you too.</yellow>\n- The world\n\n<cyan>{globe}</cyan>", pad=2, edge=True
            )

        # Subject inside solar system
        if the_subject in ["mercury", "venus", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]:
            return output_warning(
                [f"Warning: {the_subject} is another planet", "Greeting will take time to be relayed"], pad_btm=1
            )

        # Subject universe
        if the_subject in ["universe", "cosmos", "galaxy"]:
            return output_error("Greeting the entire universe is not yet supported", pad_btm=1)

        # Multiple subjects
        if isinstance(the_subject, list):
            all_subjects = the_subject
            result_set = []
            for subj in all_subjects:
                subj = subj.lower()
                result_set.append(
                    {
                        "Name": subj,
                        "Greeting date": datetime.datetime.now().strftime("%b %2, %Y"),
                        "Greeting time": datetime.datetime.now().strftime("%H:%M:%S"),
                    }
                )
            result_set = pd.DataFrame(result_set)
            output_text("<h1>List of greeted subjects</h1>\n", pad=1, return_val=False)
            return output_table(result_set, pad_btm=1)

        # Single subject
        else:
            return output_success(f"You said hello to {the_subject}.", pad_btm=1)
