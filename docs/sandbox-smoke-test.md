# Sandbox Smoke Test

## Goal

Run a minimal end-to-end check against the public sandbox contract without introducing private infrastructure dependencies.

## Sequence

1. set `BASE_URL=https://sandbox.api.neurocad.eu`
2. obtain a sandbox bearer token
3. submit one low-risk public example job
4. poll job state until terminal status
5. resolve returned artifact identifiers

## Expected checks

- authentication exchange succeeds
- job submission returns `202`
- job polling returns stable status transitions
- artifact metadata resolves with stable IDs

## Failure handling

If the smoke test fails, capture:

- request path
- response code
- response body
- environment
- correlation or request identifiers when available
