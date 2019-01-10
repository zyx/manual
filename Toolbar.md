# Toolbar

## Power meter

When power meters are enabled, Rack measures the amount of time spent processing each module in **mS** (millisamples).
This is a unit of time equal to `$0.001 / \text{sample rate}$`.
In many ways, this is analogous to the module power limit imposed by hardware modular synthesizers in mA (milliamperes).

To maintain a stable audio clock, the total amount of time spent processing all modules must equal **1000 mS**.
To achieve this, the [Audio](Core.html#audio) module from [Core](Core.html) uses your audio device's high-precision clock to regulate Rack's engine, so it idles for the remaining mS until this total is met.
If the Audio idle time falls close to an average of 0 mS over its block size, an audio stutter may occur.
This can be caused by other modules consuming lots of mS.

## Internal sample rate

Rack advances the state of each module by the duration specified by Rack's internal sample rate.
A higher sample rate decreases the timestep, resulting in more accurate analog circuit modeling at the expensive of more mS consumed by all modules.
