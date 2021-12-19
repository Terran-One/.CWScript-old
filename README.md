# CWScript

CWScript is a scripting language for writing smart contracts that run on blockchains such as Terra that use the CosmWasm as an execution layer.

## Features

- familiar syntax: can be learned and used easily without prior knowledge of Rust
- built-in language constructs for contract semantics
- compiles to functioning CosmWasm Rust code that comply with Standard Model's guidelines
- provides a common framework for communicating contracts with non-developers
- bundled with helpful tooling & generators, and easily extensible
- provides a better framework for composability and code-reusability

## Installation

CWScript requires a environment with a installation of Python v3.7+.

Install CWScript through `pip` or (sometimes `pip3`).

```sh
$ pip install cwscript
```

This installs the CWScript language toolchain as well as the `cwscript` Python library module.

Once installed, the CWScript toolchain executables should be available in your Python path.

```sh
$ python3 -m cwsc --version
CWScript Compiler v0.1.0
```

For convenience, we recommend that you include binaries installed to your Python path in your shell's `$PATH` environment variable. Then, you can simply run `cwsc` without the leading `python3 -m`.

## Usage

CWScript ships with 2 executables:

- `cwsc`: entrypoint for using CWScript compiler and contract tooling
- `cwsls`: starts a server that implements the Language Server Protocol

**NOTE:** You will likely never have to use `cwsls` manually (unless you're working on an IDE or editor plugin),
as interactions with `cwsls` will be managed automatically by the CWScript extension / plugin for your editor.

### Compiling a contract into Rust

```sh
$ cwsc compile <SOURCE-FILE(S)> --contract <CONTRACT-NAME> [--out <OUTPUT-DIR>]
```

To compile CWScript into Rust, you should specify:

- `SOURCE-FILE(S)`: path(s) to CWScript source file(s) (ext: `.cws`)

  You should specify the source files which are relevant for the build, i.e. contain the definition for a contract that you intend to compile. **The compiler automatically resolves file paths for `import` statements; it is not necessary to add them here.**

  The compiler processes the source files from left-to-right and collects each file's definitions into separate symbol tables.

- `CONTRACT-NAME`: contract(s) to compile

  You must explicitly specify the names of the contract you wish to compile. This is done using the `--contract <CONTRACT-NAME>` option.
  If no contract names are given, the compiler will only perform pre-compilation processing (parsing, static analysis, etc.) and terminate with no generated output. If the contract name is found in multiple source files, the compiler will complain and ask you to clarify like this: `--contract <FILE>:<CONTRACT-NAME>`, where `FILE` must match the format it was provided.

- `OUTPUT-DIR`: folder containing the output Rust source

### Initialize a new CWScript project

For larger projects, it is recommended to organize your code according to the CWScript project structure.

```sh
$ cwsc init <PROJECT-NAME> [<PROJECT-DIR>]
```

This command creates a new directory with the basic structure of a CWScript project. By default, the directory's name will be the provided `PROJECT-NAME` in lowercase kebab-case. If there is already a file or folder with that name, the compiler will complain and ask that you provide another location with `PROJECT-DIR`.

### Bundled tooling

CWScript ships with a set of standard tools to aid in the development of contracts. They are accessible through `cwsc tool <TOOL-NAME>`.

## Contents

This repository contains various components of the CWScript distribution.

### Language Implementation & Core Libraries

`cwscript/`

The implementation of the CWScript language (parser & analysis libraries) is written in Python 3.

### Language Server

`cwsls/`

The CWScript distribution includes `cwsls`, a basic implementation of the Language Server Protocol
which enables feature-rich language integration into editors such as VS Code, Eclipse, Emacs, etc.

### Language Server Extension for VS Code

`cwscript-vscode-extension/`

An language server extension for VS Code is also included, which integrates `cwsls` to provide
facilities for working with CWScript projects such as syntax highlighting, code linting, testing and debugging,
and live introspection from static analysis.

### Documentation

`docs/`

The documentation site for CWScript uses Docusaurus v2.

### Examples

`examples/`

We provide a number of sample CWScript projects for reference and testing. We recommend forking and
playing around with the examples to better understand how to use the CWScript language and toolchain
within the context of a real app. We have also provided several well-documented translations of popular
CosmWasm contracts from Confio and large dApp projects on Terra.
