# Week 4 Classification

As clasification is a different type of supervised learning, Classification needs a new algorithm
A decision boundary is the threshold of what the classification of a value is.

## Logistic Regression

- used for classification

Uses a sigmoid function:
$$g(z) = \frac{1}{1 + e^{-z}}$$
  - outputs between 0 and 1
  - $e$ is eulers number $e \approx 2.71828$ : 
    - base for natural log

Logistic regression is just the function $f_{\mathbf{w},b}(\mathbf{x})$ inputted into z
 - this outputs the sigmoid around the descision barrier

$$g(z) = z = \boldsymbol{w}^\top \mathbf{x} + b \implies g(\boldsymbol{w}^\top \mathbf{x} + b) = \frac{1}{1 + e^{-(\boldsymbol{w}^\top \mathbf{x} + b)}}$$
  where $\mathbf{w}$ and $\mathbf{x}$ are vectors
  - outputs between 0 and 1
    - this is the certainty of the prediction


if z is large then it is 1 over a small number meaning close to 1 and vice versa

## Descision boundaries

the boundary between classes, if there are groups the algorithm descides based on the descision boundary
ie boundary can be 0.5 then if y^ is above that then its one class and below then its another



## Cost funciton for Logistic Regression

Logistic Loss function (piecewise):

$$\text{cost}(f_{\boldsymbol{w},b}(\mathbf{x}^{(i)}), y^{(i)}) = \begin{cases} -\log(f_{\boldsymbol{w},b}(\mathbf{x}^{(i)})) & \text{if } y^{(i)} = 1 \\ -\log(1 - f_{\boldsymbol{w},b}(\mathbf{x}^{(i)})) & \text{if } y^{(i)} = 0 \end{cases}$$


loss is how well you are doing on a specific training ex and cost is how well you are doing on the whole thing


Cost for Log Reg:
$$J(\boldsymbol{w}, b) = \frac{1}{m} \sum_{i=1}^{m} \text{cost}(f_{\boldsymbol{w},b}(\mathbf{x}^{(i)}), y^{(i)})$$



