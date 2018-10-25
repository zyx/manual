# Plugin Development Tutorial

## Prerequisites

- Familiarity with C++ is required.
- [Set up your development environment](Building.html#setting-up-your-development-environment).
- If you would like to build Rack from source, follow [Building Rack](Building.html#building-rack).
- If you would like to save time, you may skip building Rack and use the [Rack SDK](https://github.com/VCVRack/Rack/issues/258#issuecomment-405119759) instead. You can then run your plugin with an official build of Rack.

## Template Plugin

Clone the [VCV Template plugin](https://github.com/VCVRack/Template) in a `plugins/` directory to get started. Familiarize yourself with the file structure.

- `Makefile`: The build system configuration file. Edit this to add compiler flags and custom targets.
- `src/`: C++ and C source files
	- `Template.cpp / Template.hpp`: Plugin-wide source and header for plugin initialization and configuration. Rename this to the name of your plugin.
	- `MyModule.cpp`: A single module's source code. Duplicate this file for every module you wish to add. You may have multiple modules per file or multiple files for a single module, but one module per file is recommended.
- `res/`: Resource directory for SVG graphics and anything else you need to `fopen()`
- `LICENSE.txt`: The template itself is released into public domain (CC0), but you may wish to replace this with your own license.

The Template plugin implements a simple sine VCO, demonstrating inputs, outputs, parameters, and other concepts.

## Inputs, Outputs, Parameters, and Lights

Decide how many components you need on the panel of your module.
Change the names of inputs, outputs, params, and lights in the enums in the `MyModule` class of `MyModule.cpp`.

## DSP

Write the DSP code of your module in the `MyModule::step()` function, using the values from the `params`, `inputs`, and `outputs` vectors.
Rack includes a work-in-progress DSP framework in the `include/dsp/` directory that you may use.
Writing a high quality audio processor is easier said than done, but there are many fantastic books and online resources on audio DSP that will teach you what you need to know.
My word of advice: *mind the aliasing*.

## Panel

Design your module's panel with a vector graphics editor and save it to the `res/` directory as an SVG file.
[Inkscape](https://inkscape.org/en/) is recommended, but [Adobe Illustrator](https://www.adobe.com/products/illustrator.html), [Affinity Designer](https://affinity.serif.com/en-gb/designer/), [Gravit Designer](https://www.designer.io/), etc. may also work with certain SVG export settings.
Make sure the path to the .svg file is correctly specified in the `setPanel(SVG::Load(...))` function in your `ModuleWidget` constructor.
Rack renders SVGs at 75 DPI, and the standard Eurorack 1HP module size is 128.5mm x 5.08mm, 5.06" x 0.2", or 380px x 15px.

Note: The Rack renderer is currently only capable of rendering path and group objects with solid fill and stroke. Gradients are experimental and might not work correctly. Text must be converted to paths. Clipping masks, clones, symbols, CSS other than a few style attributes, etc. are not supported.

## Component Widgets

Add widgets to the panel including params (knobs, buttons, switches, etc.), input ports, and output ports.
Helper functions `createParam()`, `createInput()`, and `createOutput()` are used to construct a particular `Widget` subclass, set its (x, y) position, range of values, and default value.
Rack Widgets are defined in `include/widgets.hpp` and `include/app.hpp`, and helpers are found in `include/rack.hpp`.

Note: Widgets from `include/components.hpp` using Component Library SVG graphics are licensed under CC BY-NC 4.0 and are free to use for noncommercial purposes.
Contact contact@vcvrack.com for information about licensing for commercial use.

## Naming

Eventually, you will need to change the name of your plugin from "Template" to something of your choice.

Decide on a "slug" (case-sensitive unique identifier) for your plugin that only contains letters, numbers, and the characters `_-`.
It should *NEVER* change after releasing your plugin, otherwise old patches will break, so choose the slug wisely.
To guarantee uniqueness, it is a good idea to prefix the slug by your name, alias, or company name if available, e.g. "MyCompany-MyPlugin".

- Rename `Template.cpp` and `Template.hpp`.
- Change references of `#include "Template.hpp"` in each of the source files.
- In the `Makefile`, change the `SLUG` and `VERSION`.

## Versioning

The version string of your plugin should follow the form **MAJOR.MINOR.REVISION** and is placed in your plugin's Makefile.

- Before *Rack 1.0*, the **MAJOR.MINOR** version should match the version of Rack your plugin is built for, e.g. **0.5**.
You are free to choose the **REVISION** version of your plugin, but it recommended to start counting at **0**.
For example, *MyPlugin 0.5.4* would be compatible with all *Rack 0.5.X* versions.
- After *Rack 1.0*, the **MAJOR** version should match the version of Rack your plugin is built for, e.g. **1**.
You are free to choose the **MINOR.REVISION** version of your plugin.
For example, *MyPlugin 1.4.2* would be compatible with all *Rack 1.X* versions.

After releasing a version of your plugin, it is recommended to add a git tag to your repository with `git tag X.Y.Z`.

## Licenses

Don't forget to edit the `LICENSE.txt` file to choose a license of your choice, unless you want to release your plugin into the public domain (CC0).

Before releasing your plugin, read the [Rack licenses](https://github.com/VCVRack/Rack#licenses).

If you are considering "porting" a hardware module to the VCV Rack platform, it is a good idea to ask the creator first.
It may be illegal, immoral, or cause unpleasant relationships to copy certain intellectual property without permission.

## Packaging

Make sure the VERSION and SLUG are correct in your Makefile, and run `make dist`.
A ZIP package is generated in `dist/` for your architecture.

If you do not have all platforms for building, other plugin developers will be happy to help you by simply obtaining your source and running `make dist` themselves.

## Releasing

To list your plugin on the [VCV Plugin Manager](https://vcvrack.com/plugins.html), see the [VCV community repository README](https://github.com/VCVRack/community#for-plugin-developers).

If you wish to sell your plugin on the [VCV Store](https://vcvrack.com/plugins.html), email contact@vcvrack.com for details.

## Maintaining

Since Rack is currently in Beta and moving very quickly, breaking changes may be made to the Rack plugin API.
Subscribe to the [Plugin API Updates Thread](https://github.com/VCVRack/Rack/issues/258) to receive notifications when the Rack API changes or a discussion about a change is being held.
