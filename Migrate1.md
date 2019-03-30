# Migrating 0.6 plugins to Rack v1

**This document is a draft. It is not recommended to migrate plugins at this time. If you begin now, you will likely need to follow this guide again when the Rack v1 API is stable.**

## Prerequisites

Install new build dependencies.

### Mac

```bash
brew install python jq
```

### Windows

```bash
pacman -S python mingw-w64-x86_64-jq
```

### Linux

On Ubuntu 16.04:
```bash
sudo apt install jq
```

On Arch Linux:
```bash
pacman -S python jq
```

## The easy way: using the `rack0.hpp` compatibility header

Change `#include "rack.hpp"` to `#include "rack0.hpp"`

Create a `plugin.json` manifest file for your plugin using the `helper.py` script included in the Rack SDK.
```bash
python <Rack SDK>/helper.py createmanifest
```

Add a module entry to `plugin.json` for each module in your plugin.
When prompted, don't overwrite the module .cpp file.
```bash
python <Rack SDK>/helper.py createmodule <module slug>
```

Remove `SLUG` and `VERSION` from the `Makefile`, and remove `	p->slug = ...` and `p->version = ...` from your plugin's main `.cpp` file, since they are now defined in `plugin.json`.

For each module, change the `Model::create` call
```cpp
Model *modelMyModule = Model::create<MyModule, MyModuleWidget>("Template", "MyModule", "My Module", OSCILLATOR_TAG);
```
to
```cpp
Model *modelMyModule = Model::create<MyModule, MyModuleWidget>("MyModule");
```
since the plugin name, module name, and module tags are now defined in `plugin.json`.

For the following replacements, make sure you have perl installed (`perl -v`), and paste these lines into your terminal in the root of your plugin directory to automatically make replacements.
It might even be a good idea to review the changes and `git commit` between each step.

Rename the `plugin` variable to avoid a name collision with the `plugin::` namespace.
```bash
perl -pi -e 's/\bplugin\b/pluginInstance/g' src/*
```
Rename `X::create()` functions to `createX()`.
```bash
perl -pi -e 's/Model::create/createModel/g' src/*
perl -pi -e 's/ParamWidget::create/createParam/g' src/*
perl -pi -e 's/ModuleLightWidget::create/createLight/g' src/*
perl -pi -e 's/Port::create/createPort/g' src/*
perl -pi -e 's/Port::OUTPUT/PortWidget::OUTPUT/g' src/*
perl -pi -e 's/Port::INPUT/PortWidget::INPUT/g' src/*
perl -pi -e 's/Widget::create/createWidget/g' src/*
perl -pi -e 's/MenuLabel::create/createMenuLabel/g' src/*
perl -pi -e 's/MenuItem::create/createMenuItem/g' src/*
```
Rename `to/fromJson()` methods to `dataTo/FromJson()`.
```bash
perl -pi -e 's/toJson/dataToJson/g' src/*
perl -pi -e 's/fromJson/dataFromJson/g' src/*
```

If your plugin uses any of Rack's `dsp/*.hpp` headers, remove the `#include "dsp/..."` lines since they are now automatically included by `rack.hpp`.

Now compile your plugin.
Hundreds of deprecation warnings should appear, but it might succeed.
If so, your plugin can now be distributed as a Rack v1 plugin.
If not, read the compile errors, and don't hesitate to ask questions in the [Development category of the VCV Community](https://community.vcvrack.com/c/development) or [Rack GitHub issue tracker](https://github.com/VCVRack/Rack/issues).
If your plugin is open-source, you may even ask the [VCV Repair Team](https://github.com/VCVRack/library/issues/269) to create a pull request in your repository.

## The right way: using the Rack v1 API

First complete the above section using the compatibility header as a first step.

Once it is able to compile, change `#include "rack0.hpp"` back to `#include "rack.hpp"`.

Add new arguments to the `step()` (now called `process()`) and `draw()` methods.
```bash
perl -pi -e 's/void (\w+::)?step\(\)/void $1process(const ProcessArgs &args)/g' src/*
perl -pi -e 's/void draw\(NVGcontext \*vg\)/void draw(const DrawArgs &args)/g' src/*
perl -pi -e 's/\bvg\b/args.vg/g' src/*
perl -pi -e 's/engineGetSampleRate\(\)/args.sampleRate/g' src/*
perl -pi -e 's/engineGetSampleTime\(\)/args.sampleTime/g' src/*
```
Use the `APP` macro for accessing global state.
```bash
perl -pi -e 's/Font::load/APP->window->loadFont/g' src/*
perl -pi -e 's/Image::load/APP->window->loadImage/g' src/*
perl -pi -e 's/SVG::load/APP->window->loadSvg/g' src/*
```
Use `createInput/Output()` functions instead of `createPort()`.
```bash
perl -pi -e 's/, PortWidget::INPUT//g' src/*
perl -pi -e 's/addInput\(createPort/addInput(createInput/g' src/*
perl -pi -e 's/, PortWidget::OUTPUT//g' src/*
perl -pi -e 's/addOutput\(createPort/addOutput(createOutput/g' src/*
```
Add namespaces to global functions.
```bash
perl -pi -e 's/\bassetPlugin\b/asset::plugin/g' src/*
perl -pi -e 's/\brandomUniform\b/random::uniform/g' src/*
perl -pi -e 's/\brandomNormal\b/random::normal/g' src/*
perl -pi -e 's/\brandomu32\b/random::u32/g' src/*
```
Change `.value` to getters and setters, and change `.active` to `isConnected()`.
```bash
perl -pi -e 's/(params\[.*?\])\.value/$1.getValue()/g' src/*
perl -pi -e 's/(inputs\[.*?\])\.value/$1.getVoltage()/g' src/*
perl -pi -e 's/(outputs\[.*?\])\.value = (.*?);/$1.setVoltage($2);/g' src/*
perl -pi -e 's/(inputs\[.*?\])\.active/$1.isConnected()/g' src/*
perl -pi -e 's/(outputs\[.*?\])\.active/$1.isConnected()/g' src/*
```
Add the `dsp::` namespace to dsp classes.
TODO
```bash
```
Add `config()` to the `Module` constructor, and add `setModule` to the `ModuleWidget` constructor.
```bash
perl -pi -e 's/: Module\(NUM_PARAMS, NUM_INPUTS, NUM_OUTPUTS, NUM_LIGHTS\) \{/{\n\t\tconfig(NUM_PARAMS, NUM_INPUTS, NUM_OUTPUTS, NUM_LIGHTS);/g' src/*
perl -pi -e 's/: ModuleWidget\(module\) \{/{\n\t\tsetModule(module);/g' src/*
```

Now make sure your plugin compiles.

### Adding new Rack v1 features

You are now ready to add optional Rack v1 features to your plugin.

Parameters now have optional labels.
Add `Param::config()` to the `Module` constructor.
```cpp
params[X_PARAM].config(0.0, 1.0, 0.0, "Label");
```
