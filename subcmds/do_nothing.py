# coding=utf-8

def do_nothing(arg1):
    print("this is a small sample.")
    print("type of arg1 : " + str(type(arg1)))

def register(subcmds):
    subcmds["do_nothing"] = {
            "func" : do_nothing,
            "args" : [{"name" : "arg1" , "help" : "argument 1", "type" : int}],
            "help" : "do nothing (dummy sub command)",
        }

