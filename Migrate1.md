# Migrating 0.6 plugins to Rack v1

**This document is a draft. It is not recommended to migrate plugins at this time. If you begin now, you will likely need to follow this guide again when the Rack v1 API is stabilized.**

## The easy way: using the `rack0.hpp` compatibility header

Change `#include "rack.hpp"` to `#include "rack0.hpp"`

Create a `plugin.json` manifest file for your plugin and all modules based on the [Template manifest](https://github.com/VCVRack/Template/blob/v1/plugin.json) (TODO add actual manifest template/guide).

Remove `SLUG` and `VERSION` from the `Makefile` and `	p->slug = ...` and `p->version = ...` from your plugin's main `.cpp` file, since they are now defined in `plugin.json`.

For each module, change the `Model::create` call
```cpp
Model *modelMyModule = Model::create<MyModule, MyModuleWidget>("Template", "MyModule", "My Module", OSCILLATOR_TAG);
```
to
```cpp
Model *modelMyModule = Model::create<MyModule, MyModuleWidget>("MyModule");
```

Make the following string replacements (requires Perl).
```
# Rename `plugin` variable to avoid a name collision with the `plugin::` namespace
perl -pi -e "s/\bplugin\b/pluginInstance/g" src/*

# Change `X::create()` functions to `createX()`
perl -pi -e "s/Model::create/createModel/g" src/*
perl -pi -e "s/ParamWidget::create/createParam/g" src/*
perl -pi -e "s/ModuleLightWidget::create/createLight/g" src/*
perl -pi -e "s/Port::create/createPort/g" src/*
perl -pi -e "s/Port::OUTPUT/PortWidget::OUTPUT/g" src/*
perl -pi -e "s/Port::INPUT/PortWidget::INPUT/g" src/*
perl -pi -e "s/Widget::create/createWidget/g" src/*
perl -pi -e "s/MenuLabel::create/createMenuLabel/g" src/*
perl -pi -e "s/MenuItem::create/createMenuItem/g" src/*

# Change `to/fromJson()` to `dataTo/FromJson()`
perl -pi -e "s/toJson/dataToJson/g" src/*
perl -pi -e "s/fromJson/dataFromJson/g" src/*
```

If your plugin uses any of Rack's `dsp/*.hpp` headers, remove the `#include` statements since they are now automatically included.

For most plugins, this should do it.
Compiling should generate hundreds of deprecation warnings, but it might succeed.
If not, read the compile error, and don't hesitate to ask questions in the VCV community forum or GitHub issue tracker.

## The right way: using the Rack v1 API

First complete the above section using the compatibility header as a first step.

Once it is able to compile, change `#include "rack0.hpp"` back to `#include "rack.hpp"`

```
# Use `APP` macro for accessing global state
perl -pi -e "s/engineGetSampleRate/APP->engine->getSampleRate/g" src/*
perl -pi -e "s/engineGetSampleTime/APP->engine->getSampleTime/g" src/*
perl -pi -e "s/Font::load/APP->window->loadFont/g" src/*
perl -pi -e "s/Image::load/APP->window->loadImage/g" src/*
perl -pi -e "s/SVG::load/APP->window->loadSvg/g" src/*

# Use `createInput/Output()` functions instead of `createPort()`
perl -pi -e "s/, PortWidget::INPUT//g" src/*
perl -pi -e "s/addInput\(createPort/addInput(createInput/g" src/*
perl -pi -e "s/, PortWidget::OUTPUT//g" src/*
perl -pi -e "s/addOutput\(createPort/addOutput(createOutput/g" src/*

# Add namespaces to global functions
perl -pi -e "s/randomUniform/random::uniform/g" src/*
perl -pi -e "s/randomNormal/random::normal/g" src/*

# Change `void draw(NVGcontext *vg)` to `void draw(const DrawContext &ctx)`
perl -pi -e "s/draw\(NVGcontext \*vg\)/draw\(const DrawContext &ctx\)/g" src/*
perl -pi -e "s/\(vg/(ctx.vg/g" src/*
perl -pi -e "s/draw\(vg\)/draw\(ctx\)/g" src/*

# Add the `dsp::` namespace to dsp classes
# TODO
```
