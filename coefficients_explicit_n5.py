def get_coefficients(u):
	arguments = calc_conjugations(u)
	yield sum(n5_c1(*arguments))
	yield sum(n5_c2(*arguments))
	yield sum(n5_c3(*arguments))
	yield sum(n5_c4(*arguments))
	yield sum(n5_c5(*arguments))
	yield sum(n5_c6(*arguments))
	yield sum(n5_c7_optimized(*arguments))
	yield sum(n5_c8(*arguments))

def calc_conjugations(u):
	u_data_type = str(type(u))
	if u_data_type == "<class 'clifford._multivector.MultiVector'>":
		cliff = (~u).gradeInvol()
		grade = u.gradeInvol()
		rever = ~u
		trian = lambda v: v-2*(v(4)+v(5))

		if len(u.grades())-1 != 5:
			print(f'Warning! For element U, n={len(u.grades())-1}!=5')

	elif u_data_type == "<class 'galgebra.mv.Mv'>":
		cliff = (u - 2*u.odd()).rev()
		grade = u - 2*u.odd()
		rever = u.rev()
		trian = lambda v: v-2*(v.get_grade(4)+v.get_grade(5))

		if len(u.coords) != 5:
			print(f'Warning! For element U, n={u.layout.dims}!=5')
	else:
		print('Warning! Element U is not of implemneted data type')
	return u,cliff,grade,rever,trian

def n5_c1(u,c,g,r,d):
	yield u
	yield c
	yield g
	yield r
	yield d(g)
	yield d(r)
	yield d(u)
	yield d(c)

def n5_c2(u,c,g,r,d):
	yield -u*c
	yield -u*g
	yield -u*r
	yield -u*d(g)
	yield -u*d(r)
	yield -u*d(u)
	yield -u*d(c)
	yield -c*g
	yield -c*r
	yield -c*d(g)
	yield -c*d(r)
	yield -c*d(u)
	yield -c*d(c)
	yield -g*r
	yield -g*d(g)
	yield -g*d(r)
	yield -g*d(u)
	yield -g*d(c)
	yield -r*d(g)
	yield -r*d(r)
	yield -r*d(u)
	yield -r*d(c)
	yield -d(g*r)
	yield -d(g*u)
	yield -d(g*c)
	yield -d(r*u)
	yield -d(r*c)
	yield -d(u*c)

def n5_c3(u,c,g,r,d):
	yield u*c*g
	yield u*c*r
	yield u*c*d(g)
	yield u*c*d(r)
	yield u*c*d(u)
	yield u*c*d(c)
	yield u*g*r
	yield u*g*d(g)
	yield u*g*d(r)
	yield u*g*d(u)
	yield u*g*d(c)
	yield u*r*d(g)
	yield u*r*d(r)
	yield u*r*d(u)
	yield u*r*d(c)
	yield u*d(g*r)
	yield u*d(g*u)
	yield u*d(g*c)
	yield u*d(r*u)
	yield u*d(r*c)
	yield u*d(u*c)
	yield c*g*r
	yield c*g*d(g)
	yield c*g*d(r)
	yield c*g*d(u)
	yield c*g*d(c)
	yield c*r*d(g)
	yield c*r*d(r)
	yield c*r*d(u)
	yield c*r*d(c)
	yield c*d(g*r)
	yield c*d(g*u)
	yield c*d(g*c)
	yield c*d(r*u)
	yield c*d(r*c)
	yield c*d(u*c)
	yield g*r*d(g)
	yield g*r*d(r)
	yield g*r*d(u)
	yield g*r*d(c)
	yield g*d(g*r)
	yield g*d(g*u)
	yield g*d(g*c)
	yield g*d(r*u)
	yield g*d(r*c)
	yield g*d(u*c)
	yield r*d(g*r)
	yield r*d(g*u)
	yield r*d(g*c)
	yield r*d(r*u)
	yield r*d(r*c)
	yield r*d(u*c)
	yield d(g*r*u)
	yield d(g*r*c)
	yield d(g*u*c)
	yield d(r*u*c)

def n5_c4(u,c,g,r,d):
	yield -u*c*g*r
	yield -u*c*g*d(g)
	yield -u*c*g*d(r)
	yield -u*c*g*d(u)
	yield -u*c*g*d(c)
	yield -u*c*r*d(g)
	yield -u*c*r*d(r)
	yield -u*c*r*d(u)
	yield -u*c*r*d(c)
	yield -u*c*d(g*r)
	yield -u*c*d(g*u)
	yield -u*c*d(g*c)
	yield -u*c*d(r*u)
	yield -u*c*d(r*c)
	yield -u*c*d(u*c)
	yield -u*g*r*d(g)
	yield -u*g*r*d(r)
	yield -u*g*r*d(u)
	yield -u*g*r*d(c)
	yield -u*g*d(g*r)
	yield -u*g*d(g*u)
	yield -u*g*d(g*c)
	yield -u*g*d(r*u)
	yield -u*g*d(r*c)
	yield -u*g*d(u*c)
	yield -u*r*d(g*r)
	yield -u*r*d(g*u)
	yield -u*r*d(g*c)
	yield -u*r*d(r*u)
	yield -u*r*d(r*c)
	yield -u*r*d(u*c)
	yield -u*d(g*r*u)
	yield -u*d(g*r*c)
	yield -u*d(g*u*c)
	yield -u*d(r*u*c)
	yield -c*g*r*d(g)
	yield -c*g*r*d(r)
	yield -c*g*r*d(u)
	yield -c*g*r*d(c)
	yield -c*g*d(g*r)
	yield -c*g*d(g*u)
	yield -c*g*d(g*c)
	yield -c*g*d(r*u)
	yield -c*g*d(r*c)
	yield -c*g*d(u*c)
	yield -c*r*d(g*r)
	yield -c*r*d(g*u)
	yield -c*r*d(g*c)
	yield -c*r*d(r*u)
	yield -c*r*d(r*c)
	yield -c*r*d(u*c)
	yield -c*d(g*r*u)
	yield -c*d(g*r*c)
	yield -c*d(g*u*c)
	yield -c*d(r*u*c)
	yield -g*r*d(g*r)
	yield -g*r*d(g*u)
	yield -g*r*d(g*c)
	yield -g*r*d(r*u)
	yield -g*r*d(r*c)
	yield -g*r*d(u*c)
	yield -g*d(g*r*u)
	yield -g*d(g*r*c)
	yield -g*d(g*u*c)
	yield -g*d(r*u*c)
	yield -r*d(g*r*u)
	yield -r*d(g*r*c)
	yield -r*d(g*u*c)
	yield -r*d(r*u*c)
	yield -d(g*r*u*c)

