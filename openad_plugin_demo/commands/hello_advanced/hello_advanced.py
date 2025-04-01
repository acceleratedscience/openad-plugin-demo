import datetime
import pandas as pd

# OpenAD tools
from openad_tools.output import output_error, output_warning, output_text, output_success, output_table

planet_info = {
    "mercury": {"distance": 57.9, "population": 0},
    "venus": {"distance": 108.2, "population": 0},
    "earth": {"distance": 149.6, "population": 8.062},
    "mars": {"distance": 227.9, "population": 0},
    "jupiter": {"distance": 778.6, "population": 0},
    "saturn": {"distance": 1433.5, "population": 0},
    "uranus": {"distance": 2872.5, "population": 0},
    "neptune": {"distance": 4495.1, "population": 0},
    "pluto": {"distance": 5906, "population": 0},
}


def hello_advanced(cmd_pointer, cmd):
    """Execute the hello advanced command"""

    # Parse subject(s)
    the_subject = cmd["subject"]
    the_subject = the_subject[0].lower() if isinstance(the_subject, list) and len(the_subject) == 1 else the_subject

    # 1. Subject inside solar system
    if the_subject in ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]:
        # Delay warning
        if the_subject != "earth":
            output_warning(
                [f"Warning: {the_subject} is another planet", "Greeting will take time to be relayed"],
                return_val=False,
            )

        # Assemble planet information
        info_print = [
            "<h1>Planet Information</h1>",
            f'<green>Distance from sun:</green> {planet_info[the_subject]["distance"]} million km',
            (
                "<green>Population:</green> "
                + (
                    f"{planet_info[the_subject]['population']} billion"
                    if planet_info[the_subject]["population"] > 0
                    else "0"
                )
            ),
        ]
        output_text(info_print, pad=1, return_val=False)

        # Return data
        planet_data = pd.DataFrame(
            {
                "Planet": [the_subject],
                "Distance (km)": ([planet_info[the_subject]["distance"] * 1000000]),
                "Population": ([planet_info[the_subject]["population"] * 1000000000]),
            }
        )
        return output_table(planet_data, pad=1)

    # 2. Subject out of scope
    if the_subject in ["universe", "cosmos", "galaxy"]:
        return output_error("Greeting the entire universe is not yet supported", pad_btm=1)

    # 3. All other subjects
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
