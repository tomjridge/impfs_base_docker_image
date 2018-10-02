#!/usr/bin/python3
from pathlib import Path
import importlib

# import ---------------------------------------------------------------

import sys
sys.path.append('/tmp/l/github/python_private')
from imp_shared import *
# exec(open("/tmp/l/github/python_private/imp").read())
opam_deps()

# rest -----------------------------------------------------------------

out="""FROM ubuntu_16.04_with_ocaml_4.06

RUN opam list
RUN ocamlfind list
RUN sudo apt-get -y install libfuse-dev

"""

out+="RUN opam install "+' '.join(sorted(list(opam_deps())))+"\n"

# print(out)

# create Dockerfile ----------------------------------------------------

import pathlib
pathlib.Path("Dockerfile").write_text(out)
