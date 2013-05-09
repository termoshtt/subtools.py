# coding=utf-8

def test(arg1,opt1="some"):
    print("test code.")
    print("detail of arg1")
    print("> type " + str(type(arg1)))
    print("> val  " + str(arg1))
    print("detail of opt1")
    print("> type " + str(type(opt1)))
    print("> val  " + str(opt1))

def register(subcmds):
    subcmds["test"] = {
            "func" : test,
            "args" : [{"name" : "arg1" , "help" : "argument 1", "type" : int}],
            "opts" : [{"name" : "opt1" , "help" : "option 1", "type" : str}],
            "help" : "do nothing (dummy sub command)",
        }

