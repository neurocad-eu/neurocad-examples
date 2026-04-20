"""Reference example for submitting a NeuroCAD job from Python."""

from __future__ import annotations

import json
from urllib import request


BASE_URL = "https://sandbox.api.neurocad.eu"
TOKEN = "replace-me"


def submit_solver_export(project_id: str) -> dict:
    payload = {
        "project_id": project_id,
        "task": "solver-export",
        "input": {
            "material": "aluminum-6061",
            "export_format": "solver-bundle",
            "quality_profile": "balanced",
        },
        "labels": ["public-reference"],
    }

    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }
    req = request.Request(
        f"{BASE_URL}/v1/inference/jobs",
        data=data,
        headers=headers,
        method="POST",
    )
    with request.urlopen(req) as response:  # noqa: S310 - example only
        return json.loads(response.read().decode("utf-8"))


if __name__ == "__main__":
    print("Reference example. Replace TOKEN before use.")
    result = submit_solver_export("prj_demo_001")
    print(json.dumps(result, indent=2))
