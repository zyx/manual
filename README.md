# VCV Rack Manual

The scope of the manual is the VCV Rack application. It does not include individual plugins for Rack---those should be documented and hosted by the plugin developer.

### Contributions

Send a pull request to this repository with your edits.
Major changes like new pages and complete overhauls are welcome, as well as minor fixes like grammar, spelling, and reorganization.
Your PR will be accepted if it is a net positive benefit to readers.

### Building

Install [Node](https://nodejs.org/en/). Make sure `npm` is in your PATH.

Install [gitbook](https://github.com/GitbookIO/gitbook) with

	npm install gitbook-cli -g

Install gitbook plugins with

	gitbook install

Build with

	make run

and preview the manual at http://localhost:8080/.
