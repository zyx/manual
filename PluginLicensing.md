# Plugin Licensing

**This document is a draft. It is currently not in effect, so everything here is bogus now, but it may eventually become the guide for plugin licensing in the future.**

VCV Rack is open-source software, but you should still familiarize yourself with the [VCV Rack licenses](https://github.com/VCVRack/Rack/blob/v1-gpl/LICENSE.md) before releasing your plugin, to avoid misuse of intellectual property. If in doubt, send any licensing questions to contact@vcvrack.com.


### I want to release my plugin under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) (GPLv3).

Since Rack is licensed under GPLv3, you may license your plugin under GPLv3 as well.
You may do anything with your plugin that the GPLv3 allows, including selling it without a commercial license (below) as long as you release the source code under GPLv3.

### I want to release my plugin non-commercially under non-GPLv3 terms.

This is the most common choice among plugin developers.
Rack offers a [VCV Rack Non-Commercial Plugin License Exception](https://github.com/VCVRack/Rack/blob/v1-gpl/LICENSE.md) which allows you to license your plugin under any terms you want, as long as it is offered free of charge.
You may choose:
- **Open-source**. [BSD 3-clause](https://opensource.org/licenses/BSD-3-Clause), [MIT](https://opensource.org/licenses/MIT), and [CC0](https://creativecommons.org/publicdomain/zero/1.0/) are popular licenses.
- **Closed-source freeware**.
- **Donationware**, as long as a donation is not required for use.

Note that if you copy significant portions of Rack's code into your own plugin, you must license it under GPLv3.

If someone makes a fork of your non-GPLv3 open-source plugin that is not a Rack plugin (e.g. a port to VST or a digital hardware module), their source code becomes no longer linked to VCV Rack and is thus no longer a "derived work" of Rack, so Rack's license does not apply to their source code.

### I want to sell my plugin commercially under non-GPLv3 terms.

VCV offers commercial royalty licensing for Rack plugins by emailing [contact@vcvrack.com](mailto:contact@vcvrack.com).
This license also includes permission to use the [Component Library](https://github.com/VCVRack/Rack/blob/v1/include/componentlibrary.hpp) graphics by [Grayscale](https://grayscale.info/), which are normally licensed for non-commercial use only.

It is recommended to contact VCV as early as possible in your development process to make sure the license agreement is ready well before you release your plugin.
You can expedite the licensing processing by sending concepts and design mockups along with your license request.

You may also wish to sell your plugin on the [VCV Store](https://vcvrack.com/plugins.html).
Some benefits of distributing your plugin on the VCV Store:
- Most Rack users are already familiar with the VCV Store checkout system.
- Plugin updates are automatically synchronized to users' Rack installations.
- VCV offers advanced technical support with the Rack SDK and DSP library.
- You may supply VCV with either binary packages for Mac/Windows/Linux, or a source package which we will build for you.
- Access to dashboard for managing customers' purchases and viewing real-time statistics.

You must follow the **VCV Rack Plugin Ethics Guidelines** in order to obtain a commercial plugin license:
- You may not clone the brand name, model name, logo, or layout of components (knobs, ports, switches, etc) of an existing hardware or software module without permission from its owner, regardless of whether these are covered under trademark/copyright law.
