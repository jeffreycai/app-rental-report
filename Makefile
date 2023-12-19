compile:
	osacompile -o send.scpt send.applescript
.PHONEY: compile

run: compile
	osascript send.scpt
.PHONEY: run

make_report:
	python3 make_report.py
.PHONEY: make_report
