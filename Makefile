# Scoping-stage Makefile. Grows as WP-F lands the real workflow.

MANIFEST ?= data/manifest/benchmark_v0.example.csv
TIER     ?= hackathon_minimum

.PHONY: help validate budget links check smoke

help:
	@echo "validate   validate a manifest        (MANIFEST=path)"
	@echo "budget     estimate GPU-hours         (TIER=tiny_smoke_test|hackathon_minimum|useful_pilot|scale_up)"
	@echo "links      check every relative link and anchor in the markdown"
	@echo "check      run every check in the repo"
	@echo "smoke      five synthetic pairs through every stage  [WP-F, day 1 -- not implemented]"

validate:
	python3 tools/validate_manifest.py $(MANIFEST)

budget:
	python3 tools/compute_budget.py $(TIER)

links:
	python3 tools/check_links.py --self-test
	python3 tools/check_links.py

check: validate links
	@python3 tools/compute_budget.py > /dev/null && echo "compute_budget.py OK"

smoke:
	@echo "not implemented -- WP-F ships this on day 1 of the hackathon."
	@echo "See workflow/README.md and docs/02-pipeline/stages/S8-orchestration.md"
	@exit 1
