FROM ubuntu_18.04_with_opam2_ocaml_4.06

RUN opam list
RUN sudo apt-get -y install libfuse-dev

RUN opam install -y bos core dune extlib extunix fileutils lwt num ocamlfind ocamlfuse omd ppx_bin_prot ppx_deriving_yojson yojson
