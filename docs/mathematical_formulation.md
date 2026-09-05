# Mathematical Formulation

Probability of default is modeled with `PD = σ(xᵀβ)`. New evidence updates the prior through Bayes' theorem. Credit migration can be represented as a Markov chain `p_next = p_current P`.

Expected loss is `EL = PD × LGD × EAD`. The policy validator can apply approval thresholds and produce an auditable decision.
