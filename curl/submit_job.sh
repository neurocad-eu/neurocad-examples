#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${BASE_URL:-https://sandbox.api.neurocad.eu}"
TOKEN="${TOKEN:-replace-me}"

curl -sS \
  -X POST "${BASE_URL}/v1/inference/jobs" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d @- <<JSON
{
  "project_id": "prj_demo_001",
  "task": "mesh-generation",
  "input": {
    "material": "steel-a36",
    "resolution": "medium"
  },
  "labels": ["public-curl-example"]
}
JSON
