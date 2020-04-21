# Bayesian-inference
Bayesian inference for the given Data


## Objective: Bayesian inference on the given data.

## Problem: Bayesian network is a directed acyclic graphical representation of a set of variables and their conditional dependencies. Each variable is represented as a node in the graph and a directed edge between the nodes represents parent-child relationship between the considered nodes. In this assignment we will estimate probability distributions or parameters of a given network. For this, we will make use of a dataset containing samples comprising of values observed for different variables.

## Input
Two text files will be as input to your program, which will contain
input1
• Line 1: n : no. of variable or nodes (N1, N2, ...., Nn)
• Line 2 to Line n + 1: Comma separated list of all possible values of variables N1 to Nn
• Line n + 2 to Line 2n + 1: n × n matrix of 1’s and 0’s representing conditional dependencies, e.g. a value 1 at location (3,2) shows that N2 is conditionally dependent on N3 input2 Comma separated CSV file. First Line contains names of the  variables and remaining lines contain the list of samples comprising of values observed for all variables (N1, N2, ...., Nn) for each sample.

## Sample input:
input1
3
TRUE, FALSE
TRUE, FALSE
TRUE, FALSE
0 0 1
0 0 1
0 0 0
input2
N1, N2, N3
TRUE, FALSE, TRUE
FALSE, TRUE, FALSE
.
.
.
.
1
.
There are three binary variables (N1, N2, N3) in this Bayesian network where N3 is conditionally dependent on N1 and N2. In other words, N1 and N2 are the parents of N3.

## Output
Your program should learn the parameters (probability distributions of each variable) of the given network and return them in the following formatOutput format: Output file should have n lines where Line 1 will contain probability distribution of variable N1, Line 2 will contain probability distribution of variable N2and so on For the above problem the output is
0.2 0.8
0.4 0.6
0.2 0.4 0.3 0.5 0.8 0.6 0.7 0.5

This implies P(N1=TRUE) = 0.2, and P(N1=FALSE) = 0.8. Similarly P(N2=TRUE) = 0.4, and P(N2=FALSE) = 0.6. Further, P(N3=TRUE|N1=TRUE, N2=TRUE) = 0.2,P(N3=TRUE|N1=TRUE, N2=FALSE) = 0.4, P(N3=TRUE|N1=FALSE, N2=TRUE) =0.3 and so on.


