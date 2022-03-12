The Implementation of the formulas from the paper "**Basis-free Formulas for Characteristic Polynomial Coefficients in Geometric Algebras**
=========================================================
Here we present implementation in Python programming language of the formulas and algorithms in Geometric Algebra from the paper "**Basis-free Formulas for Characteristic Polynomial Coefficients in Geometric Algebras**". 

The Implementation
------------------
The implementation requires [`galgebra`](https://github.com/pygae/galgebra) for symbolic computations and [`clifford`](https://github.com/pygae/clifford) for numeric computations. 
**We implement the following:**
In `coefficients_recursive.py`
-- The *recursive* formulas for the characteristic polynomial coefficients from the paper [**"On computing the determinant, other characteristic polynomial coefficients, and inverse in Clifford algebras of arbitrary dimension"**](https://arxiv.org/abs/2005.04015) (*Theorem 4*).

In `coefficients_explicit_n5.py`
-- The *explicit* formulas for the characteristic polynomial coefficients in the case n=5 from the paper "**Basis-free Formulas for Characteristic Polynomial Coefficients in Geometric Algebras**" (*Theorem 5.1*).

In `coefficients_explicit_genralform.py`
-- Our method to obtain a general form of the basis-free formulas for all characteristic polynomial coefficients in the cases n≤ 6  from the paper **"Basis-free Formulas for Characteristic Polynomial Coefficients in Geometric Algebras"** (*Sections 7 and 8*)  


Examples
----------
We provide examples of application of the implementation in the Jupyter notebooks. The examples could be opened on a free Jupyter notebook environment [Google Colaboratory](https://research.google.com/colaboratory/) that runs in the cloud: 
[`Example___coefficients_recursive.ipynb`](https://colab.research.google.com/github/kamranuz/clifford_det/blob/main/examples/Example___coefficients_recursive.ipynb)
[`Example___coefficients_explicit_n5.ipynb`](https://colab.research.google.com/github/kamranuz/clifford_det/blob/main/examples/Example___coefficients_explicit_n5.ipynb)
[`Example___coefficients_explicit_genralform.ipynb`](https://colab.research.google.com/github/kamranuz/clifford_det/blob/main/examples/Example___coefficients_explicit_genralform.ipynb)
---
