# load and export .env
ifneq (,$(wildcard ./.env))
  include .env
  export
endif

compile:
	osacompile -o send.scpt send.applescript
.PHONEY: compile

run: report compile
	python3 send.py
.PHONEY: run

test: report compile
	TARGET=jeffreycaizhenyuan@gmail.com osascript send.scpt
.PHONEY: test

report:
	python3 make_report.py
.PHONEY: make_report

temp:
	echo ${TARGET} >> /tmp/testlog.txt
.PHONEY: temp
