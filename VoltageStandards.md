# Voltage Standards

In Rack, input and output values carried by patch cables are in voltage units (V).
You can measure absolute voltage levels using modules like Fundamental Scope.

Rack attempts to model Eurorack standards as accurately as possible, but this is a problem for two reasons: there are very few actual "standards" in Eurorack (The only rule is that you can always find a module which breaks the rule), and there are a few differences between digital (finite sample rate) and analog (infinite sample rate).

## Levels

Signals should typically be \\(10V_{pp}\\) (peak-to-peak).
This means that audio outputs should typically be **±5V** (before bandlimiting is applied), and CV modulation sources should typically be **0 to 10V** (unipolar CV) or **±5V** (bipolar CV).

## Output Saturation

In Eurorack, power supplies supply **-12 to 12V**.
No voltage should be generated beyond this range, since it would be mostly impossible to obtain in Eurorack.
Additionally, protection diodes on the ±12V rails usually drop the range to about ±11.7V.

However, if you do not want to model analog output saturation for simplicity or performance reasons, that is perfectly fine.
It is much better to allow voltages outside this range rather than use hard clipping with `clamp(out, -1.f, 1.f)` because in the best case they will be attenuated by a module downstream, and in the worst case, they will be hard clipped by the Audio module from Core.

If your module is capable of applying >1x gain to an input, it is a good idea to saturate the output.

## Triggers and Gates

In Eurorack, many modules are triggered by reaching a particular rising slope threshold.
However, because of the [Gibbs phenomenon](https://en.wikipedia.org/wiki/Gibbs_phenomenon), a digital emulation will falsely retrigger many times if the trigger source is bandlimited (e.g. by using a virtual VCO square wave as a trigger input or a hardware trigger through an audio interface.)

Therefore, trigger inputs in Rack should be triggered by a [Schmitt trigger](https://en.wikipedia.org/wiki/Schmitt_trigger) with a low threshold of about **0.1V** and a high threshold of around **1 to 2V**.
Rack plugins can implement this using `dsp::SchmittTrigger` with `schmittTrigger.process(rescale(x, 0.1f, 2.f, 0.f, 1.f))`

Trigger sources should produce **10V** with a duration of **1ms**.
An easy way to hold a trigger for this duration is to use `dsp::PulseGenerator` with `pulseGenerator.trigger(1e-3f)`.

Gates should produce **10V** when active.

## Timing

Each cable in Rack induces a 1-sample delay of its carried signal from the output port to the input port.
This means that it is not guaranteed that two signals generated simultaneously will arrive at their destinations at the same time if the number of cables in each signal's chain is different.
For example, a pulse sent through a utility module and then to a sequencer's CLOCK input will arrive one sample later than the same pulse sent directly to the sequencer's RESET input.
This will cause the sequencer to reset to step 1, and one sample later, advance to step 2, which is undesirable behavior.

Therefore, modules with a CLOCK and RESET input, or similar variants, should ignore CLOCK triggers up to **1ms** after receiving a RESET trigger.
You can use `dsp::Timer` for keeping track of time.

## Pitch and Frequencies

Modules should use the **1V/oct** (volt per octave) standard for CV control of frequency information.
In this standard, the relationship between frequency \\(f\\) and voltage \\(V\\) is \\(f = f_0 \cdot 2^{V}\\), where \\(f_0\\) is the baseline frequency.
Your module might have a frequency knob which may offset \\(V\\).
At its default position, audio-rate oscillators should use a baseline of the note C4 defined by [International Pitch Notation](https://en.wikipedia.org/wiki/Scientific_pitch_notation) ("middle C", MIDI note 60, \\(f_0\\) = 261.6256 Hz = `dsp::FREQ_C4`).
Low-frequency oscillators and clock generators should use 120 BPM (\\(f_0\\) = 2 Hz).

## NaNs and Infinity

If your module might produce [NaNs](https://en.wikipedia.org/wiki/NaN) or infinite output values when given only finite input, e.g. an unstable IIR filter or reverb, it should check and return 0 if this happens: `std::isfinite(out) ? out : 0.f`.

## Polyphony

If your module has polyphonic outputs, then it can be considered a "polyphonic module", so add the "Polyphonic" tag to the module's manifest.
It is recommended to support up to 16 channels, which is the maximum that Rack allows.

Typically each voice in your module can be abstracted into an "engine".
The number of active engines \\(N\\) should be defined by the number of channels of the "main" input (e.g. 1V/oct input for VCOs, audio input for filters, gate input for envelope generators, etc).
All other secondary inputs with \\(M\\) channels should follow these rules:
- If monophonic (\\(M = 1\\)), its voltage should be copied to all engines.
- If polyphonic with enough channels (\\(M \geq N\\)), each channel voltage should be used in its respective engine.
- If polyphonic but not enough channels (\\(1 < M < N\\)), 0V should be copied to out-of-bounds engines.

All of this behavior is provided by `Port::getPolyVoltage(c)`.

Monophonic modules should handle polyphonic inputs gracefully:
- For inputs intended to be used solely for audio, sum the voltages of all channels (e.g. with `Port::getVoltageSum()`)
- For inputs intended to be used for CV or hybrid audio/CV, use the first channel's voltage (e.g. with `Port::getVoltage()`)
