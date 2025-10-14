# QUAM intro: 

Quam represents a higher-level abstraction on QUA, making it easier for experimental physicists to conduct experiments using the QM hardware. 

Below is the general workflow of how one uses Quam and its specifics, so that you know how you might integrate this into your SW. Later on, there are more automated examples. 

### Create your machine

Your machine represents the top-level container for your quantum setup. The 'machine' at the start of your code is an empty container, which will be populated as we go on. 

e.g. 
 ```python
 machine = Quam()
 ```

Once you populate this machine with the right components, then you can save this via `machine.save()`. This Quam state can then easily be loaded into whichever 
experiment you need via `Quam.load()`. We will see this more later. 

### Populate the machine with channels

Say your qubit only requires a single output. In that case, you would use the `SingleChannel` Quam channel. The example is shown in script 1. 

 ```python
 qubit = SingleChannel(
    opx_output = ("con1", 5, 1), # FEM 5, output 1. Output from the OPX perspective
 )
 ```

#### Output Channels
##### SingleChannel
- A single analogue OPX output channel

##### IQChannel
- A dual analogue I/Q output channel

##### MWChannel
- An analogue MW output channel


#### Input Channels
##### InSingleChannel
- A single analogue input channel

##### InIQChannel
- A dual analogue input channel 

##### InMWChannel
- A single MW input channel

#### In/Out Channels
##### InOutSingleChannel
- A single analogue output and a single input

##### InOutIQChannel
- A dual I/Q analogue output and a dual analogue input

##### InSingleOutIQChannel
- A single analogue output and a dual analogue I/Q input

##### InIQOutSingleCHannel
- A dual analogue I/Q output and a single analogue input

##### InOutMWChannel
- An analogue MW FEM output and input

#### Misc
##### DigitalOutputChannel
- A digital output channel

##### TimeTaggingAddon
- A channel addon which allows time-tagging

##### StickyChannelAddon
- A channel addon which makes the channel element sticky. Sticky elements persist their last-applied voltage. 


### Populate the operations and other features of your object

Right now, your qubit is only tied to an OPX output, with no other features. Quam allows you to easily populate the element with the necessary pulses and waveforms. 

 ```python
 qubit.operations["GaussianPulse"] = pulses.GaussianPulse(...)
 ```


