# Installing & Running

## System Requirements

VCV Rack is free software, so you may simply install it to check if it works.
However, if you are experiencing performance issues, make sure you have the following.
- Operating system: MacOS 10.7+, Windows 7+, or Linux (Ubuntu 16.04+, etc)
- CPU: Intel/AMD 64-bit processor from \~2011 or later
- Graphics: Dedicated Nvidia/AMD graphics card from \~2013 or later. Integrated (non-dedicated) graphics such as Intel HD/Iris are not recommended and cause significantly increased CPU usage.
- RAM: 1GB+
- Disk space: 1GB+

## Installing Rack

Download Rack on the [VCV Rack website](https://vcvrack.com/).

### Installing on Mac

Open the DMG image and copy the Rack app to your Applications folder.

If you wish to use [VCV Bridge](Bridge.html), copy `VCV-Bridge.vst` to the VST folder and/or the `VCV-Bridge.component` Audio Unit to the Components folder.

### Installing on Windows

Run the installer.

If you wish to use [VCV Bridge](Bridge.html), make sure the VST feature is checked for your architecture (32- or 64-bit) and specify the location to install it in the next few steps.

### Installing on Linux

Unzip the zip file.

If you wish to use [VCV Bridge](Bridge.html), copy the `Bridge/VCV-Bridge.so` VST plugin to your system's VST search location such as `/usr/lib/vst`.

## Installing plugins

On [VCVRack.com](https://vcvrack.com/) or the [VCV Plugin Manager](https://vcvrack.com/plugins.html), add each plugin you wish to install.
If not logged in to your VCV account, you will be prompted to log in or register.
Once the desired plugins are added to your account, open Rack and log in using the toolbar at the top of the window.
After logging in, click "Update plugins" and the new plugins will be synchronized to your computer.

If your computer is offline, you may download plugins using another computer and transfer the `Rack/plugins` folder to the offline computer.
Downloading plugins directly from the Plugin Manager website is not supported at this time.

## Installing plugins not available on the Plugin Manager

*Install third-party plugins at your own risk. Like VST plugins, installing plugins from unknown sources may compromise your computer and personal information.*

Download the plugin ZIP package from the vendor's website to `<Rack local directory>/plugins` (See [Where is the "Rack local directory"?](FAQ.html#where-is-the-rack-local-directory)). Rack will extract and load the plugin upon launch.

Note: Do not download the plugin via GitHub's green "Clone or download" button. These are source code ZIP packages and do not contain the compiled plugin binary. If the vendor distributes their plugin with GitHub, look in the "Releases" section for the compiled ZIP packages.


## Running Rack

### Running on Mac

Launch Rack from the Applications folder or the dock.
On modern Mac versions, you may need to right click the application and click "Open" when launching for the first time.

### Running on Windows

Click on Rack in the Start Menu.

### Running on Linux

Double click the `Rack` binary.
Or with the command-line, `cd` into the `Rack` directory and run `./Rack`.

### Command line usage

To launch Rack from the command line, `cd` into Rack's directory, and run `./Rack`.

- `-d`: Enables development mode
- `-g <path>`: Sets Rack's global directory
- `-l <path>`: Sets Rack's local directory
