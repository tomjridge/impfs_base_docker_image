FROM ubuntu_16.04_with_ocaml_4.06

RUN opam list
RUN ocamlfind list
RUN sudo apt-get -y install libfuse-dev

RUN opam install num ocamlfuse extlib extunix bos omd yojson ppx_bin_prot ocamlfind core ppx_deriving_yojson lwt fileutils dune
