# Migrating 0.6 plugins to Rack v1

***This document is a draft. It is not recommended to migrate plugins at this time. If you begin now, you will likely need to follow this guide again when the Rack v1 API is stabilized.***

## The easy way: using the `rack0.hpp` compatibility header

Change `#include "rack.hpp"` to `#include "rack0.hpp"`

Create a `plugin.json` manifest file for your plugin and all modules based on the [Template manifest](https://github.com/VCVRack/Template/blob/v1/plugin.json) (TODO add actual manifest template/guide).

Remove `SLUG` and `VERSION` from the `Makefile`, since they are now defined in `plugin.json`.

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
perl -p -i -e "s/Model::create/createModel/g" src/*.cpp
perl -p -i -e "s/ParamWidget::create/createParam/g" src/*.cpp
perl -p -i -e "s/ModuleLightWidget::create/createLight/g" src/*.cpp
perl -p -i -e "s/Port::create/createPort/g" src/*.cpp
perl -p -i -e "s/Port::OUTPUT/PortWidget::OUTPUT/g" src/*.cpp
perl -p -i -e "s/Port::INPUT/PortWidget::INPUT/g" src/*.cpp
perl -p -i -e "s/Widget::create/createWidget/g" src/*.cpp
perl -p -i -e "s/MenuLabel::create/createMenuLabel/g" src/*.cpp
perl -p -i -e "s/MenuItem::create/createMenuItem/g" src/*.cpp
perl -p -i -e "s/toJson/dataToJson/g" src/*.cpp
perl -p -i -e "s/fromJson/dataFromJson/g" src/*.cpp
```

If your plugin uses any of Rack's `dsp/*.hpp` headers, remove the `#include` statements since they are now automatically included.

For most plugins, this should do it.
Compiling should generate hundreds of deprecation warnings, but it might succeed.
If not, continue to the next section.

## The right way: using the Rack v1 API

First follow the above section using the compatibility header.

Change `#include "rack0.hpp"` back to `#include "rack.hpp"`

Change
```cpp
addInput(createPort<...>(..., PortWidget::INPUT, ...));
to
addInput(createInput<...>(..., ...));
```

```cpp
addOutput(createPort<...>(..., PortWidget::OUTPUT, ...));
to
addOutput(createOutput<...>(..., ...));
```

```cpp
engineGetSampleRate()
to
app()->engine->getSampleRate()
```

```cpp
engineGetSampleTime()
to
app()->engine->getSampleTime()
```

TODO
