PYTHON_VERSION=python3.5
DB=data/db.sqlite3
.PHONY: clean server shell


all: | env $(DB)

clean:
	rm -rf env
	rm -rf data/$(DB)

env:
	$(PYTHON_VERSION) -m venv env && \
	. env/bin/activate && \
	pip install -e . \
		ipython \
		coloredlogs

$(DB): | env
	. env/bin/activate && \
	info-display-cli migrate && \
	info-display-cli loaddata \
		login_data.json \
		station_data.json \
		calendar_data.json

db:
	rm $(DB) -rf && \
	$(MAKE) $(DB)

server: | env $(DB)
	. env/bin/activate && \
	. scripts/debug-env.sh && \
	info-display

shell: | env $(DB)
	. env/bin/activate && \
	. scripts/debug-env.sh && \
	info-display-cli shell

browser:
	./scripts/info-display-browser.py
