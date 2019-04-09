FROM ubuntu:18.04

# ubuntu extra packages for ocaml build --------------------------------

RUN apt-get -y update
RUN apt-get install -y git make
RUN apt-get install -y curl
RUN apt-get install -y gcc
RUN apt-get install -y bzip2
RUN apt-get install -y wget
RUN apt-get install -y sudo
RUN apt-get install -y unzip m4

RUN apt-get install -y time
RUN apt-get install -y rsync bubblewrap

# from https://github.com/avsm/opam2-ppa/blob/master/scripts/Dockerfile.base ; needed?
# RUN apt-get -y install build-essential ocaml-native-compilers devscripts dh-make


# setup opam user --------------------------------------------------------

# taken from https://github.com/ocaml-attic/opam-dockerfiles/blob/ubuntu-16.04_ocaml-4.04.2/Dockerfile

LABEL distro_style="apt" distro="ubuntu" distro_long="ubuntu-18.04" arch="x86_64" ocaml_version="4.06.1" opam_version="2" operatingsystem="linux"
RUN apt-get -y update && \
  DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \
  DEBIAN_FRONTEND=noninteractive apt-get -y install aspcud && \
  mkdir -p /etc/sudoers.d && \
  echo 'opam ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/opam && \
  chmod 440 /etc/sudoers.d/opam && \
  chown root:root /etc/sudoers.d/opam && \
  adduser --disabled-password --gecos '' opam && \
  passwd -l opam && \
  chown -R opam:opam /home/opam
USER opam
ENV HOME /home/opam
WORKDIR /home/opam

RUN mkdir .ssh && \
  chmod 700 .ssh && \
  git config --global user.email "docker@example.com" && \
  git config --global user.name "Docker CI" 


# opam repository ------------------------------------------------------

# NOTE tag faebdfd is just a reasonably recent (today!) 
RUN \
  git clone git://github.com/ocaml/opam-repository && \
  cd opam-repository && \
  git reset --hard faebdfd


# opam exe from web not apt -----------------------------------------------

# NOTE the github download link is redirected; so just place in my web
# directory and download from there

RUN curl https://www.cs.le.ac.uk/people/tr61/opam-2.0.3-x86_64-linux >opam
RUN chmod u+x ./opam
RUN ./opam --help
RUN sudo mv ./opam /bin


RUN \
  opam init -a --disable-sandboxing -y --compiler 4.06.1 /home/opam/opam-repository && \
  opam install -y depext travis-opam

RUN opam install ocamlfind dune

# some bash setup ------------------------------------------------------

RUN sudo rm -f /bin/sh && sudo ln -sf /bin/bash /bin/sh
RUN echo "test -r /home/opam/.opam/opam-init/init.sh && . /home/opam/.opam/opam-init/init.sh > /dev/null 2> /dev/null || true" >> ~/.bashrc
RUN bash -i -c "ocamlfind list"


ENTRYPOINT [ "opam", "config", "exec", "--" ]
CMD [ "bash" ]


