#!/usr/bin/python2
# coding=utf-8

import argparse
import os.path
import sys

sys.path = [sys.path[0]] + [os.path.join(os.path.dirname(__file__), "..")] + sys.path[1:]
import subcmds
sys.path = [sys.path[0]] + sys.path[2:]

def main():
    parser =  argparse.ArgumentParser(description='interface generater for small python functions')
    sub_psr = parser.add_subparsers(help="valid subcommands")

    for subcmd in subcmds.subcmds_dics:
        dic = subcmds.subcmds_dics[subcmd]
        psr = sub_psr.add_parser(subcmd,help=dic["help"])
        for arg in dic["args"]:
            psr.add_argument(arg["name"],help=arg["help"])
        psr.set_defaults(name=subcmd)
        psr.set_defaults(dic=dic)

    sys_args = parser.parse_args()

    func = sys_args.dic["func"]
    args = []
    for arg in sys_args.dic["args"]:
        val = vars(sys_args)[arg["name"]]
        if "type" in arg:
            val = arg["type"](val)
        args.append(val)
    func(*args)

if __name__ == "__main__":
    main()
