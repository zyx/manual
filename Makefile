
all: build

build: pdf
	gitbook build

run:
	gitbook serve --port 8080

pdf:
	gitbook pdf . VCV-Rack-manual.pdf

upload: all
	rsync _book/ vcvrack.com:vcvrack.com/manual/ -ruvz --delete

