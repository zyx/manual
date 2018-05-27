# Voltage Standards

In Rack, input and output values carried by patch cables are in voltage units (V).
You can measure absolute voltage levels using modules like Fundamental Scope.

Rack attempts to model Eurorack standards as accurately as possible, but this is a problem for two reasons: there are very few actual "standards" in Eurorack (The only rule is that you can always find a module which breaks the rule), and there are a few differences between digital (finite sample rate) and analog (infinite sample rate).

### Audio and Modulation

Audio outputs are typically **±5V** (before bandlimiting is applied), and CV modulation sources are typically **0 to 10V** (unipolar CV) or **±5V** (bipolar CV).

### Output Saturation

In Eurorack, power supplies supply **-12 to 12V**.
No voltage should be generated beyond this range, since it would be mostly impossible to obtain in Eurorack.
Additionally, protection diodes on the ±12V rails usually drop the range to about ±11.7V.

However, if you do not want to model analog output saturation for simplicity or performance reasons, that is perfectly fine.
It is much better to allow voltages outside this range rather than use hard clipping with `clampf(out, -1.f, 1.f)` because in the best case they will be attenuated by a module downstream, and in the worst case, they will be hard clipped by the Audio module from Core.

If your module is capable of applying >1x gain to an input, it is a good idea to saturate the output.

### Triggers

In Eurorack, many modules are triggered by reaching a particular rising slope threshold.
However, because of the [Gibbs phenomenon](https://en.wikipedia.org/wiki/Gibbs_phenomenon), a digital emulation will falsely retrigger many times if the trigger source is bandlimited.

Thus, trigger inputs in Rack should use `SchmittTrigger` from `digital.hpp` with a low threshold of about **0.1V** and a high threshold of around **1 to 2V**.
For example, Audible Instruments modules are triggered once the input reaches 1.7V and can only be retriggered after the signal drops to or below 0V.
Rack plugins can implement this with `schmittTrigger.process(rescale(x, 0.1f, 2.f, 0.f, 1.f))`

Trigger sources should produce **5 to 10V** with a duration of 1 millisecond.
An easy way to do this is to use `PulseGenerator` from `digital.hpp`.

### Pitch

Most Eurorack manufacturers use the **1V/octave** standard.
The relationship between frequency $f$ and voltage $V$ is $f = f_0 \cdot 2^{V}$, where $f_0$ is an arbitrary baseline set by a pitch knob or the note C4 (MIDI note 60, $f_0 =$ 261.626 Hz).

### NaNs and Infinity

If your module might produce [NaNs](https://en.wikipedia.org/wiki/NaN) or infinite values with finite input, e.g. an unstable IIR filter or reverb, it should check and return 0 if this happens: `isfinite(out) ? out : 0.f`.