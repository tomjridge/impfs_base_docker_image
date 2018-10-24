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

out="""FROM ubuntu_18.04_with_opam2_ocaml_4.06

RUN opam list
RUN sudo apt-get -y install libfuse-dev

"""

out+="RUN opam install -y "+' '.join(sorted(list(opam_deps())))+"\n"

# print(out)

# create Dockerfile ----------------------------------------------------

import pathlib
pathlib.Path("Dockerfile").write_text(out)
