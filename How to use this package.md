# How to use this package

## Distribution package

The "Distribution" package can generate random numbers from a specific statistical distribution and calculate the mean and variance of the generated numbers. It contains 3 modules: exponential, normal and uniform. Each module has 3 functions: `generate()`, `mean()`, and `var()`. User will provide parameters for the .generate() function: `Exponential().generate(rate, n)`, `Normal().generate(mu, sigma, n)`, `Uniform().generate(lower, upper, n)`.

To generate 100 random numbers from normal distribution: `num = Normal().generate(0, 1, 100)`  
To calculate the mean of the 100 generated numbers: `num.get_mean()`  
To calculate the variance of the 100 generated numbers: `num.get_var()`

## Sequence package

Under the Package NumberGenerator, there are two subpackages. One of the subpackages is called Sequences.
Here is the list of functions that are in the three modules of Sequences:

def finite_series()

- Asks the user for the lower and upper bound
- generates the series for each of the three kinds of series (Triangle, Square, Pentagon)

def infinite_series()

- Asks the user for just the upper bound
- generates the series for each of the three kinds of series (Triangle, Square, Pentagon)

def mean(), def get_mean()

- Calculates the mean of the user-generated series

def Median(), def get_Median()

- Calculates the median of the user-generated series

def display()

- Helper function that customizes the user input interaction more visually appealing

def get_range()

- Gets lower and upper bound for number series generation
