def keyword(name):
   return ["keyword", name] #rosa

def param(name):
     return ["parameter", name] #orange

def value(name):
   return ["value", name] #yellow

def func(name):
     return ["function", name] #blue

def macro(name):
   return ["macro", name] #celeste

def string(name):
   return ["string", "\"" + name + "\""] #verde

def string_f(name):
   return ["string", name]

def tag(name):
   return ["tag", name] #rosso

_import = ["keyword", "import "]
_from = ["keyword", "from "]
_def = ["keyword", "def "]
_with = ["keyword", "with "]
_as = ["keyword", "as "]
_if = ["keyword", "if "]
_elif = ["keyword", "elif "]
_else = ["keyword", "else:"]
_is = ["keyword", "is "]
_not = ["keyword", "not "]
_and = ["keyword", "and "]
_in = ["keyword", "in "]
_for = ["keyword", "for "]
_try = ["keyword", "try:"]
_except = ["keyword", "except "]
_pass = ["keyword", "pass"]
_f = ["keyword", "f"]
_return = ["keyword", "return "]
_lambda = ["keyword", "lambda "]
_None = ["value", "None"]
_True = ["value", "True"]
_at = ["at", "@"] #teal
_pip = ["keyword", "pip "]
_install = ["keyword", "install "]
