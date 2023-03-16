.SILENT:
args = `arg="$(filter-out $@,$(MAKECMDGOALS))" && echo $${arg:-${1}}`

init:
	cp config.ini.public config.ini
	python3 -m venv venv && . venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

audio_to_text:
	. venv/bin/activate && python3 audio_to_text.py $(call args)

text_to_actions_list:
	. venv/bin/activate && python3 text_to_actions_list.py $(call args)
