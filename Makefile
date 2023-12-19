compile:
	osacompile -o send.scpt send.applescript
.PHONEY: compile

run: compile
	osascript send.scpt
.PHONEY: run