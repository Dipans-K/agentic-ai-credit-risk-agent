import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -40, 40)))


def probability_of_default(features, beta):
    return float(sigmoid(np.dot(features, beta)))


def bayesian_update(prior, likelihood_good, likelihood_bad):
    numerator = prior * likelihood_good
    return float(numerator / (numerator + (1-prior) * likelihood_bad))


def expected_loss(pd, lgd, ead):
    return float(pd * lgd * ead)


def markov_next(probabilities, state):
    return float(np.asarray(state) @ np.asarray(probabilities))


def agent():
    pd = probability_of_default([1, .4, -.2], [-1.2, 1.1, .8])
    posterior = bayesian_update(pd, .25, .75)
    loss = expected_loss(posterior, .45, 100000)
    return {"pd": pd, "posterior_pd": posterior, "expected_loss": loss}


if __name__ == "__main__":
    print(agent())
