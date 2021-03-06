""" Default configuration and hyperparameter values for algorithms. """

ALGconfig = {
    'method': "dummy",
    'iterations': 100,
    'eta': 0.01,  # learning rate
    'discount': 1.0,
    'absErr': 1.0e-3,
    'nAbsErr': 1,
    'eval_valid_in_iters': False,
    'eval_test_in_iters': False,
    'update_by': 'episode',  # batch, episode, step
}
