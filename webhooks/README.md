# Webhook Notes

Typical public webhook use cases include:

- job completion notifications
- failure notifications
- artifact availability events

Recommended validation posture:

- verify event signatures
- separate sandbox and production endpoints
- treat webhook payloads as untrusted input
- log event IDs for replay protection
