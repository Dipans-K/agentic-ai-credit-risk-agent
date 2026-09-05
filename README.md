# Agentic AI Credit Risk Agent

An auditable credit-risk Agentic AI prototype combining logistic probability of default, Bayesian evidence updates, Markov transitions, and expected-loss calculations.

## Mathematics
- Logistic PD: σ(xᵀβ)
- Bayesian posterior updates
- Markov transition matrices
- Expected loss = PD × LGD × EAD
- Threshold and risk-policy validation

## Agent Workflow
Planner → Credit Feature Analyst → PD Model → Bayesian Evidence Tool → Markov Risk Tool → Policy Validator → Decision Synthesizer

## Run
```bash
pip install -r requirements.txt
python -m src.main
pytest -q
```

## Structure
`src/` agents/tools · `tests/` tests · `data/` sample applications · `docs/` mathematical formulation and architecture · `notebooks/` analysis · `results/` outputs.

## Interview topics
Probability of default, Bayes theorem, Markov chains, calibration, expected loss, risk thresholds, explainability, guardrails, and agentic tool selection.
