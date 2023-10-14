# Numerical Methods Repository

This repository contains Python scripts for various numerical methods and simulations developed during the course "Computational Methods for physicists" at University of Antioquia in 2017. Each script is designed to solve specific mathematical or physical problems. Below, you'll find a brief overview of each script and its key features.

## Tridiagonal System Solver

**File:** `TriDiagSys.py`

**Description:** This code solves a system of equations with a tridiagonal matrix using LU factorization. It works for systems where the diagonal elements are not zero. The inputs are a (lower co-diagonal), b (main diagonal), c (upper co-diagonal), d (constant terms), and n (order of the system).

## Cubic Spline Interpolation

**File:** `SplineInterpolation.py`

**Description:** This code calculates the coefficients of cubic splines for a set of data points and returns interpolated values for a given set of interpolation points. It allows you to specify the first derivatives at the boundaries or use a parabolic approximation.

## Gaussian Quadrature Integration

**File:** `GaussianIntegration.py`

**Description:** This code implements Gaussian quadrature for numerical integration, providing accurate approximations for definite integrals of a given function over a specified interval.

## Monkey Hunter Simulation

**File:** `MonkeyHunterSimulation.py`

**Description:** This code simulates a scenario where a hunter aims to shoot a monkey in a tree. It uses basic physics principles to calculate the trajectories of a bullet and the falling monkey, and creates a 3D graphical representation of the simulation.

## Kepler's Equation Solver

**File:** `KeplersEquationSolver.py`

**Description:** This code implements the bisection algorithm to solve Kepler's equation, used for celestial objects in elliptical orbits. It includes an application to compute the eccentric anomaly for Halley's Comet.

## Numerical Root Finding Methods

**File:** `RootFindingMethods.py`

**Description:** This code demonstrates and implements various numerical methods for finding roots of a given function, including Secant, Bisection, and Newton's methods.

## Lagrange Polynomial Interpolation

**File:** `LagrangeInterpolation.py`

**Description:** This code demonstrates Lagrange polynomial interpolation, a method for approximating a function based on a set of discrete data points.

## Numerical Integration Methods

**File:** `NumericalIntegration.py`

**Description:** This code performs numerical integration of a given function using the trapezoid and Simpson methods, comparing the results with the analytical solution.

## Von Neumann Numerical Integration

**File:** `VonNeumannIntegration.py`

**Description:** This code implements Von Neumann's numerical integration method to calculate the area between two curves and provides an interactive visualization of the process.

## Harmonic Motion with Euler's Method

**File:** `HarmonicMotionWithEuler.py`

**Description:** This code simulates harmonic motion using Euler's method, both with and without the presence of friction, allowing for different initial conditions.

## 2D Rossler Attractor

**File:** `2DRosslerAttractor.py`

**Description:** This code simulates the 2D Rossler attractor using the Runge-Kutta method and provides graphical representations of the system's behavior.

## Random 2D Path with Exponential Steps

**File:** `Random2DPathWithExponentialSteps.py`

**Description:** This code generates a random 2D path with exponential step lengths, controlled by the parameter lambda (λ), and visualizes the path in 3D.

## Solving Systems of ODEs with RK4

**File:** `RK4_Solving_System.py`

**Description:** This code uses the RK4 method to solve systems of ordinary differential equations (ODEs).

## Gravitational Simulation Earth

**File:** `GravitationalSimulationEarth.py`

**Description:** This script simulates the motion of a particle in a gravitational field created by Earth's layers, accounting for changes in density and volume as the particle moves through the Earth.

Each script is designed to address specific mathematical or physical problems and provides a clear explanation of its purpose and usage. Feel free to explore and use these scripts for your numerical analysis needs.
