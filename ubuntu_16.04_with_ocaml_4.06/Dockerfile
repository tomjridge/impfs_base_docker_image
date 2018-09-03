FROM ubuntu:16.04

# ubuntu extra packages for ocaml build --------------------------------

RUN apt-get -y update
RUN apt-get install -y git make
RUN apt-get install -y curl
RUN apt-get install -y gcc
RUN apt-get install -y bzip2
RUN apt-get install -y wget
RUN apt-get install -y sudo
RUN apt-get install -y unzip m4


# begin section --------------------------------------------------------

#  git clone -b 1.2 git://github.com/ocaml/opam /tmp/opam && \
#  sh -c "cd /tmp/opam && make cold && make install && echo Not installing OPAM2 wrappers && rm -rf /tmp/opam" && \


# taken from https://github.com/ocaml-attic/opam-dockerfiles/blob/ubuntu-16.04_ocaml-4.04.2/Dockerfile

LABEL distro_style="apt" distro="ubuntu" distro_long="ubuntu-16.04" arch="x86_64" ocaml_version="4.04.2" opam_version="1.2" operatingsystem="linux"
RUN apt-get -y update && \
  DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \
  DEBIAN_FRONTEND=noninteractive apt-get -y install aspcud && \
  DEBIAN_FRONTEND=noninteractive apt-get -y install opam && \
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


# NOTE tag cef3d38 is just a reasonably recent (4 weeks ago) 
RUN mkdir .ssh && \
  chmod 700 .ssh && \
  git config --global user.email "docker@example.com" && \
  git config --global user.name "Docker CI" && \
  sudo -u opam sh -c "git clone git://github.com/ocaml/opam-repository && cd opam-repository && git reset --hard cef3d38" && \
  sudo -u opam sh -c "opam init -a -y --compiler 4.06.1 /home/opam/opam-repository" && \
  sudo -u opam sh -c "opam install -y depext travis-opam"
ENTRYPOINT [ "opam", "config", "exec", "--" ]
CMD [ "bash" ]

# end section ----------------------------------------------------------



# more useful ubuntu packages ------------------------------------------

USER root
RUN apt-get install -y time
USER opam
