compile:
	osacompile -o send.scpt send.applescript
.PHONEY: compile

run: report compile
	python3 send.py
.PHONEY: run

report:
	python3 make_report.py
.PHONEY: make_report
