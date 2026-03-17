def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    x=0
    for i in range(steps):
        f_dash = 2*a*x + b
        
        x = x - lr * f_dash

    return x