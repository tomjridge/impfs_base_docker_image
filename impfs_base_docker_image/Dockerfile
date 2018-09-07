FROM ubuntu_16.04_with_ocaml_4.06

RUN opam list
RUN ocamlfind list
RUN sudo apt-get -y install libfuse-dev

RUN opam install yojson extlib core lwt fileutils omd ppx_bin_prot ppx_deriving_yojson ocamlfind ocamlfuse bos
