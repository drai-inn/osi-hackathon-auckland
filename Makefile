# Light by design. Standard library only, so anything here runs on day 1.

.PHONY: help check cards figures poster site pages

help:
	@echo "check    every relative link and anchor in the markdown"
	@echo "cards    regenerate the four theme cards"
	@echo "figures  regenerate the structural figures (needs biopython + numpy)"
	@echo "poster   rebuild the A3 poster PDF from outreach/poster.html"
	@echo "site     build the GitHub Pages site into _site/"
	@echo "pages    build and publish _site/ to the gh-pages branch"

check:
	python3 tools/check_links.py --self-test
	python3 tools/check_links.py

cards:
	python3 tools/make_cards.py

figures:
	python3 tools/render_structures.py
	python3 tools/render_components.py

poster:
	@command -v chrome >/dev/null 2>&1 && CHROME=chrome || CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; \
	"$$CHROME" --headless --disable-gpu --no-pdf-header-footer \
	  --print-to-pdf=outreach/poster-A3.pdf "file://$$PWD/outreach/poster.html"
	@echo "wrote outreach/poster-A3.pdf"

site:
	python3 tools/build_site.py

pages: site
	@git rev-parse --verify gh-pages >/dev/null 2>&1 || git branch gh-pages $$(git commit-tree $$(git hash-object -t tree /dev/null) -m "init gh-pages")
	@cd _site && git init -q . && git add -A && git -c user.email=noreply@auckland.ac.nz -c user.name="pages build" commit -qm "Publish site" && git push -qf https://github.com/drai-inn/osi-hackathon-auckland.git HEAD:gh-pages && rm -rf .git
	@echo "published -> https://drai-inn.github.io/osi-hackathon-auckland/"
