import pyparsing as py

hello = py.CaselessKeyword("hello")
subject = py.Word(py.alphanums + "_-~.:;?/|\\+<=>*@#$%&")
subject_list = py.delimitedList(subject, delim=",")
localize = py.CaselessKeyword("localize") | py.CaselessKeyword("localise")
a = py.CaselessKeyword("a")
b = py.CaselessKeyword("b")

validate = py.CaselessKeyword("validate")
result = py.CaselessKeyword("result")
visualize = py.CaselessKeyword("visualize") | py.CaselessKeyword("vizualize")
