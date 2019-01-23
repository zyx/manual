# FAQ

## When will Rack 1.0 be ready?

Rack is currently in Beta (thus the version 0.x), so by using it, you are an "early tester".
Don't worry, Rack 1.0 will also be free open-source software.

In order for Rack to earn its "1.0" designation, it must improve in the following three fronts.

### Compatibility
Since I am an "indie developer", I cannot yet afford to test Rack on every combination of hardware on the market.
With the introduction of commercial VCV plugin sales, I will soon be able to invest in hardware that is known to have compatibility problems with Rack.
If you are willing to lend me hardware to test, email contact@vcvrack.com for details.

### Stability
Rack is not ready to be trusted for live use, although some musicians have used it successfully in live performances.
In order for Rack to be considered "stable", it must produce audio with no clicks or pops on modern hardware for several minutes and must crash less than once per several days of continuous use.
Currently, stability in Rack is the most developed among these three fronts.

### Performance
Depending on your CPU and graphics card, Rack may consume high CPU/GPU resources and therefore increase your laptop's fan speed.
I am aware of this, so there is no need to inform me.

To answer the original question, there is currently no time estimate for 1.0.

## My audio interface / MIDI device doesn't work.

Make sure the device drivers are up to date for your operating system.
If this does not solve it, please refrain from notifying me unless you
- are willing to lend me your audio interface (email contact@vcvrack.com for more details), or
- you are a developer and have discovered a fix to the source code of Rack, [RtAudio](https://github.com/thestk/rtaudio) (use [rtaudio_test](https://github.com/AndrewBelt/rtaudio_test) to determine whether the issue is with Rack or RtAudio), or [RtMidi](https://github.com/thestk/rtmidi).

See **Compatibility** above.

## The graphics are rendered incorrectly, not at all, or Rack doesn't launch because of an "OpenGL error".

Rack requires at least OpenGL 2.0 with the `GL_EXT_framebuffer_object` extension.
If your graphics card supports this, make sure you've installed the latest graphics drivers, and restart Rack.
If this does not fix it, see below for instructions on submitting a bug to Rack's issue tracker.

See **Compatibility** above.

## The CPU usage is high.

See **Performance** above.

## I found a bug.

Search [Rack's issue tracker](https://github.com/VCVRack/Rack/issues?q=is%3Aissue) to check whether someone else has posted a similar issue.
If you believe the problem has never been reported before, [open an issue](https://github.com/VCVRack/Rack/issues/new/choose) on GitHub, or email contact@vcvrack.com if you don't want to register a GitHub account, with a detailed report containing the following information.

- Your operating system and version
- The Rack version
- The actions that trigger the problem
- Any error messages that appear. Screenshots are helpful.
- The hardware (e.g. audio interface, MIDI device, graphics card) related to your problem

## I have a feature request.

Search [Rack's issue tracker](https://github.com/VCVRack/Rack/issues?q=is%3Aissue) to check whether someone else has posted a similar feature request.
If you believe the feature has never been posted before, [open an issue](https://github.com/VCVRack/Rack/issues/new/choose) on GitHub, or email contact@vcvrack.com if you don't want to register a GitHub account, with a detailed report containing the following information.

- Your proposal, with consideration for how it fits into Rack's existing features
- A possible workflow or diagram (if your request involves multiple steps or UI states, e.g. dragging multiple modules simultaneously).

Your feature request may be addressed during the next period of new feature design of Rack.
If your request is judged to be not sufficiently useful to other users, it may be closed.

## How do I load a default patch when selecting File > New?

Save a patch to `<Rack local directory>/template.vcv`, and it will be loaded after clearing the rack.

## Where is the "Rack local directory"?

- MacOS: `Documents/Rack/`
- Windows: `My Documents/Rack/`
- Linux: `~/.Rack/`

When running Rack in development mode, it is your current working directory instead.

## Will Rack be ported to iOS or Android?

It is not planned. Many issues would need to be addressed.
- Tablet and phone users don't normally use mice, so a touch driver would need to be written. If GLFW is still used, [touch support](https://github.com/glfw/glfw/issues/42) would need to be added to the library.
- There is no user-managed filesystem on iOS, and forcing users to mess with the filesystem is bad UX on Android, so plugin folders and patch files would need to be managed entirely by Rack itself.
- There is no OpenGL on mobile devices, so the OpenGL ES driver would need to be used and tested.
- RtAudio and RtMidi don't have iOS Core Audio/MIDI or Android HAL/OpenSL ES backends, so they would need to be added and tested.
- Apple does not allow apps distributed through the store to download and execute code, so either all plugins would need to be included in the distributable, or it could only be distributed on jailbroken iOS devices, which is an absurd user requirement.
- Such a port would be very expensive to develop, so it would need to be sold commercially. Some plugins (proprietary, GPL, etc) would need special licensing agreements in order to be included in the package. Some plugins would increase the cost of the product if included in the package. Others would simply be omitted from the third-party plugin collection.
- The friction for a developer to build and test their plugins on iOS/Android is significantly higher than the three desktop OS's, which may decrease their willingness to develop Rack plugins.
