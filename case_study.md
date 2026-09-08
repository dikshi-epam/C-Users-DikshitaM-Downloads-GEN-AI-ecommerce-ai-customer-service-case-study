# Case Study: AI Customer Service Chatbot

## Business problem

A high volume of repetitive e-commerce inquiries creates long wait times, inconsistent answers, customer dissatisfaction, and avoidable operating cost.

## Automation scope

Automate low-risk, repeatable questions: order-status guidance, shipping estimates, returns policy, cancellation eligibility, payment-method information, and basic product availability. The bot may explain policy and collect information, but it must not invent order data, approve exceptions, issue refunds, or change an order without an authenticated tool result.

Keep these cases human-led: suspected fraud, account takeover, chargebacks, legal threats, safety issues, accessibility complaints, abusive interactions, vulnerable customers, and any request requiring an exception or unavailable customer record.

## Datasets

The RAG dataset is `data/knowledge_base.jsonl`. It contains approved policy records with stable IDs, effective dates, text, and source labels. The golden dataset is `data/golden_dataset.jsonl`; it is held out from retrieval during evaluation and contains representative requests plus expected behavior.

## Agent design

A single customer-facing agent uses a retrieve-then-answer flow. It classifies intent and sentiment, retrieves approved records, checks whether the request is within scope, answers with citations, and documents the event. A judge evaluates groundedness, intent handling, escalation correctness, and tone. A human agent remains the authority for exceptions and sensitive cases.

## Success metrics

- 80% or higher containment for in-scope routine contacts after 30 days.
- 95% or higher grounded-answer rate, measured by citation and claim review.
- 98% or higher correct escalation rate on high-risk golden cases.
- 90% or higher customer satisfaction on bot-contained sessions.
- 20% reduction in cost per resolved contact without increasing reopen rate.
- P95 first response under 3 seconds for retrieval and response orchestration.

## Testing strategy

Run unit tests for classification, retrieval, sentiment, prompt-injection resistance, PII redaction, escalation, and documentation. Run golden-set evaluation on every prompt or retrieval change. Add adversarial tests for instruction overrides, fabricated order details, unsupported policy claims, and requests for restricted actions. In production, sample sessions for human review and compare containment, CSAT, escalation precision/recall, groundedness, and safety incidents against a baseline.

## Rollout

Pilot with a limited traffic slice and read-only capabilities. Monitor failures daily, update the approved knowledge base through content governance, then add authenticated order lookup and ticket creation only after safety thresholds hold. Keep a visible handoff path and preserve the full audit event for every session.
