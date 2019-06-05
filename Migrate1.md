# Migrating v0.6 Plugins to Rack v1

This is a step-by-step guide for migrating plugins using the Rack v0.6 API to Rack v1.
There are three phases of porting.
- **Phase 1**: Quickly produces a valid Rack v1 plugin.
- **Phase 2**: Modernizes the code by replacing deprecated v0.6 function calls with new v1 functions.
- **Phase 3**: Takes advantage of new Rack v1 features such as parameter labels and polyphony.

## Prerequisites

Install new build dependencies.
- [jq](https://stedolan.github.io/jq/) for parsing JSON when building plugins
- Python 3.6+ for running Rack's `helper.py` script
- Perl for replacing text with regex.

### Mac

```bash
brew install jq python
```

### Windows

```bash
pacman -S mingw-w64-x86_64-jq python3
```

### Linux

On Ubuntu 18.04+:
```bash
sudo apt install jq python3
```

On Arch Linux:
```bash
pacman -S jq python perl
```

## Phase 1: Using the `rack0.hpp` compatibility header

### 1.1

`cd` to your plugin's root directory.
Create a `plugin.json` manifest file for your plugin using the helper script included in the Rack SDK.
```bash
python3 <Rack SDK>/helper.py createmanifest <plugin slug>
```

### 1.2

For each module in your plugin, add an entry to `plugin.json` using the helper script.
```bash
python3 <Rack SDK>/helper.py createmodule <module slug>
```

### 1.3

Remove `SLUG` and `VERSION` from the `Makefile`, and remove `	p->slug = ...` and `p->version = ...` from your plugin's main `.cpp` file, since they are now defined in `plugin.json`.

### 1.4

Change `#include "rack.hpp"` to `#include "rack0.hpp"` to access deprecated functions.

### 1.5

For each module, remove the author, module name, and tags from the `Model::create` call, since they are now defined in `plugin.json`.
For example, change
```cpp
Model *modelMyModule = Model::create<MyModule, MyModuleWidget>("Template", "MyModule", "My Module", OSCILLATOR_TAG);
```
to
```cpp
Model *modelMyModule = Model::create<MyModule, MyModuleWidget>("MyModule");
```

### 1.6

Make the following [regex](https://en.wikipedia.org/wiki/Regular_expression) replacements by pasting these lines into your terminal in the root of your plugin directory.
It is a good idea to review the changes and `git commit` between each step, in case an automatic replacement goes wrong.

#### 1.6.1

Rename the `plugin` variable to avoid a name collision with the `plugin::` namespace.
```bash
perl -i -pe 's/\bplugin\b/pluginInstance/g' src/*
```

#### 1.6.2

Rename `X::create()` functions to `createX()`.
```bash
perl -i -pe 's/Model::create/createModel/g' src/*
perl -i -pe 's/ParamWidget::create/createParam/g' src/*
perl -i -pe 's/ModuleLightWidget::create/createLight/g' src/*
perl -i -pe 's/Port::create/createPort/g' src/*
perl -i -pe 's/Port::OUTPUT/PortWidget::OUTPUT/g' src/*
perl -i -pe 's/Port::INPUT/PortWidget::INPUT/g' src/*
perl -i -pe 's/Widget::create/createWidget/g' src/*
perl -i -pe 's/MenuEntry::create\(\)/new MenuEntry/g' src/*
perl -i -pe 's/MenuLabel::create/createMenuLabel/g' src/*
perl -i -pe 's/MenuItem::create/createMenuItem/g' src/*
```

#### 1.6.3

Rename `to/fromJson()` methods to `dataTo/FromJson()`.
```bash
perl -i -pe 's/toJson/dataToJson/g' src/*
perl -i -pe 's/fromJson/dataFromJson/g' src/*
```

### 1.7

If your plugin uses any of Rack's `dsp/*.hpp` headers, remove the `#include "dsp/..."` lines since they are now automatically included by `rack.hpp`.

### 1.8

The event API has been overhauled in v1.
If you use `on*()` event handler methods in your custom widgets, see [event.hpp](https://github.com/VCVRack/Rack/blob/v1/include/event.hpp) and [widget/Widget.hpp](https://github.com/VCVRack/Rack/blob/v1/include/widget/Widget.hpp) for new methods and event classes.

Once completed, your plugin may compile, although many deprecation warnings may appear.
If there are too many warnings to see the errors, you may temporarily add `FLAGS += -w` to your `Makefile`.

### 1.9

Your `ModuleWidget`s must gracefully handle a NULL `module` argument, otherwise Rack will crash when the Module Browser attempts to display your module.
`createParam()` etc. gracefully handle NULL, but if you've written custom widgets with a `module` pointer, make sure you check `if (module) ...` before accessing the pointer.

### 1.10

Test your plugin in Rack by adding your modules, moving parameters, clicking custom widgets, and searching your plugin in the Module Browser.

If your plugin still does not build, read the compile errors, and don't hesitate to ask questions in the [Development board of the VCV Community](https://community.vcvrack.com/c/development) or [Rack's GitHub issue tracker](https://github.com/VCVRack/Rack/issues) about the v1 API.
If your plugin is open-source, you may even ask the [VCV Repair Team](https://github.com/VCVRack/library/issues/269) to create a pull request for you.

## Phase 2: Updating your code to the Rack v1 API

### 2.1

Once your plugin can be compiled, change `#include "rack0.hpp"` back to `#include "rack.hpp"`.

### 2.2

Add new arguments to the `Module::step()` (now called `process()`) and `Widget::draw()` methods.
```bash
perl -i -pe 's/void (\w+::)?step\(\)/void $1process(const ProcessArgs &args)/g' src/*
perl -i -pe 's/void draw\(NVGcontext \*vg\)/void draw(const DrawArgs &args)/g' src/*
perl -i -pe 's/\bvg\b/args.vg/g' src/*
```
Note: `Widget::step()` has not been renamed, but this replacement will incorrectly rename it.

### 2.3

Use the `Module::process()` argument struct to access the sample rate/time.
```bash
perl -i -pe 's/engineGetSampleRate\(\)/args.sampleRate/g' src/*
perl -i -pe 's/engineGetSampleTime\(\)/args.sampleTime/g' src/*
```
Note: This only works inside `Module::process()` methods.
You can call `APP->engine->getSampleRate()` and `APP->engine->getSampleTime()` anywhere in your code, although this is slightly slower than the above.

### 2.4

Use the `APP` macro for accessing global state instead of calling global functions.
```bash
perl -i -pe 's/Font::load/APP->window->loadFont/g' src/*
perl -i -pe 's/Image::load/APP->window->loadImage/g' src/*
perl -i -pe 's/SVG::load/APP->window->loadSvg/g' src/*
```

### 2.5

Use `createInput/Output()` functions instead of `createPort()`.
```bash
perl -i -pe 's/, PortWidget::INPUT//g' src/*
perl -i -pe 's/addInput\(createPort/addInput(createInput/g' src/*
perl -i -pe 's/, PortWidget::OUTPUT//g' src/*
perl -i -pe 's/addOutput\(createPort/addOutput(createOutput/g' src/*
```

### 2.6

Add namespaces to global functions.
```bash
perl -i -pe 's/\bassetGlobal\b/asset::system/g' src/*
perl -i -pe 's/\bassetLocal\b/asset::user/g' src/*
perl -i -pe 's/\bassetPlugin\b/asset::plugin/g' src/*
perl -i -pe 's/\brandomUniform\b/random::uniform/g' src/*
perl -i -pe 's/\brandomNormal\b/random::normal/g' src/*
perl -i -pe 's/\brandomu32\b/random::u32/g' src/*
perl -i -pe 's/\bstringf\b/string::f/g' src/*
```

### 2.7

Change `.value` to getters and setters, and change `.active` to `isConnected()`.
```bash
perl -i -pe 's/(params\[.*?\])\.value/$1.getValue()/g' src/*
perl -i -pe 's/(inputs\[.*?\])\.value/$1.getVoltage()/g' src/*
perl -i -pe 's/(outputs\[.*?\])\.value = (.*?);/$1.setVoltage($2);/g' src/*
perl -i -pe 's/(inputs\[.*?\])\.active/$1.isConnected()/g' src/*
perl -i -pe 's/(outputs\[.*?\])\.active/$1.isConnected()/g' src/*
```

### 2.8

Add the `dsp::` namespace to dsp classes.
```bash
perl -i -pe 's/\b(quadraticBipolar|cubic|quarticBipolar|quintic|sqrtBipolar|exponentialBipolar|BooleanTrigger|SchmittTrigger|PulseGenerator|RealFFT|ComplexFFT|RCFilter|PeakFilter|SlewLimiter|ExponentialSlewLimiter|ExponentialFilter|RealTimeConvolver|MinBlepGenerator|stepEuler|stepRK2|stepRK4|SampleRateConverter|Decimator|Upsampler|RingBuffer|DoubleRingBuffer|AppleRingBuffer|VuMeter|hann|hannWindow|blackman|blackmanWindow|blackmanNuttall|blackmanNuttallWindow|blackmanHarris|blackmanHarrisWindow|Frame|VUMeter)\b/dsp::$1/g' src/*
```

### 2.9

Add `config()` to the `Module` constructor, and add `setModule()` to the `ModuleWidget` constructor.
```bash
perl -i -pe 's/: Module\(NUM_PARAMS, NUM_INPUTS, NUM_OUTPUTS, NUM_LIGHTS\) \{/{\n\t\tconfig(NUM_PARAMS, NUM_INPUTS, NUM_OUTPUTS, NUM_LIGHTS);/g' src/*
perl -i -pe 's/: ModuleWidget\(module\) \{/{\n\t\tsetModule(module);/g' src/*
```

### 2.10

For each param in each module, copy `minValue, maxValue, defaultValue` from `createParam(pos, module, paramId, minValue, maxValue, defaultValue)` to a new `configParam(paramId, minValue, maxValue, defaultValue)` call in your `Module` constructor.
Then remove the values from `createParam`.

For example, if you have the line
```cpp
	addParam(createParam<BlackKnob>(Vec(10, 20), module, MyModule::LEVEL_PARAM, 0.f, 10.f, 5.f));
```
create a new line
```cpp
	configParam(LEVEL_PARAM, 0.f, 10.f, 5.f);
```
in the `MyModule` constructor, and change the original line to
```cpp
	addParam(createParam<BlackKnob>(Vec(10, 20), module, MyModule::LEVEL_PARAM));
```

You can automate this process by running
```bash
perl -nle 'print "configParam($1, \"\");" while /createParam.*?module, (.*?)\)/g' src/*
```
and copying the respective groups of lines into each module's `Module` constructor.
Then remove the arguments with
```bash
perl -i -pe 's/(createParam.*?module, .*?)(,.*?)\)/$1)/g' src/*
```

Now make sure your plugin compiles.

## Phase 3: Adding new Rack v1 features

You are now ready to add optional Rack v1 features to your plugin.

You may add parameters labels, units, and nonlinear scaling to be displayed when users right-click on a parameter or enable *View > Parameter tooltips*. See [Module::configParam()](https://github.com/VCVRack/Rack/blob/v1/include/engine/Module.hpp#L94-L95).

If you with to add support for polyphonic cables, see [How polyphonic cables will work in Rack v1](https://community.vcvrack.com/t/how-polyphonic-cables-will-work-in-rack-v1/1464), [Making your monophonic module polyphonic](https://community.vcvrack.com/t/how-polyphonic-cables-will-work-in-rack-v1/1464/39), and [engine/Port.hpp](https://github.com/VCVRack/Rack/blob/v1/include/engine/Port.hpp).
