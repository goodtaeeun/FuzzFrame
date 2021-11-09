FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive

# (Temporary: replace URL for fast download during development)
RUN sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list

ENV DEBIAN_FRONTEND="noninteractive"
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -yy libc6-dev binutils libgcc-9-dev
RUN apt-get install -yy \
      wget apt-transport-https git unzip \
      build-essential libtool libtool-bin gdb \
      automake autoconf bison flex python python3 sudo vim

# Copied from OSS-FUZZ
ENV OUT=/out
ENV SRC=/src
ENV WORK=/work
ENV PATH="$PATH:/out"
RUN mkdir -p $OUT $SRC $WORK
ENV CMAKE_VERSION 3.21.1
RUN wget https://github.com/Kitware/CMake/releases/download/v$CMAKE_VERSION/cmake-$CMAKE_VERSION-Linux-x86_64.sh && \
    chmod +x cmake-$CMAKE_VERSION-Linux-x86_64.sh && \
    ./cmake-$CMAKE_VERSION-Linux-x86_64.sh --skip-license --prefix="/usr/local" && \
    rm cmake-$CMAKE_VERSION-Linux-x86_64.sh && \
    rm -rf /usr/local/doc/cmake /usr/local/bin/cmake-gui
COPY docker-setup/checkout_build_install_llvm.sh /root/
RUN /root/checkout_build_install_llvm.sh
RUN rm /root/checkout_build_install_llvm.sh

# Install packages needed for fuzzers and benchmark
RUN apt-get update && \
    apt-get install -yy \
      # Several packages get uninstalled after LLVM setup.
      git build-essential bc\
      # For boringssl
      golang \
      # For guetzli
      libpng-dev \
      # For harfbuzz
      ragel \
      # For libxml
      python-dev \
      # For libarchive
      libbz2-dev liblzo2-dev liblzma-dev liblz4-dev libz-dev \
      libxml2-dev libssl-dev libacl1-dev libattr1-dev lrzip \
      liblz4-tool lzop \
      # For openssl
      libgcrypt20-dev \
      # For freetype
      libarchive-dev \
      # For libssh
      libgss-dev \
      # For pcre
      subversion \
      # For libjpeg
      nasm

# Create a fuzzer directory and start working there.
RUN mkdir /fuzzer
WORKDIR /fuzzer
COPY docker-setup/setup_AFLGo.sh /fuzzer/setup_AFLGo.sh
RUN ./setup_AFLGo.sh

# Create a benchmark directory and start working there.
RUN mkdir -p /benchmark/bin && \
    mkdir -p /benchmark/seed && \
    mkdir -p /benchmark/runtime
COPY docker-setup/seed/empty /benchmark/seed/empty
WORKDIR /benchmark

# Copy proof-of-concept inputs and fuzzing target points.
COPY docker-setup/poc /benchmark/poc
COPY docker-setup/target /benchmark/target

# Setup binutils.
COPY docker-setup/build_binutils.sh /benchmark/build_binutils.sh
RUN ./build_binutils.sh

WORKDIR /
