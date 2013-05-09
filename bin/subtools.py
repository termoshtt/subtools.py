#!/usr/bin/python2
# coding=utf-8

import argparse
import os.path
import sys
import ConfigParser

sys.path = [sys.path[0]] + [os.path.join(os.path.dirname(__file__), "..")] + sys.path[1:]
import subcmds
sys.path = [sys.path[0]] + sys.path[2:]

def main():
    # set options
    parser =  argparse.ArgumentParser(description='interface generater for small python functions')
    parser.add_argument("-c","--configure",dest="cfg_filename",default="~/.subtoolsrc",help="specify configure file")
    sub_psr = parser.add_subparsers(help="auto-generated valid subcommands")
    for subcmd in subcmds.subcmds_dics:
        dic = subcmds.subcmds_dics[subcmd]
        psr = sub_psr.add_parser(subcmd,help=dic["help"])
        for arg in dic["args"]:
            psr.add_argument(arg["name"],help=arg["help"])
        for opt in dic["opts"]:
            psr.add_argument("--"+opt["name"],help=opt["help"])
        psr.set_defaults(name=subcmd)
        psr.set_defaults(dic=dic)
    sys_args = parser.parse_args()

    # args
    args = []
    for arg in sys_args.dic["args"]:
        val = vars(sys_args)[arg["name"]]
        if "type" in arg:
            val = arg["type"](val)
        args.append(val)

    # options
    opts = {}
    cfg = ConfigParser.SafeConfigParser()
    cfg_fn = os.path.expanduser(sys_args.cfg_filename)
    if not os.path.exists(cfg_fn):
        print("configure file does not found")
    else:
        cfg.read(cfg_fn)
        if cfg.has_section(sys_args.name):
            for opt in cfg.options(sys_args.name):
                opts[opt] = cfg.get(sys_args.name,opt)
    if "opt" in  sys_args.dic
        for opt in sys_args.dic["opts"]:
            val = vars(sys_args)[opt["name"]]
            if not val:
                continue
            if "type" in opt:
                val = opt["type"](val)
            opts[opt["name"]] = val

    # execute
    func = sys_args.dic["func"]
    func(*args,**opts)

if __name__ == "__main__":
    main()
