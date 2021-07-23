def get_coefficients(n,u,get_grade0):
	u_k = u
	n = pow(2, (n+1)//2)
	for k in range(1,n):
		c_k = get_c_k(n,k,u_k,get_grade0)
		yield c_k
		k += 1
		u_k = get_u_k(k,u,u_k,c_k)

def get_u_k(k,u,u_k,c_k):
	return u*(u_k-c_k)

def get_c_k(n,k,u_k,get_grade0):
	return n/k*get_grade0(u_k)