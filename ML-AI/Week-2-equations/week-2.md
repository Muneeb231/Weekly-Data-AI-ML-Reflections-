# Week 2

## Week 2 Data Reflections — DML vs DDL

This week I learned about DML (Data Manipulation Language) keywords: UPDATE, INSERT INTO, and DELETE FROM. Unlike DDL (Data Definition Language), which changes the structure of a database (tables, columns, schemas), DML changes the contents of the data.

I also learned how to maintain referential integrity when deleting data. One useful tool for this is ON DELETE CASCADE: when a row is deleted in the primary table, any rows in other tables that reference it via a foreign key are automatically deleted too. An example of ON DELETE CASCADE is as follows:

## Week 2 AI/ML Reflections — One Pager

### Context
Went through more of the AI Specialization Course from Stanford Deeplearning.AI. Went through numpy basics, labs, cost function, and gradient descent.


#### 1. Linear Regression Model Function
$$f_{w,b}(x^{(i)}) = wx^{(i)} + b$$

#### 2. Cost Function (Mean Squared Error)
$$J(w,b) = \frac{1}{2m} \sum_{i=0}^{m-1} \left( f_{w,b}(x^{(i)}) - y^{(i)} \right)^2$$

#### 3. Gradient Descent Algorithm
$$ repeat until convergence \ $$
$$ w = w - \alpha \frac{\partial J(w,b)}{\partial w} $$
$$ b = b - \alpha \frac{\partial J(w,b)}{\partial b} $$
$$ \ $$

#### 4. Gradient Calculations (Partial Derivatives)
$$\frac{\partial J(w,b)}{\partial w} = \frac{1}{m} \sum_{i=0}^{m-1} \left( f_{w,b}(x^{(i)}) - y^{(i)} \right) x^{(i)}$$

$$\frac{\partial J(w,b)}{\partial b} = \frac{1}{m} \sum_{i=0}^{m-1} \left( f_{w,b}(x^{(i)}) - y^{(i)} \right)$$
