# neurocad-examples

[![Example Validation](https://github.com/neurocad-eu/neurocad-examples/actions/workflows/validate.yml/badge.svg)](https://github.com/neurocad-eu/neurocad-examples/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/neurocad-eu/neurocad-examples)](https://github.com/neurocad-eu/neurocad-examples/releases)

Reference integration examples and usage patterns for NeuroCAD.

## Purpose

This repository contains minimal public examples that show how external systems can interact with the NeuroCAD integration surface.

It is intended for:

- enterprise solution architects
- partner engineering teams
- internal integration reviewers
- technical diligence workflows

## Included

- Python example client flow
- curl-based job submission example
- webhook handling notes
- notebook-oriented usage guidance
- JavaScript example client
- local environment example
- minimal webhook receiver
- sandbox smoke-test checklist

## Excluded

This repository does not expose production credentials, private infrastructure, or proprietary kernel internals.

## Status

Public example surface in active hardening.

Examples are aligned with the draft public API contract published in `neurocad-api-docs` and are intended for sandbox-first integration review.

## Repository layout

- `python/` Python reference clients
- `javascript/` JavaScript reference clients
- `curl/` shell-first examples
- `webhooks/` receiver patterns
- `notebooks/` notebook-oriented quickstarts
- `docs/` integration and smoke-test notes

## Recommended use

Start with:

1. `neurocad-api-docs/openapi/openapi.yaml`
2. `curl/submit_job.sh`
3. `javascript/submit_job.mjs`
4. `python/submit_job.py`
5. `docs/sandbox-smoke-test.md`