def n5_c5(u,c,g,r,d):
	yield u*c*g*r*d(g)
	yield u*c*g*r*d(r)
	yield u*c*g*r*d(u)
	yield u*c*g*r*d(c)
	yield u*c*g*d(g*r)
	yield u*c*g*d(g*u)
	yield u*c*g*d(g*c)
	yield u*c*g*d(r*u)
	yield u*c*g*d(r*c)
	yield u*c*g*d(u*c)
	yield u*c*r*d(g*r)
	yield u*c*r*d(g*u)
	yield u*c*r*d(g*c)
	yield u*c*r*d(r*u)
	yield u*c*r*d(r*c)
	yield u*c*r*d(u*c)
	yield u*c*d(g*r*u)
	yield u*c*d(g*r*c)
	yield u*c*d(g*u*c)
	yield u*c*d(r*u*c)
	yield u*g*r*d(g*r)
	yield u*g*r*d(g*u)
	yield u*g*r*d(g*c)
	yield u*g*r*d(r*u)
	yield u*g*r*d(r*c)
	yield u*g*r*d(u*c)
	yield u*g*d(g*r*u)
	yield u*g*d(g*r*c)
	yield u*g*d(g*u*c)
	yield u*g*d(r*u*c)
	yield u*r*d(g*r*u)
	yield u*r*d(g*r*c)
	yield u*r*d(g*u*c)
	yield u*r*d(r*u*c)
	yield u*d(g*r*u*c)
	yield c*g*r*d(g*r)
	yield c*g*r*d(g*u)
	yield c*g*r*d(g*c)
	yield c*g*r*d(r*u)
	yield c*g*r*d(r*c)
	yield c*g*r*d(u*c)
	yield c*g*d(g*r*u)
	yield c*g*d(g*r*c)
	yield c*g*d(g*u*c)
	yield c*g*d(r*u*c)
	yield c*r*d(g*r*u)
	yield c*r*d(g*r*c)
	yield c*r*d(g*u*c)
	yield c*r*d(r*u*c)
	yield c*d(g*r*u*c)
	yield g*r*d(g*r*u)
	yield g*r*d(g*r*c)
	yield g*r*d(g*u*c)
	yield g*r*d(r*u*c)
	yield g*d(g*r*u*c)
	yield r*d(g*r*u*c)

def n5_c6(u,c,g,r,d):
	yield -u*c*g*r*d(g*r)
	yield -u*c*g*r*d(g*u)
	yield -u*c*g*r*d(g*c)
	yield -u*c*g*r*d(r*u)
	yield -u*c*g*r*d(r*c)
	yield -u*c*g*r*d(u*c)
	yield -u*c*g*d(g*r*u)
	yield -u*c*g*d(g*r*c)
	yield -u*c*g*d(g*u*c)
	yield -u*c*g*d(r*u*c)
	yield -u*c*r*d(g*r*u)
	yield -u*c*r*d(g*r*c)
	yield -u*c*r*d(g*u*c)
	yield -u*c*r*d(r*u*c)
	yield -u*c*d(g*r*u*c)
	yield -u*g*r*d(g*r*u)
	yield -u*g*r*d(g*r*c)
	yield -u*g*r*d(g*u*c)
	yield -u*g*r*d(r*u*c)
	yield -u*g*d(g*r*u*c)
	yield -u*r*d(g*r*u*c)
	yield -c*g*r*d(g*r*u)
	yield -c*g*r*d(g*r*c)
	yield -c*g*r*d(g*u*c)
	yield -c*g*r*d(r*u*c)
	yield -c*g*d(g*r*u*c)
	yield -c*r*d(g*r*u*c)
	yield -g*r*d(g*r*u*c)

def n5_c7(u,c,g,r,d):
	yield u*c*g*r*d(g*r*u)
	yield u*c*g*r*d(g*r*c)
	yield u*c*g*r*d(g*u*c)
	yield u*c*g*r*d(r*u*c)
	yield u*c*g*d(g*r*u*c)
	yield u*c*r*d(g*r*u*c)
	yield u*g*r*d(g*r*u*c)
	yield c*g*r*d(g*r*u*c)

def n5_c7_optimized(u,c,g,r,d):
    a1, a2 = u*c, g*r
    b1 = a1*a2
    yield b1*d(a2*u)
    yield b1*d(a2*c)
    yield b1*d(g*a1)
    yield b1*d(r*a1)
    b2 = d(a2*a1)
    yield a1*g*b2
    yield a1*r*b2
    yield u*a2*b2
    yield c*a2*b2

def n5_c8(u,c,g,r,d):
	yield -u*c*g*r*d(g*r*u*c)
