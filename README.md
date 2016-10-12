derivative
==========

Library for calculating exact numeric derivatives using dual numbers.
Inspiration from http://jliszka.github.io/2013/10/24/exact-numeric-nth-derivatives.html


    f = lambda x: x * 5 + x ** 2 - 2 / x + 3 / x ** 2
    print(derive(f, 6))
