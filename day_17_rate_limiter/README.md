# Day 17 – API Rate Limiter (System Design)

## Overview
This project implements a rate limiter to protect APIs
from abuse using the Token Bucket algorithm.

---

## Why Rate Limiting?
Used by:
- Google APIs
- Amazon
- Payment gateways
- Cloud services

It prevents:
- DDoS attacks
- Server overload
- Abuse of free APIs

---

## Algorithm Used
Token Bucket Algorithm

Each user gets tokens per second.
When tokens are over, requests are blocked.

---

## How to Run
