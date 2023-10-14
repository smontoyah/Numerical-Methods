def TriDiagSys(a, b, c, d, n):
#----------------------------------------------------------------------------
#  Solves a system with tridiagonal matrix by LU factorization (diag(L) = 1).
#  a - lower co-diagonal (i=2,3,...n)
#  b - main diagonal (i=1,2,...n)
#  c - upper co-diagonal (i=1,2,...n-1)
#  d - constant terms; solution on exit
#  n - order of system.
#----------------------------------------------------------------------------
   if (b[1] == 0e0): print("TriDiagSys: singular matrix !"); return
   for i in range(2,n+1):                                     # factorization
      a[i] /= b[i-1]
      b[i] -= a[i]*c[i-1]
      if (b[i] == 0e0): print("TriDiagSys: singular matrix !"); return
      d[i] -= a[i]*d[i-1]

   d[n] /= b[n]                                       # backward substitution
   for i in range(n-1,0,-1): d[i] = (d[i] - c[i]*d[i+1])/b[i]