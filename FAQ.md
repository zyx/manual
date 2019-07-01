# FAQ

## I found a bug.

Search [Rack's issue tracker](https://github.com/VCVRack/Rack/issues?q=is%3Aissue) to check if someone else has posted a similar bug report.
If you believe the problem has never been reported before, [create a GitHub account](https://github.com/) (it's free) and [open a bug report issue](https://github.com/VCVRack/Rack/issues/new?template=bug_report.md).
You must fill out the issue template, or it will be closed.

## I have a feature request.

All features added to Rack must begin with a well-written proposal.
If approved, it is implemented, publicly tested with development builds, and released in a future Rack version.

Search [Rack's issue tracker](https://github.com/VCVRack/Rack/issues?q=is%3Aissue) to check if someone else has posted a similar feature request.
If you believe the feature has never been requested before, [create a GitHub account](https://github.com/) (it's free) and [open an feature request issue](https://github.com/VCVRack/Rack/issues/new?template=feature_request.md).
You must fill out the issue template, or it will be closed.

## The graphics are rendered incorrectly, not at all, or Rack doesn't launch because of an "OpenGL error".

Rack requires at least OpenGL 2.0 with the `GL_EXT_framebuffer_object` extension.
If your graphics card supports this, make sure you've installed the latest graphics drivers, and restart Rack.
If this does not fix it, see below for instructions on submitting a bug to Rack's issue tracker.

## Where is the "Rack user folder"?

- MacOS: `Documents/Rack/`
- Windows: `My Documents/Rack/`
- Linux: `~/.Rack/`

When running Rack in development mode, it is your current working directory instead.

## Will Rack be ported to iOS or Android?

It is not planned. There are many issues with such a project.

- Technical:
	- Tablet and phone users don't normally use mice, so a touch driver would need to be written. If GLFW is still used, [touch support](https://github.com/glfw/glfw/issues/42) would need to be added to the library.
	- There is no user-managed filesystem on iOS, and forcing users to mess with the filesystem is bad UX on Android, so plugin folders and patch files would need to be managed entirely by Rack itself.
	- RtAudio and RtMidi don't have iOS Core Audio/MIDI or Android HAL/OpenSL ES backends, so they would need to be added and tested.
	- Apple does not allow apps distributed through the store to download and execute code, so either all plugins would need to be included in the distributable, or it could only be distributed on jailbroken iOS devices, which is an absurd user requirement.

- Business:
	- Such a port would be expensive to develop, so it would need to be sold commercially. Some plugins (proprietary, GPL, etc) would need special licensing agreements in order to be included in the package. Some plugins would increase the cost of the product if included in the package. Others would simply be omitted from the third-party plugin collection.
	- The friction for a developer to build and test their plugins on iOS/Android is significantly higher than the three desktop OS's, which may decrease their willingness to develop Rack plugins.
	- When serving an app on the App Store or Google Play, Apple and Google are not obligated to continue serving an app and may remove it at will or change policies on a whim that can disrupt VCV's business model. This would place VCV's risk in a small number of baskets.

## Why does VCV Audio consume so much CPU?

The CPU meter measures the time spent processing each module, not the "resource" of CPU power.
In order for playback timing to be consistent, your audio device, and therefore VCV Audio, waits until all samples in the current audio buffer are played before moving onto the next audio buffer.
Otherwise, your device's DAC and ADC would play and record at very inconsistent and incorrect sample rates.
While waiting, the engine thread is put to sleep, so no energy is consumed by the thread.
See [CPU timer](MenuBar.html#cpu-timer) for more info.

## Is VCV Rack available as a VST/AU/AAX plugin for DAWs?

VCV Rack is a standalone application, not a plugin.
Shortly after Rack v2 is released, estimated for Dec 2019, Rack will also be available as a 64-bit VST2 plugin for around $99.
VST3/AU/AAX versions might be released afterwards.
All Rack v2 plugins will be compatible with the plugin version of Rack.
The standalone version of Rack v2 will continue to be free/open-source.

## Does VCV Rack work with touch screens?

Rack's window library GLFW does not support [touch input](https://github.com/glfw/glfw/issues/42), so Rack relies on the operating system to control the mouse cursor using the touch screen.
This means that multi-touch gestures do not work.
However, you can set `"allowCursorLock"` to `false` in `<Rack user dir>/settings.json` to improve touch cursor handling for knobs.
