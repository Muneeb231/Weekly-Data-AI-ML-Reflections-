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



gradient:
for i in range(m):
z_wb = 0
for j in range(n): 
    z_wb += w[j]*X[i][j]
z_wb += b
f_wb = 1 / (1+np.exp(-z_wb))

dj_db_i = f_wb - y[i]
dj_db += dj_db_i

for j in range(n):
    dj_dw[j] += (f_wb-y[i]) * X[i][j]
    
dj_dw = dj_dw/m
dj_db = dj_db/m



prediction function:
    for i in range(m):   
        z_wb = 0
        # Loop over each feature
        for j in range(n): 
            # Add the corresponding term to z_wb
            z_wb += w[j] * X[i][j]
        
        # Add bias term 
        z_wb += b
        
        # Calculate the prediction for this example
        f_wb = sigmoid(z_wb)

        # Apply the threshold
        p[i] = 1 if f_wb >= 0.5 else 0






'''
