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

Search [Rack's issue tracker](https://github.com/VCVRack/Rack/issues?q=is%3Aissue) to check whether someone else has posted a similar issue. If you think your problem is unique (unlikely but possible), you may open an issue or email contact@vcvrack.com with a detailed report containing the following information.

- Your operating system and version
- The Rack version
- The actions that trigger the problem
- Any error messages that appear. Screenshots are helpful.
- The hardware (e.g. audio interface, MIDI device, graphics card) related to your problem

## I have a feature request.

After searching [Rack's issue tracker](https://github.com/VCVRack/Rack/issues?q=is%3Aissue), you may open an issue or email contact@vcvrack.com with the following information.

- Your proposal, with consideration for how it fits into Rack's existing features
- A possible workflow or diagram (if your request involves multiple steps or UI states, e.g. dragging multiple modules simultaneously).

Depending on the usefulness of your request, it may take 15 minutes or 24 months for your feature to be added, or the issue may be closed if there is little total benefit compared to the cost of implementation (time saved or spent using the feature, divided by the time to develop the feature).

## How do I load a default patch when selecting File > New?

Save a patch to `<Rack local directory>/template.vcv`, and it will be loaded after clearing the rack.

## Where is the "Rack local directory"?

- MacOS: `Documents/Rack/`
- Windows: `My Documents/Rack/`
- Linux: `~/.Rack/`

When running Rack in development mode, it is your current working directory instead.
