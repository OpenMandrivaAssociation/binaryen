Name: binaryen
Version: 118
Release: 1
Source0: https://github.com/WebAssembly/binaryen/archive/refs/tags/version_%{version}.tar.gz
Summary: Optimizer and compiler/toolchain library for WebAssembly
URL: https://github.com/binaryen/binaryen
License: MIT
Group: Development/Tools
BuildSystem: cmake
BuildOption: -DBUILD_TESTS:BOOL=OFF
BuildOption: -DEMSCRIPTEN_ENABLE_PTHREADS:BOOL=ON
BuildOption: -DEMSCRIPTEN_ENABLE_WASM64:BOOL=ON
BuildOption: -DEMSCRIPTEN_ENABLE_WASM_EH:BOOL=ON
BuildOption: -DBUILD_FOR_BROWSER:BOOL=ON

%description
Optimizer and compiler/toolchain library for WebAssembly

# It doesn't really make sense to split out -devel files here, given
# the whole package is really a -devel
%files
%{_bindir}/wasm-as
%{_bindir}/wasm-ctor-eval
%{_bindir}/wasm-dis
%{_bindir}/wasm-emscripten-finalize
%{_bindir}/wasm-fuzz-lattices
%{_bindir}/wasm-fuzz-types
%{_bindir}/wasm-merge
%{_bindir}/wasm-metadce
%{_bindir}/wasm-opt
%{_bindir}/wasm-reduce
%{_bindir}/wasm-shell
%{_bindir}/wasm-split
%{_bindir}/wasm2js
%{_includedir}/binaryen-c.h
%{_includedir}/wasm-delegations.def
%{_libdir}/libbinaryen.so
