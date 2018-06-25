# Installing

Download Rack on the [VCV Rack website](https://vcvrack.com/).

### Mac

Open the DMG image and copy the Rack app to your Applications folder.
You may need to right click the application and click "Open" when launching for the first time.

### Windows

Run the installer, and launch Rack from the Start Menu.

### Linux

Unzip the zip file. Run `./Rack`.

## Installing plugins

On the [VCV Plugin Manager](https://vcvrack.com/plugins.html), add each plugin you wish to install.
If not logged in to your VCV account, you will be prompted to log in or register.
Once the desired plugins are added to your account, open Rack and log in using the toolbar at the top of the window.
After logging in, click "Update plugins" and the new plugins will be synchronized to your computer.

If your computer is offline, you may download plugins using another computer and transfer the `Rack/plugins` folder to the offline computer.

## Installing plugins not available on the Plugin Manager

*Install third-party plugins at your own risk. Like VST plugins, installing plugins from unknown sources may compromise your computer and personal information.*

Download the plugin ZIP package from the vendor's website to `<Rack local directory>/plugins` (See [Where is the "Rack local directory"?](FAQ.html#where-is-the-rack-local-directory)). Rack will extract and load the plugin upon launch.

Note: Do not download the plugin via GitHub's green "Clone or download" button. These are source code ZIP packages and do not contain the compiled plugin binary. If the vendor distributes their plugin with GitHub, look in the "Releases" section for the compiled ZIP packages.
