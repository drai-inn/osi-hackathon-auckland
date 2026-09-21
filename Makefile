# Light by design. Standard library only, so anything here runs on day 1.

.PHONY: help check cards figures

help:
	@echo "check    every relative link and anchor in the markdown"
	@echo "cards    regenerate the four theme cards"
	@echo "figures  regenerate the structural figures (needs biopython + numpy)"

check:
	python3 tools/check_links.py --self-test
	python3 tools/check_links.py

cards:
	python3 tools/make_cards.py

figures:
	python3 tools/render_structures.py
	python3 tools/render_components.py
