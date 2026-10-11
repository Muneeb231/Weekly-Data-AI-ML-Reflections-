# Week 1

## Week 1 Data Reflections — My Process for Designing a Database

**Context**

This week I worked through a problem set from Harvard's CS50 Databases course involving an airport system. The database included modeling passengers, flights, airlines, and concourses. Rather than just posting the final schema, I wanted to document the process I used to get there, since that's the part that's actually reusable on future projects.

**The Process**
1) List your entities: Passengers, Flights, Airlines, Concourses.
2) For every pair of entities, ask: "is there a real-world relationship here?"
Passenger ↔ Flight — yes, obviously.
Passenger ↔ Airline — not directly; only indirectly through their flight.
Flight ↔ Airline — yes, one airline operates a flight.
3) For each real relationship, figure out the cardinality. Is it one-to-one, one-to-many, or many-to-many?
Passenger ↔ Flight is many-to-many: one passenger can take many flights over time, and one flight has many passengers.
4) Design the database based off of the cardinality:
Many-to-many → needs a junction table that includes the foreign key to reference both tables.
One-to-many → the foreign key goes on the "many" side.

**Key Takeaway**
Steps 1–3 are really about thinking in relationships before thinking in tables. It's tempting to jump straight to "what tables do I need," but starting from entities and asking honestly whether a relationship exists (and what shape it is) avoids a lot of schema rework later.

## Week 1 AI/ML Reflections — One Pager

### **Context**

Currently working through the DeepLearning.ai ML Specialization courses. Week one goes through the basics of ML. Definitions like what is Supervised Learning, Unsupervised Learning, and common types of both of those.

Along with the ML Specialization course, I reviewed my notes on important mathematics in regards to ML. Matricies and their related mathematics, Calculus, and common functions as part of week 1.

### **Notes and Summries**

#### General Notes
- Supervised Learning = Learning based on inputs and outputs. Gives a prediction of an output based on its given labeled data.
  - Types: 
    - Regression - Predicts a number, inf possible outcomes
    - Classification - Predicts Categories, finite possbile outcomes

- Unsupervised Learning = Learning based on given unlabeled data, predicts patterns
  - Types:
    - Clustering - Groups data into categories, finds patterns based off of raw data. Used in marketing, ads, etc.

- Cost = tells machine how wrong it is
  - \# of errrors / # of predictions
- The study of machine learning can be oversimplified to the minimization of the cost function. 

#### Matrices
Dot product:

Given two vectors:
* $\mathbf{A} = [1, 2]$
* $\mathbf{B} = [2, 4]$

The dot product $\mathbf{A} \cdot \mathbf{B}$ is calculated as:

$$\mathbf{A} \cdot \mathbf{B} = (1 \times 2) + (2 \times 4)$$
$$\mathbf{A} \cdot \mathbf{B} = 2 + 8$$
$$\mathbf{A} \cdot \mathbf{B} = 10$$


#### Calculus
