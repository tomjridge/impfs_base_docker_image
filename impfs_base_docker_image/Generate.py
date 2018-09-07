#!/usr/bin/python3
from pathlib import Path

out="""FROM ubuntu_16.04_with_ocaml_4.06

RUN opam list
RUN ocamlfind list
RUN sudo apt-get -y install libfuse-dev

"""


# impfs deps -----------------------------------------------------------

imp_deps={
    'tjr_lib': {},
    'isa_btree': {},
    'tjr_monad': {},
    'tjr_fs_shared': { 'tjr_lib' },
    'tjr_btree': { 'isa_btree', 'tjr_monad', 'tjr_fs_shared' },
    'path_resolution': { 'tjr_monad', 'tjr_fs_shared' },
    'tjr_net': {},
    'tjr_pcache': { 'tjr_btree' },
    'mini-fs': { 'path_resolution', 'tjr_net' },
    'imp_fs': { 'tjr_pcache', 'mini-fs' }
}

has_dev_branch=['tjr_btree', 'mini-fs']


# dockerfiles ----------------------------------------------------------

has_dockerfile=['tjr_lib','tjr_btree','tjr_pcache']


# travis ---------------------------------------------------------------

travis="""
a_tjr_lib/.travis.yml
c_tjr_btree/.travis.yml
d_tjr_pcache/.travis.yml
"""

# project paths --------------------------------------------------------

paths={
    'tjr_lib': 'a_tjr_lib',
    'isa_btree': 'b_isa_btree',
    'tjr_monad': 'b_tjr_monad',
    'tjr_fs_shared': 'b_tjr_fs_shared',
    'tjr_btree': 'c_tjr_btree',
    'path_resolution': 'c_path_resolution',
    'tjr_net': 'c_tjr_net',
    'tjr_pcache': 'd_tjr_pcache',
    'mini-fs': 'd_mini-fs',
    'imp_fs': 'imp_fs'
}


# opam deps ------------------------------------------------------------

deps={}
all_deps=set()
package_root_dir="/tmp/l/github"
packages_with_opam_deps=["a_tjr_lib", "b_isa_btree", "b_tjr_monad", "c_tjr_btree", "c_tjr_net", "d_mini-fs"]
for f in packages_with_opam_deps:
    deps[f]=(Path(package_root_dir) / f / "opam_depends").read_text()
    print("Dependencies of",f,": ",deps[f],"\n")
    all_deps=all_deps.union(deps[f].split(' '))

out+="RUN opam install "+' '.join(all_deps)+"\n"

# print(out)

# create Dockerfile ----------------------------------------------------

import pathlib
pathlib.Path("Dockerfile").write_text(out)
