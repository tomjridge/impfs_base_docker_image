# FIXME maybe make this publicly available so others can use for eg travis builds etc


# This is the base docker image from which we build everything else

# NOTE maybe add a "RUN echo ..." to force a rebuild, or --no-cache

# FROM ocaml/opam:ubuntu - latest doesn't work due to problems with ppx_deriving deps
# 17.04 doesn't work due to missing archives at ubuntu? or stale packages info?

# FIXME following is a bit worrysome since it doesn't update from the web opam repo https://github.com/ocaml-attic/opam-dockerfiles/blob/ubuntu-16.04_ocaml-4.04.2/Dockerfile
FROM ocaml/opam:ubuntu-16.04_ocaml-4.04.2
# RUN apt-get -y update

RUN opam list
RUN opam update
RUN opam install batteries extunix
RUN opam install ppx_deriving_yojson extlib core ppx_bin_prot ocaml-compiler-libs lwt
RUN opam list
RUN ocamlfind list


# for tjr_lib
RUN opam install core_kernel ppx_deriving_yojson rresult bos fileutils omd

# for mini-fs
RUN sudo apt-get -y install libfuse-dev
RUN opam install ocamlfuse ppx_bin_prot 


# export NAME=impfs_base_docker_image
# docker build -t $NAME .
# docker run -ti $NAME bash
