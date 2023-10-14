def Spline(x, y, n, xi, yi, ni, a, b, c, d, d1, dn, iopt):
#----------------------------------------------------------------------------
#  Calculates the coefficients of the cubic splines for n data points and
#  returns interpolated values on a mesh of ni points
#
#  x[]  - x-coordinates of data points
#  y[]  - y-coordinates of data points
#  n    - number of data points
#  xi[] - x-coordinates of interpolation points (output)
#  yi[] - y-coordinates of interpolation points (output)
#  ni   - number of interpolation points
#  a[], b[], c[], d[], i=1,..,n-1
#       - coefficients of cubic splines on the n-1 subintervals (output)
#  d1   - first derivative at the left boundary x[1]
#  dn   - first derivative at the right boundary x[n]
#  iopt - iopt == 0, parabolic approximation of 1st derivative at boundaries
#          iopt != 0, considers d1 and dn as 1st derivatives at boundaries
#----------------------------------------------------------------------------
   if (iopt == 0):      # parabolic approximation of derivative at boundaries
      d1 = (y[2] - y[1])/(x[2] - x[1]) \
         - (y[3] - y[2])/(x[3] - x[2]) \
         + (y[3] - y[1])/(x[3] - x[1])
      dn = (y[n  ] - y[n-1])/(x[n  ] - x[n-1]) \
         - (y[n-1] - y[n-2])/(x[n-1] - x[n-2]) \
         + (y[n  ] - y[n-2])/(x[n  ] - x[n-2])

   hi = 0e0; di = d1       # coefficients of system for 2nd order derivatives
   for i in range(1,n):
      hm = hi; hi = x[i+1] - x[i]
      dm = di; di = (y[i+1] - y[i])/hi
      a[i] = hm; b[i] = 2e0*(hm + hi); c[i] = hi; d[i] = 6e0*(di - dm)

   a[n] = hi; b[n] = 2e0*hi; c[n] = 0e0; d[n] = 6e0*(dn - di)

   TriDiagSys(a,b,c,d,n)               # solve system with tridiagonal matrix (call from TriDiagSys.py)
                                       # solution: 2nd order derivatives in d
   for i in range(1,n):                             # coefficients of splines
      ip = i + 1
      xx = x[i]; xp = x[ip]; hi = xp - xx
      a[i] = (d[ip] - d[i]) / (6e0*hi)
      b[i] = (d[i]*xp - d[ip]*xx) / (2e0*hi)
      c[i] = (d[ip]*xx*xx - d[i]*xp*xp) / (2e0*hi) \
                                           + (y[ip] - y[i]) / hi - a[i]*hi*hi
      d[i] = (d[i]*xp*xp*xp - d[ip]*xx*xx*xx) / (6e0*hi) \
                                 + (y[i]*xp - y[ip]*xx) / hi - b[i]*hi*hi/3e0
   for i in range(1,ni):                    #  loop over interpolation points
      xx = xi[i]
      ip = 1
      while (xx > x[ip+1]): ip += 1                        #  index of spline
      yi[i] = ((a[ip]*xx + b[ip])*xx + c[ip])*xx + d[ip]   #  evaluate spline