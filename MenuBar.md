# Menu Bar

![](images/menubar.png)


## File
### New
Clears the patch and loads the template patch (`<Rack user dir>/template.vcv`).
### Open/Save/Save as
Opens/saves the patch from/to a `.vcv` file.
Patches use the [JSON](https://json.org/) format and can also be viewed with a text editor.
### Save template
Saves the patch as `<Rack user dir>/template.vcv` so it is loaded when creating new patches.
### Revert
Restores the patch from the last saved state.
### Quit
Autosaves the patch to `<Rack user dir>/autosave.vcv` and closes Rack.
Rack also autosaves every 15 seconds to prevent losing work due to a crash, power failure, etc.


## Edit
### Undo/Redo
Rewinds and plays back all actions that edit the patch.
### Clear cables
Removes all cables from the patch.


## View
### Parameter tooltips
Enables/disables tooltips when hovering over parameters (knobs, sliders, buttons, etc) which display the name, numeric value, and optionally description of the parameter.
### Lock modules
Locks/unlocks modules from being moved by the mouse.
Prevents accidentally dragging modules.
### Zoom
Adjusts the zoom level for the rack from 25-400%.
Double-click to reset to 100%.
### Cable opacity
Sets the transparency level for patch cables.
Double-click to reset to 50%.
### Cable tension
Sets the relative length of patch cables.
Double-click to reset to 0.5.
### Fullscreen
Expands Rack to fill the screen with no window borders.


## Engine
### CPU timer
Enables/disables the measurement of time for each module to generate each sample (see [Sample rate](#sample-rate)).
This displays a meter on each module with the number of microseconds (μs) and the percentage of time spent in the module's assigned thread (see [Threads](#threads)).

If running in single-threaded mode, the total percentage must equal 100%, with "blocking" modules like [VCV Audio](Core.html#audio) consuming the remaining time by "sleeping" until the audio device is ready for more audio.
If multi-threading is enabled, the total percentage may equal up to \\(N \times 100\\%\\), although this number is a bit less in reality due to [multi-threading overhead](https://en.wikipedia.org/wiki/Amdahl%27s_law).

Timing takes CPU power itself, so it is recommended to disable the CPU timer when it is not needed for best performance.

### Sample rate
Sets Rack's engine sample rate.

Rack's engine works by repeatedly stepping the state of each module by `1 / sampleRate` seconds, producing 1 new sample for each output.
A higher sample rate decreases the timestep, resulting in more accurate analog circuit modeling and digital algorithms, while a lower sample rate decreases engine CPU usage.

### Threads
Sets the number of cores to be used in Rack's multithreaded engine.

To minimize power usage and CPU resources for other programs to use, disable multithreading by selecting 1 thread.
Using more threads increases CPU usage but increases the maximum number of modules you can use in the rack.

It is recommended to begin with 1 thread, and if you experience audio hiccups, try increasing the thread count by 1.
Continue adding threads until no hiccups occur.
The maximum recommended number of threads is the number of physical cores in your machine.
For example, a quad-core machine would likely maximize the number of modules by using 4 threads.

Due to [simultaneous multithreading](https://en.wikipedia.org/wiki/Simultaneous_multithreading) such as [Intel Hyper-Threading](https://en.wikipedia.org/wiki/Hyper-threading), you may attempt to use up to twice as many threads as physical cores in your machine, but typically this results in worse performance with higher power usage.


## Plugins

### Login
Logs into your VCV account registered at [vcvrack.com](https://vcvrack.com/).
Email [contact@vcvrack.com](mailto:contact@vcvrack.com) for account assistance.

### Update all
Updates and downloads all new plugins and plugin versions added to your VCV account.
Rack must be restarted to load new plugin updates.


## Help

### Manual
Opens [this manual](QuickStart.html).

### Open user folder
Opens the [Rack user directory](FAQ.html#where-is-the-rack-user-directory) in Windows Explorer, Apple Finder, etc.
