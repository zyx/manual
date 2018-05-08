
build:
	gitbook build

all: build pdf

run:
	gitbook serve --port 8080

pdf: build
	gitbook pdf . _book/VCV-Rack-manual.pdf

upload: all
	rsync _book/ vcvrack.com:vcvrack.com/manual/ -ruvz --delete
