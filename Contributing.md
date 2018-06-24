# Contributing

I (Andrew Belt) generally do not accept external contributions to the Rack codebase itself.

Before writing a single line of code, most features and bug fixes require
- research to devise the best solution with a convincing argument
- testing on relevant platforms, audio/MIDI devices, different plugins, etc.
- dedication to maintain the code in the future
- generalizability to solve similar issues, and flexibility for solving future solutions without an entire rewrite
- sometimes legal review

Instead, there are many other areas where contributions are much appreciated.
- Dependencies of Rack. Especially [nanovg](https://github.com/memononen/nanovg)'s performance, [rtaudio](https://github.com/thestk/rtaudio)/[rtmidi](https://github.com/thestk/rtmidi)'s stability and compatibility, and maybe even touch support in [GLFW](https://github.com/glfw/glfw). You would be helping many more projects than just Rack.
- Your own Rack [plugin](PluginDevelopmentTutorial.md)
- Maintaining the Rack plugin ecosystem by [curating](https://github.com/VCVRack/community/issues/352), [updating](https://github.com/VCVRack/community/issues/269), and [reviewing](https://github.com/VCVRack/community/issues/354) plugins
- Edits to the [VCV Rack manual](https://github.com/VCVRack/manual).

I will consider your contribution to Rack if you first open a [GitHub issue](https://github.com/VCVRack/Rack/issues) with a detailed design proposal, which may create an open discussion before the change is implemented.
By submitting code through a pull request, you agree to assign the copyright of your code to Andrew Belt to be licensed under the BSD-3-Clause (see [Licenses](https://github.com/VCVRack/Rack#licenses)).
