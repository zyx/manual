# Plugin Metadata

This document defines the `plugin.json` file found at the root of your plugin folder.
For example, see Fundamental's [plugin.json](https://github.com/VCVRack/Fundamental/blob/v1/plugin.json) file.

JSON paths are denoted in "flat format", as used by [jq](https://stedolan.github.io/jq/manual/).

## `.slug`

*String. Required.*

The unique identifier for your plugin.
Slugs may only contain letters `a-z` and `A-Z`, numbers `0-9`, hyphens `-`, and underscores `_`.

After your plugin is released, the slug must *never* change, otherwise patch compatibility would be broken.
To guarantee uniqueness, it is a good idea to prefix the slug by your "brand name" if available, e.g. "MyCompany-MyPlugin".

The word "slug" [comes from web publishing](https://en.wikipedia.org/wiki/Clean_URL#Slug) to represent URL paths that never change, which in turn [comes from typesetting](https://en.wikipedia.org/wiki/Slug_(typesetting)).

## `.name`

*String. Required.*

The human-readable name for your plugin.
Used for labeling your plugin the VCV Library.

Unlike slugs, the name can be changed at any time without breaking patch compatibility.

## `.version`

*String. Required.*

The version of your plugin should follow the form `MAJOR.MINOR.REVISION`.
Do not include the "v" prefix---this is added automatically where appropriate.

The `MAJOR` version should match the version of Rack your plugin is built for, e.g. 1.
You are free to choose the `MINOR.REVISION` part of your plugin version.
For example, *MyPlugin 1.4.2* would specify that your plugin is compatible with *Rack 1.X*.

If you publish the source code in a git repository, it is recommended to add a git tag with `git tag vX.Y.Z` and `git push --tags`.

## `.license`

*String. Required.*

The license of your plugin.
Use `"proprietary"` for commercial and freeware plugins.

If your plugin uses a common open-source license, the identifier from the [SPDX License List](https://spdx.org/licenses/) should be used.

## `.brand`

*String. Optional.*

Prefix string for all modules in your plugin.
For example, the brand "VCV" is used by the Fundamental plugin to create "VCV VCF", VCV Unity", etc.
If blank or undefined, the plugin name is used.

## `.author`

*String. Required.*

Your name, company, alias, GitHub username, etc.

## `.authorEmail`

*String. Optional.*

Your email address for support inquiries.

## `.authorUrl`

*String. Optional.*

Homepage for yourself or your company.

## `.pluginUrl`

*String. Optional.*

Homepage for the plugin itself.

## `.manualUrl`

*String. Optional.*

The manual of your plugin.
E.g. HTML, PDF, GitHub readme, GitHub wiki.

## `.sourceUrl`

*String. Optional.*

Homepage for the source code.
For GitHub URLs, use the main project page, not the `.git` URL.

## `.donateUrl`

*String. Optional.*

Link to donation page for users who wish to donate.
E.g. [PayPal.Me](https://www.paypal.me/), [Cash App](https://cash.app/) links.

## `.modules[].slug`

*String. Required.*

The unique identifier for the module.
Similar guidelines from [.slug](#slug) apply.

## `.modules[].name`

*String. Required.*

The human-readable name for the module.

## `.modules[].tags`

*Array of strings. Optional.*

List of tags representing the functions and/or properties of the module.
All tags must match the [list of allowed tags](https://github.com/VCVRack/Rack/blob/v1/src/plugin.cpp#L540) in Rack, case insensitive.

## `.modules[].description`

*String. Optional.*

A one-line summary of the module's purpose.
Displayed in the Module Browser tooltip.
