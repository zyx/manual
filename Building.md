# Building

## Setting up your development environment

Before building Rack, you must install build dependencies provided by your system's package manager.
Rack's own dependencies (GLEW, glfw, etc) do not need to be installed on your system, since specific versions are compiled locally during the build process.
However, you need proper tools to build Rack and these dependencies.

### Mac

Install [Xcode](https://developer.apple.com/xcode/).
Using [Homebrew](https://brew.sh/), install the build dependencies.
```
brew install git wget cmake autoconf automake libtool jq
```

### Windows

If you have an anti-virus program running, disable it.

Install [MSYS2](http://www.msys2.org/) and launch the MinGW 64-bit shell from the Start menu, *not the default MSYS shell*.
```
pacman -Syu
```
Then restart the shell.
```
pacman -Su git wget make tar unzip zip mingw-w64-x86_64-gcc mingw-w64-x86_64-cmake autoconf automake mingw-w64-x86_64-libtool mingw-w64-x86_64-jq
```

### Linux

On Ubuntu 16.04:
```
sudo apt install git curl cmake libx11-dev libglu1-mesa-dev libxrandr-dev libxinerama-dev libxcursor-dev libxi-dev zlib1g-dev libasound2-dev libgtk2.0-dev libjack-jackd2-dev jq
```

On Arch Linux:
```
pacman -S git wget gcc make cmake tar unzip zip curl jq
```

## Building Rack

*If the build fails for you, please report the issue with a detailed error message to help the portability of Rack.*

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

Be sure to check out and build the version of Rack you wish to build your plugins against.

It is recommended to download plugins to Rack's `plugins/` directory, e.g.

	cd plugins
	git clone https://github.com/VCVRack/Fundamental.git

Clone the git repo's submodules.

	cd Fundamental
	git submodule update --init --recursive

Build the plugin.

	make dep
	make
