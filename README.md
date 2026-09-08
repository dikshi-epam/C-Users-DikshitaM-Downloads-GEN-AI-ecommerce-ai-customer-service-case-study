# Streamlining E-commerce Customer Service with AI Chatbots

## Submission contents

- `agent/agent_spec.md`: prompt-engineered agent design, scope, guardrails, tools, and metrics.
- `agent/customer_service_agent.py`: dependency-free reference implementation with retrieval, sentiment/context handling, escalation, and auto-documentation.
- `data/knowledge_base.jsonl`: RAG source dataset representing an approved customer-service knowledge base.
- `data/golden_dataset.jsonl`: golden evaluation dataset with expected intent, grounding, escalation, and tone.
- `tests/test_agent.py`: executable regression and safety tests.
- `case_study.md`: business problem, solution approach, operating model, and rollout plan.

## Run

From this folder in PowerShell:

```powershell
python -m unittest discover -s tests -v
```

The implementation uses a deterministic local adapter so the submission runs without API keys. In production, replace the adapter with the approved LLM and vector-search provider while retaining the prompt, retrieval citations, guardrails, and evaluator contract.

## Share

Submit the `ecommerce-ai-customer-service-case-study` folder or zip it. The RAG dataset and golden dataset are both included as JSON Lines files and can be imported into an agent platform or evaluation harness.

## Live documentation integration

`ConversationDocumenter` is the live-tool boundary. The reference implementation writes each conversation event to `runtime/conversation_log.jsonl`, including redacted customer text, intent, sentiment, citations, action, and escalation status. In production this boundary can call Confluence, SharePoint, Salesforce, or a ticketing API with the same event schema.

## Production prerequisites

Use authenticated retrieval over approved first-party content, an order-management API for account-specific actions, a ticketing system for escalation, PII redaction, audit logging, access controls, rate limits, and human review for high-risk cases. Do not expose the local deterministic adapter as a customer-facing model.
