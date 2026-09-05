from src.main import probability_of_default, bayesian_update, expected_loss


def test_pd_range():
    p = probability_of_default([1,.4,-.2], [-1.2,1.1,.8])
    assert 0 < p < 1


def test_bayes_and_loss():
    p = bayesian_update(.1,.25,.75)
    assert 0 < p < .1
    assert expected_loss(p,.45,100000) > 0
