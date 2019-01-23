# Migrating 0.6 plugins to Rack v1

***This document is a draft. It is not recommended to migrate plugins at this time. If you begin now, you will likely need to follow this guide again when the Rack v1 API is stabilized.***

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
perl -pi -e "s/Model::create/createModel/g" src/*.cpp
perl -pi -e "s/ParamWidget::create/createParam/g" src/*.cpp
perl -pi -e "s/ModuleLightWidget::create/createLight/g" src/*.cpp
perl -pi -e "s/Port::create/createPort/g" src/*.cpp
perl -pi -e "s/Port::OUTPUT/PortWidget::OUTPUT/g" src/*.cpp
perl -pi -e "s/Port::INPUT/PortWidget::INPUT/g" src/*.cpp
perl -pi -e "s/Widget::create/createWidget/g" src/*.cpp
perl -pi -e "s/MenuLabel::create/createMenuLabel/g" src/*.cpp
perl -pi -e "s/MenuItem::create/createMenuItem/g" src/*.cpp
perl -pi -e "s/toJson/dataToJson/g" src/*.cpp
perl -pi -e "s/fromJson/dataFromJson/g" src/*.cpp
```

If your plugin uses any of Rack's `dsp/*.hpp` headers, remove the `#include` statements since they are now automatically included.

For most plugins, this should do it.
Compiling should generate hundreds of deprecation warnings, but it might succeed.
If not, read the compile error, and don't hesitate to ask questions in the VCV community forum or GitHub issue tracker.

## The right way: using the Rack v1 API

First complete the above section using the compatibility header as a first step.

Once it is able to compile, change `#include "rack0.hpp"` back to `#include "rack.hpp"`

```
perl -pi -e "s/engineGetSampleRate/app()->engine->getSampleRate/g" src/*.cpp
perl -pi -e "s/engineGetSampleTime/app()->engine->getSampleTime/g" src/*.cpp
perl -pi -e "s/, PortWidget::INPUT//g" src/*.cpp
perl -pi -e "s/addInput\(createPort/addInput(createInput/g" src/*.cpp
perl -pi -e "s/, PortWidget::OUTPUT//g" src/*.cpp
perl -pi -e "s/addOutput\(createPort/addOutput(createOutput/g" src/*.cpp
perl -pi -e "s/randomUniform/random::uniform/g" src/*.cpp
perl -pi -e "s/randomNormal/random::normal/g" src/*.cpp
```

Add the `dsp::` prefix.

TODO
