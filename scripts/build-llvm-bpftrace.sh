#!/bin/bash
set -x
mydir=$(cd $(dirname $0) && pwd)
cd "$mydir"

llvm_version=17.0.6
bpftrace_version=0.19.1
bcc_version=0.29.1
libbpf_version=1.3.0


if ! echo "$PATH" | grep -q devtoolset-11; then
	echo "please install and enable devtoolset-11 first"
cat <<EOF
Commands:
yum install centos-release-scl
yum install devtoolset-11-*
scl enable devtoolset-11 bash
EOF
	exit 1

fi
echo "please install other lib"
cat <<EOF
安装最新版本cmake
https://cmake.org/download/
解压之后加到PATH
# cereal 头文件安装
https://github.com/USCiLab/cereal/archive/v1.3.2.tar.gz
tar xf cereal-1.3.2.tar.gz
mv cereal-1.3.2/include/cereal /usr/local/include/
# 源码下载安装bzip2, xz, libpcap
https://sourceware.org/bzip2/
https://tukaani.org/xz/
dwarves-1.24
libpcap
EOF

echo "build and install llvm"
cd "$mydir"
tar xf llvm-${llvm_version}.src.tar.xz
tar xf clang-${llvm_version}.src.tar.xz
mv clang-${llvm_version}.src llvm-${llvm_version}.src/tools/clang
tar xf libcxx-${llvm_version}.src.tar.xz
mv libcxx-${llvm_version}.src llvm-${llvm_version}.src/tools/libcxx
tar xf cmake-${llvm_version}.src.tar.xz
mv cmake-${llvm_version}.src cmake
tar xf clang-tools-extra-${llvm_version}.src.tar.xz
mv  clang-tools-extra-${llvm_version}.src llvm-${llvm_version}.src/tools/clang/tools/extra
mkdir llvm-build && cd llvm-build
cmake -G "Unix Makefiles" \
    -DCMAKE_INSTALL_PREFIX=/opt/llvm-clang-17 \
    -DCMAKE_BUILD_TYPE=Release \
    -DLLVM_TARGETS_TO_BUILD="host;BPF" \
    -DLLVM_INCLUDE_TESTS=OFF \
    -DLLVM_INCLUDE_BENCHMARKS=OFF \
    -DLIBCLANG_BUILD_STATIC=ON \
    -DLLVM_ENABLE_LTO=OFF \
    -DLLVM_ENABLE_TERMINFO=OFF \
    -DBUILD_SHARED_LIBS=OFF \
    ../llvm-${llvm_version}.src
make -j8 && make install

echo "build bpftrace"
cd "$mydir"
if [[ ! -d bcc ]]; then
 curl -FssL https://github.com/iovisor/bcc/releases/download/v${bcc_version}/bcc-src-with-submodule.tar.gz
fi
if [[ ! -d libbpf ]]; then
 curl -FssL https://github.com/libbpf/libbpf/archive/refs/tags/v1.3.0.tar.gz
fi
mv bcc/* bpftrace-${bpftrace_version}/bcc/
mv libbpf/* bpftrace-${bpftrace_version}/libbpf/

mkdir bpftrace-build && cd bpftrace-build
../bpftrace-${bpftrace_version}/build-libs.sh
cmake \
    -DCMAKE_BUILD_TYPE=Release   \
    -DSTATIC_LINKING:BOOL=ON   \
    -DBUILD_TESTING=OFF \
    -DLIBBFD_INCLUDE_DIRS=/opt/rh/devtoolset-11/root/usr/include \
    -DLIBOPCODES_INCLUDE_DIRS=/opt/rh/devtoolset-11/root/usr/include \
    -DCMAKE_PREFIX_PATH=/opt/llvm-clang-17 \
    -DCMAKE_INSTALL_PREFIX=/opt/bpftrace \
    ../bpftrace-${bpftrace_version}
make -j8 && make install

