
# Scientific Computing with Python

[Davide Gerosa](https://davidegerosa.com/)  - davide.gerosa@unimib.it  
University of Milano-Bicocca, 2023.

## Aims

The python programming language and its library ecosystem are an essential tool in modern science. This class provides an advanced introduction to phython and its main functionalities, focusing in particular on its applications to computational physics. Targeted topics include: array vectorization with numpy, pretty plotting with matplotlib, scientific recipes with scipy, symbolic manipulation with sympy, just-in-time compilating with numba, module packaging, and unit testing. I will also introduce other essential computational tools such as the git version-control protocol. The format will be highly interactive and tailored to the research interests of the participants. 

## Lectures


1. [**Introduction: python**](lectures/L01_python.ipynb). Why python. Basics. Datatypes. Control flow. Functions. Classes. Modules. Exceptions. File I/O. 
2. [**Arrays: numpy**](lectures/L02_numpy.ipynb). Array. Shaping. Slicing. Masking. Avoid loops. 
3. [**Plotting: matplotlib**](lectures/L03_matplotlib.ipynb). Pretty plotting. OO interface. Latex compatibility. Lines. Histograms. Contour maps. Annotations. Surfaces.
4. [**Numerical methods: scipy**](lectures/L04_scipy.ipynb). Integration. Interpolation. Root finding. Initial value problems. Boundary value problems. Fitting. Fourier transforms. Linear algebra.
5. [**Symbolic maths: sympy**](lectures/L05_sympy.ipynb). Symbols. Substitution. Simplification. Calculus. Solvers. Units.
6. [**Go faster: numba**](lectures/L06_numba.ipynb). Python extensions. Decorators. Just-in-time compilation.  
7. [**Version control: git**](lectures/L07_git.ipynb). Why. Git walkthrough. SSH keys. Github. 
8. [**Package and deploy: pip**](lectures/L08_pip.ipynb). Module setup. Installation. Usage. Deployment.
9. [**Unit testing: pytest**](lectures/L09_pytest.ipynb). Unit tests. Automated tests. Benchmark tests.


Each lecture has some exercises at the end.


## Schedule

TBC


## Resources

#### Texbooks

There are infinitely many textbooks on scientific computing. Here are three that I think are particularly useful:

- *["Learning Scientific Programming with Python"](https://www.cambridge.org/core/books/learning-scientific-programming-with-python/3D264483BC7B380A3059B3861C661237), C. Hill, Cambridge University Press, 2020. Supporting [code](https://scipython.com/).*

This textbook provides a gentle introduction to the beautiful world of python; it's a great starting point.

- *["Scientific Computing with Python: High-performance scientific computing with NumPy, SciPy, and pandas"](https://www.packtpub.com/product/scientific-computing-with-python-second-edition/9781838822323), C. Fuhrer, O. Verdier, J. E., Packt Publishing, 2021. Supporting [code](https://github.com/PacktPublishing/Scientific-Computing-with-Python-Second-Edition).*

This one is more advanced. It's ideal for sharpening your existing Python skills and go the extra mile. Instead of keep on coding the same way, as some point you'll need to do it better. It's one of my go-to references when looking for a specific package/topic/task.

- *["Effective Computation in Physics"](https://www.oreilly.com/library/view/effective-computation-in/9781491901564/), A. Scopatz, K. D. Huff, O'Reilly Media, 2015.*

Perhaps a bit outdated, but the really nice thing about this textbook is that has a bit of everything you might need for science, not just python. Things like command line operations, data visualization, regular expressions, version control, debugging, latex, etc). This book is a perfect companion when starting your PhD.

 
#### Classes

Here are some classes similar to this one which you might find useful:

- ["Scientific Computing with Python"](https://github.com/caam37830/book) University of Chicago, USA.
- ["Python for Scientific Computing"](https://sbu-python-class.github.io/python-science/Introduction.html), Stony Brook University, USA
- ["Python Programming for Scientists"](https://astrofrog.github.io/py4sci/), University of Heidelberg, Germany.
- ["Python for Scientific Computing"](https://aaltoscicomp.github.io/python-for-scicomp/), Aalto University, Finland.
- ["Lectures on scientific computing with Python"](https://github.com/jrjohansson/scientific-python-lectures), R. Johansson et al.  
- ["Python for Astronomers"](https://astro.uni-bonn.de/~rschaaf/Python2008/), University of Bonn, Germany. 


## Credits

This class is built on top of that taught by [Michael Zingale](https://github.com/zingale) at Stony Brook University: [https://sbu-python-class.github.io](https://sbu-python-class.github.io/python-science/Introduction.html)

## Careful... 

<p align="center">
  <img src="https://imgs.xkcd.com/comics/python.png" />
</p>

Credit: [xkcd 2582](https://xkcd.com/353/). This actually a Python easter egg... You can truly `pip install antigravity` and `import antigravity`. Try!
