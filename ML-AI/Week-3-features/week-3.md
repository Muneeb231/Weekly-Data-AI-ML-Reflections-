# Week 3

## Week 3 AI/ML Reflections — Learning Updates

### Context

Continued through the course, learn allot this week. Batch Gradient Descent, Multiple Features, Vector representations of features and weights, Multiple Linear Regression. Also learned about Vectorization and Numpy Library.

Normal Equation - for lin regression only - Solving for w, b without iteration. -- slow -- does not generalize --slow with large features

General Rule* - if a features potential values are small, its weight will generally be large and viceversa.

#### Feature Size and Gradient descent
- if your features differ allot in their amplitute (ie one ranges from 0 to 1 and another feature ranges from -1m to +10m) the weights for each feature will be very different. Meaning that the contour of weights will be skewed and it will be hard for your algorithm to find the minimum. It is more difficult as it will be more volitile to changes and can make the cost jump around after each descent iteration. leading to large convergence times.

- the solution for this is called **Feature Scaling**, this method allows us to scale features to similar ranges so that the weights can also be distributed "evenly" and will be more similar. This makes it easier for our gradient descent to find the minimum cost in an optimal amount of time.
  - I can think of one example, imagine two bowls, one is a perfect concave, the second has bumps and protruding edges and varies in gradient and contour. If you put syrup on each of the edges, which one logically will reach the bottom of their respective bowls the fastest? the smooth and perfectly concave one obviously. The same intuition goes for the features and gradient descent. The more even and uniform the feature ranges, the more smooth the descent will eventually be.

##### Some methods for feature scaling:
(note: these will run on each of the features in the set of features, scaling them to a similar range)

  - Mean normalization:
    - find μ (mu) : this is the average of all of the inputs of that specific feature
    - find the max of that features values
    - find the min of that features values

    - Alg is: (xi - μ) / (max(xi) - min(xi))
    - this results in a even input of that feature being ranged from -1 to 1 centered around 0


  - Z-score normalization:
    - find σ (sig) : thias is the standard deviation of that feature across its inputs
    - find mu : same as above
    - alg is : (xij - μ) / σ

    - this gives you a slightly more forgiving range (without the hard bounds of mean norm.) that is again, centered around 0

##### general points
almost no harm in feature scaling

Check for convergence:
- J(W->, b) should decrease after every iteration
- can do a convergence test, ie set e and then test if J (cost func) decreases by less than that then you have converged
- checking the learning curve may be more robust


How to choose the Learning Rate (α):
- G.D. should decr. after each iteration
- if α is small and J still jumps up and down there may be a bug in the code
- can use an iterative approach



#### Feature Engineering
Feature engineering is the practice of combining or modifying features based off of intuition of what may be helpful in the model.


#### Polynomial Regression
 when dealing with features to the "power of" ie xij^2 xij^4 etc, feature scaling becomes more important as the weights of each feature matter more. ie each change to a weight multiplies and changes the function more and more as the power grows.

y = price
predicted price is = y^

x1 = sq footage - weight small
x2 = age - weight large

- if both influence equally

to solve this:
feature scaling
