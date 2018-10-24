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

# begin section --------------------------------------------------------

#  git clone -b 1.2 git://github.com/ocaml/opam /tmp/opam && \
#  sh -c "cd /tmp/opam && make cold && make install && echo Not installing OPAM2 wrappers && rm -rf /tmp/opam" && \


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


# tjr: install opam from web not apt -----------------------------------

# #   DEBIAN_FRONTEND=noninteractive apt-get -y install opam && 
# RUN curl -sL https://raw.githubusercontent.com/ocaml/opam/master/shell/install.sh > install.sh
# RUN chmod u+x install.sh
# RUN ./install.sh -y

RUN curl https://www.cs.le.ac.uk/people/tr61/opam-2.0.1-x86_64-linux  >opam
RUN chmod u+x ./opam
RUN sudo mv ./opam /bin

# RUN opam init -a --disable-sandboxing --compiler=4.06.1
# RUN ./opam switch create 4.06.1
RUN sudo echo $PATH

# NOTE tag 2f780f7 is just a reasonably recent (today!) 
RUN mkdir .ssh && \
  chmod 700 .ssh && \
  git config --global user.email "docker@example.com" && \
  git config --global user.name "Docker CI" && \
  sudo -u opam sh -c "git clone git://github.com/ocaml/opam-repository && cd opam-repository && git reset --hard 2f780f7" && \
  sudo -u opam sh -c "opam init -a --disable-sandboxing -y --compiler 4.06.1 /home/opam/opam-repository" && \
  sudo -u opam sh -c "opam install -y depext travis-opam"
RUN opam install ocamlfind

# end section ----------------------------------------------------------


# some bash setup ------------------------------------------------------

RUN sudo rm -f /bin/sh && sudo ln -sf /bin/bash /bin/sh
RUN echo "test -r /home/opam/.opam/opam-init/init.sh && . /home/opam/.opam/opam-init/init.sh > /dev/null 2> /dev/null || true" >> ~/.bashrc
RUN bash -i -c "ocamlfind list"


# end ------------------------------------------------------------------

ENTRYPOINT [ "opam", "config", "exec", "--" ]
CMD [ "bash" ]
