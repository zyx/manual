# ABI/API Version

An **ABI** ([Application Binary Interface](https://en.wikipedia.org/wiki/Application_binary_interface)) is a machine-readable list of symbols (functions, globals, and classes) that can only be called, accessed, and used in specific ways.
An **API** ([Application Programming Interface](https://en.wikipedia.org/wiki/Application_programming_interface)) consists of C and C++ headers (`.h`/`.hpp`) that define how the ABI can be used.

Rack plugins must be compiled against a particular *major version* of Rack to match its ABI, so that when Rack loads them, they link to Rack's symbols correctly.
The major version is `X` in the version name `vX.Y.Z`.


## Symbol additions

Symbols might be added to the API/ABI of Rack in a minor version update.
Plugins may use these new symbols, but they cannot be loaded with older versions of Rack.
Users will need to upgrade their Rack minor version to load your plugin.

The minor version is `Y` in the version name `vX.Y.Z`.

This is similar to how VST plugins work, where for example, VST 2.3 plugins cannot load in DAWs that only implement the VST 2.2 standard.


## Git branches and tags

In [Rack's git repository](https://github.com/VCVRack/Rack), each major version has its own branch, labeled `v1`, `v2`, etc.

There is no `master` branch.
The default branch on GitHub is the major version for the latest release of Rack listed at [vcvrack.com](https://vcvrack.com/).
To update the major version of your source tree, simply check out its branch.
It is highly recommended to run `make clean` in the root and `dep/` directories after or before switching branches.

When any version of Rack is released, the build's commit is tagged with its full version name (e.g. `v1.0.0`).
However, this is only for informative purposes.
Building from "detached heads" of branches is not supported, since dependency URLs and other issues may need to be fixed after time has passed from the release date.
