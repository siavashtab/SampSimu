
Sampling techniques for simulation and generating random sample

Author: Siavash Tabrizian - stabrizian@smu.edu

---------
There are different sampling techniques can be used in order to generate sample. This package helps 
the user to generate samples with three methods::

1 - Crude Monte Carlo sampling:

The unbiased sample mean estimator $\bar{x} = \frac{\sum x_i}{n}$ can be used in this case in order to estimate the mean $\mu$.
In this sampling technique, in order to obtain $n$ number of samples, first $$n$$ random numbers should be generated from the $$\big[0,1\big]^d$$ where $$d$$ is the number of random variables, and after that  using the CDF, values can be taken from the distribution. 

Sampling steps for generating $n$ samples:

~~~
For i < n:
	1. build the cumulative distribution of the random variable (CDF)
	2. draw a random number from [0,1] interval = r
	3. find the value of the random variable for r using the CDF
~~~

======================================

2 - Antithetic Sampling 

In this sampling technique, in order to obtain $n$ number of samples, first $$n/2$$ random numbers should be generated from the $$r_1 = \big[0,1\big]^d$$ where $$d$$ is the number of random variables, and after that  using the CDF, values can be taken from the distribution using $r_1$ and $1-r_1$. 


Sampling steps:

~~~
For i < n/2:
	1. build the cumulative distribution of the random variable (CDF)
	2. draw a random number from [0,1] interval = r
	3. find the value of the random variable for r using the CDF
	3. find the value of the random variable for 1-r using the CDF
~~~

=======



