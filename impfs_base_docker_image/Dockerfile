FROM ubuntu_18.04_with_ocaml_4.07.1

RUN opam list
RUN sudo apt-get -y install libfuse-dev

RUN opam install -y bos core dune extlib extunix fileutils lwt num ocamlfind ocamlfuse omd oseq ppx_bin_prot ppx_deriving_yojson yojson
