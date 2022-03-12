NI = 'NOT_IMPLEMENTED'
DETS = [NI,
        lambda x1,x2: f'self.{x1}*self.{x2}',
        lambda x1,x2: f'self.{x1}*self.{x2}',
        lambda x1,x2,x3,x4: f'self.{x1}*self.{x2}*self.{x3}*self.{x4}',
        lambda x1,x2,x3,x4: f'self.{x1}*self.{x2}*self.t(self.{x3}*self.{x4})',
        lambda x1,x2,x3,x4,x5,x6,x7,x8: f'self.{x1}*self.{x2}*self.{x3}*self.{x4}*self.t(self.{x5}*self.{x6}*self.{x7}*self.{x8})',
        lambda x1,x2,x3,x4,x5,x6,x7,x8: f'self.{x1}*self.{x2}*self.{x3}*self.{x4}*self.t(self.{x5}*self.{x6}*self.{x7}*self.{x8})',
        lambda x1,x2,x3,x4,x5,x6,x7,x8: f'self.{x1}*self.{x2}*self.t(self.t(self.{x3}*self.{x4})*self.t(self.t(self.{x5}*self.{x6})*self.t(self.{x7}*self.{x8})))',]

DELS = [NI,
        ('u','g'),
        ('u','c'),
        ('u','g','r','c'),
        ('u','c','g','r'),
        ('u','c','g','r','g','r','u','c'),
        ('u','r','g','c','g','c','u','r'),
        ('u','r','g','c','g','c','u','r')]

TRIA = [NI,
        lambda v: v,
        lambda v: v,
        lambda v: v,
        lambda v: v-2*v(4),
        lambda v: v-2*v(4)-2*v(5),
        lambda v: v-2*v(4)-2*v(5)-2*v(6),
        lambda v: v-2*v(4)-2*v(5)-2*v(6)]


TEXS = ['U',
        '\\widetilde{U}',
        '\\widehat{U}',
        '\\widehat{\\widetilde{U}}']

def TRIAtex(v):
    v = str(v)
    if v == '':
        return ''

    if v in TEXS:
        return v+'^{\\bigtriangleup}'

    if v[-17:] == '^{\\bigtriangleup}' and v[:-17] in TEXS:
        return v[:-17]

    if v[0] == '(' and v[-18:] == ')^{\\bigtriangleup}' and '{\\bigtriangleup}' not in v[1:-18]:
        return v[1:-18]

    return '('+v+')^{\\bigtriangleup}'

N = [1,2,2,4,
     4,
     8,
     8,
     8]

class CoefsGeneralFormNumeric():
    def __init__(self,u,n,DETS=DETS,DELS=DELS,TRIA=TRIA,):   
        from math import floor

        self.det = DETS[n]
        self.els = DELS[n]
        self.t   = TRIA[n]
        self.N   = N[n]

        self.n = n if n<7 else n-1
        self.u = u
        self.r = (~u)
        self.g = u.gradeInvol()
        self.c = (~u).gradeInvol()
        self.e = u(0)-u(0)+1

    def coefs_terms_els(self):
        return [set_X(k,self.els) for k in range(1,self.N+1)]

    def coefs_terms(self):
        return [[self.det(*els) for els in terms_els] for terms_els in self.coefs_terms_els()]

    def eval_terms(self):
        locals = {'self': self}
        return [[eval(term, locals) for term in terms] for terms in self.coefs_terms()]

    def eval_coefs(self):
        return [((-1)**i)*sum(terms) for i,terms in enumerate(self.eval_terms())]

class CoefsGeneralFormLatex():
    def __init__(self,n,DETS=DETS,DELS=DELS,TRIA=TRIA,):
        from math import floor

        self.det = DETS[n]
        self.els = DELS[n]
        self.N = N[n]


        self.t   = TRIAtex

        self.n = n if n<7 else n-1
        self.u = TEXS[0]
        self.r = TEXS[1]
        self.g = TEXS[2]
        self.c = TEXS[3]
        self.e = ''

    def coefs_terms_els(self):
        return [set_X(k,self.els) for k in range(1,self.N+1)]

    def coefs_terms(self):
        return [[self.det(*els).replace('*','+') for els in terms_els] for terms_els in self.coefs_terms_els()]

    def eval_terms(self):
        locals = {'self': self}
        return [[eval(term, locals) for term in terms] for terms in self.coefs_terms()]

    def eval_coefs(self):
        return [((-1)**i)*'-('+'+'.join(terms)+((-1)**i)*')' for i,terms in enumerate(self.eval_terms())]


def set_X(k, els):
    '''
    example input:  k=3, els=['u','c','g','r']
            output: [['1', 'c', 'g', 'r'], ['u', '1', 'g', 'r'], ['u', 'c', '1', 'r'], ['u', 'c', 'g', '1']]
    '''
    from itertools import combinations as combi
    n = len(els)
    # print(n,k)
    indexes_to_1 = (indexes for indexes in combi(range(n),n-k))

    coef_terms_els = []
    for indexes in indexes_to_1:
        term = list(els)[::]
        for i in indexes:
            term[i] = 'e'
        coef_terms_els.append(term)

    return coef_terms_els
