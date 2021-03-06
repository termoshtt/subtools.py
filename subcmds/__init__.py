# coding=utf-8
"""@subtools.subcmds
"""

import glob
import os.path

__all__ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
           if os.path.basename(f) != "__init__.py"]

mod_list = [__import__(mod, globals(), locals(), [], - 1) for mod in  __all__]

subcmds_dics = {}
for mod in mod_list:
    try:
        register = getattr(mod, "register")
    except:
        continue
    register(subcmds_dics)

