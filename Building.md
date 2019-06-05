# Building

## Setting up your development environment

Before building Rack or Rack plugins, you must install build dependencies provided by your system's package manager.
Rack's own dependencies (GLEW, glfw, etc) do not need to be installed on your system, since specific versions are compiled locally during the build process.
However, you need proper tools to build Rack and these dependencies.

### Mac

Install [Homebrew](https://brew.sh/), and install build dependencies.
```bash
brew install git wget cmake autoconf automake libtool jq
```

### Windows

If you have an anti-virus program running, disable it or it may interfere with the build process.

Install [MSYS2](http://www.msys2.org/) and launch the MinGW 64-bit shell from the Start menu, *not the default MSYS shell*.
```bash
pacman -Syu
```
Then restart the shell.
```bash
pacman -Su git wget make tar unzip zip mingw-w64-x86_64-gcc mingw-w64-x86_64-gdb mingw-w64-x86_64-cmake autoconf automake mingw-w64-x86_64-libtool mingw-w64-x86_64-jq
```

### Linux

On Ubuntu 18.04+:
```bash
sudo apt install git gdb curl cmake libx11-dev libglu1-mesa-dev libxrandr-dev libxinerama-dev libxcursor-dev libxi-dev zlib1g-dev libasound2-dev libgtk2.0-dev libjack-jackd2-dev jq
```

On Arch Linux:
```bash
pacman -S git wget gcc gdb make cmake tar unzip zip curl jq
```

## Building Rack

You do not need to build Rack to build plugins if you use the Rack SDK.

*If the build fails for you, please [report the issue](FAQ.html#i-found-a-bug) to help the portability of Rack.*

Clone this repository with `git clone https://github.com/VCVRack/Rack.git` and `cd Rack`.
Make sure there are no spaces in your absolute path, since this breaks the Makefile-based build system.

Clone submodules.

	git submodule update --init --recursive

Build dependencies locally.
You may add `-j4` (or your number of logical cores) to your `make` commands to parallelize builds.
This may take 15-60 minutes.

	make dep

Build Rack.
This may take 1-5 minutes.

	make

Run Rack.

	make run

## Building Rack plugins

Plugins can be built in two ways:
- [Build Rack from source](#building-rack) and build plugins in the `plugins/` directory.
- Download a build of Rack and the Rack SDK, and build plugins anywhere you like.

Download or clone the plugin source code, e.g.

	git clone https://github.com/VCVRack/Fundamental.git

Clone the git repo's submodules.

	cd Fundamental
	git submodule update --init --recursive

Build the plugin.

	make dep
	make

If using the Rack SDK, specify its location with

	RACK_DIR=<Rack SDK dir> make dep
	RACK_DIR=<Rack SDK dir> make

To build, package, and install plugins to your Rack user directory in one step, run

	make install
