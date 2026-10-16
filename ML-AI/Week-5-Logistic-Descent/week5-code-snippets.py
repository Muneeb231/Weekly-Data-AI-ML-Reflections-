'''
sig:
g = 1 / (1+np.exp(-1*z))

cost:
z = lambda i: np.dot(w,X[i]) + b
f = lambda i: 1 / (1+np.exp(-1*z(i)))

loss = lambda i: ((-y[i] * np.log(f(i))) - ((1-y[i])*np.log(1-f(i))))

total_cost = 0
for i in range(m):
    total_cost += loss(i)
    
total_cost = total_cost /m






'''
