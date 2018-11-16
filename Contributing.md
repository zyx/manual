# Contributing

I (Andrew Belt) generally do not accept unpaid contributions to the Rack codebase itself due to time costs.

Writing code is easy. Instead, the difficulty of changing Rack's source code involves

- research to devise the best solution with a convincing argument
- acceptance of API/ABI change proposals
- generalizability to solve similar issues, and flexibility for solving future solutions without an entire rewrite
- future-proofing to avoid unnecessarily breaking patches or API/ABI in the near future
- testing on relevant platforms, hardware devices, plugins, etc.
- dedication to maintain the code in the future
- sometimes legal review

Unpaid contributions typically omit many of the above tasks, making the code more expensive for me to accept than simply writing it myself. Instead, there are many other areas where contributions are much appreciated.

- Dependencies of Rack. Especially [nanovg](https://github.com/memononen/nanovg)'s performance, [rtaudio](https://github.com/thestk/rtaudio)/[rtmidi](https://github.com/thestk/rtmidi)'s stability and compatibility, and maybe even touch support in [GLFW](https://github.com/glfw/glfw). You would be helping many more projects than just Rack.
- Your own Rack [plugin](PluginDevelopmentTutorial.html)
- Maintaining the Rack plugin ecosystem by [curating](https://github.com/VCVRack/community/issues/352), [updating](https://github.com/VCVRack/community/issues/269), and [reviewing](https://github.com/VCVRack/community/issues/354) plugins
- Edits to the [VCV Rack manual](https://github.com/VCVRack/manual).

I will consider your contribution to Rack if you first open a [GitHub issue](https://github.com/VCVRack/Rack/issues) with a detailed design proposal, which may create an open discussion before the change is implemented.
By submitting code through a pull request, you agree to assign the copyright of your code to Andrew Belt to be licensed under the BSD-3-Clause (see [Licenses](https://github.com/VCVRack/Rack#licenses)).
