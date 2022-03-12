def get_coefficients(u):
	from math import floor
	get_grade0, n = define_algebra_operations(u)
	u_k = u
	n = 2**floor((n+1)/2)
	for k in range(1,n+1):
		c_k = get_c_k(n,k,u_k,get_grade0)
		yield c_k
		k += 1
		u_k = get_u_k(k,u,u_k,c_k)

def get_auxiliary(u):
	from math import floor
	get_grade0, n = define_algebra_operations(u)
	u_k = u
	n = 2**floor((n+1)/2)
	for k in range(1,n+1):
		c_k = get_c_k(n,k,u_k,get_grade0)
		yield u_k
		k += 1
		u_k = get_u_k(k,u,u_k,c_k)

def get_u_k(k,u,u_k,c_k):
	return u*(u_k-c_k)

def get_c_k(n,k,u_k,get_grade0 = lambda x: x[0]):
	return n/k*get_grade0(u_k)


def define_algebra_operations(u):
	u_data_type = str(type(u))
	if u_data_type == "<class 'clifford._multivector.MultiVector'>":
		get_grade0 = lambda x: x[0]
		n = len(u.layout.dims)

	elif u_data_type == "<class 'galgebra.mv.Mv'>":
		get_grade0 = lambda x: x.scalar()
		n = len(u.coords)
	else:
		print('Warning! Element U is not of implemneted data type')
	return get_grade0, n