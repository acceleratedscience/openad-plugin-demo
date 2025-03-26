"""
Centralized Pyparsing grammar definitions

You can also define these in the command file, but if you will repeat
grammar definitions across multiple commands, it's better to centralize them.
"""

import pyparsing as py

# Hello world
hello = py.CaselessKeyword("hello")
world = py.CaselessKeyword("world")

# Hello advanced
subject = py.Word(py.alphanums + "_-~.:;?/|\\+<=>*@#$%&")
subject_list = py.delimitedList(subject, delim=",")

# Localize
localize = py.CaselessKeyword("localize") | py.CaselessKeyword("localise")
a = py.CaselessKeyword("a")
b = py.CaselessKeyword("b")

# Validate molecules
validate = py.CaselessKeyword("validate")
result = py.CaselessKeyword("result")

# Visualize molecules
visualize = py.CaselessKeyword("visualize") | py.CaselessKeyword("vizualize")
clause_basic = py.Optional(py.CaselessKeyword("basic"))("basic")
