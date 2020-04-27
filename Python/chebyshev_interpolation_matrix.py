
"""
    @author: thehalfspace
    Reference: Spectral Methods by J.P. Boyd
"""

def chebyshev_interpolation_matrix(n=None):
    """ Interpolate any single-variable function as a Chebyshev Polynomial
        
        Input parameters:
        ----------------
            n:  int
                number of points in the interpolation,
                
        Returns:
        --------
            x: interpolation points
            M: Chebyshev matrix

    
    np.dot(np.linalg.inv(M), f(x)) will give you any interpolated function f
    as linear combination of chebyshev polynomials
    """
    
    if type(n) != int: 
        raise ValueError("n must be integer")

    from numpy import ones, pi, linspace, cos
        
    theta = linspace(0.0,1.0,n)*pi
    x = cos(theta)

    # Create the chebyshev matrix
    M = ones((n,n))
    for i in range(n):
        for j in range(n):
            M[i,j] = cos(i*theta[j])

    return x, M
