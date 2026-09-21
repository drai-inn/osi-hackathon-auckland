# Light by design. Standard library only, so anything here runs on day 1.

.PHONY: help check cards card-geometry figures poster

help:
	@echo "check    every relative link and anchor in the markdown"
	@echo "cards    regenerate the four theme cards"
	@echo "figures  regenerate the structural figures (needs biopython + numpy)"
	@echo "poster   rebuild the A3 poster PDF from outreach/poster.html"

check:
	python3 tools/check_links.py --self-test
	python3 tools/check_links.py

cards:
	python3 tools/make_cards.py

card-geometry:            ## refresh the real coordinates the cards draw from
	python3 tools/extract_card_geometry.py

figures:
	python3 tools/render_structures.py
	python3 tools/render_components.py

poster:
	@command -v chrome >/dev/null 2>&1 && CHROME=chrome || CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; \
	"$$CHROME" --headless --disable-gpu --no-pdf-header-footer \
	  --print-to-pdf=outreach/poster-A3.pdf "file://$$PWD/outreach/poster.html"
	@echo "wrote outreach/poster-A3.pdf"
