# geometry_lib
---
Library in Python with the following functionality:
- An abstract ``Shape`` class with methods ``area()`` and ``is_right()``.
- The ``Circle`` class for calculating the area of a circle.
- The ``Triangle`` class checks the validity of the sides, calculates the area using the Heron formula, and determines whether the triangle is rectangular.
- The ``ShapeFactory.create()`` factory, which allows you to create shapes by string name.
- The universal ``compute_area()`` function, which calculates the area without knowing the shape type at the compilation stage.
- Unit tests for all key scenarios: correct and incorrect parameters, rectangular and non-rectangular triangle, factory, exceptions.
The library is easily expandable: to add a new shape, you need to inherit from ``Shape``, implement methods, and register in the factory.

# Additionally PySpark
---
1. ``prod_with_cat``
- Takes the ``df_link`` relationship table and, through an ``inner join`` with ``df_cat``, substitutes its ``category_name`` for each ``product_id``.
- There are no products without links in this table.

2. ``Left join``
- Take all the products from ``df_prod``.
- Substitute the found ``category_name`` (or ``null`` if the product has no links).
As a result, you will get:
All existing ``Product Name – Category Name`` pairs
For products without categories, a string like (``"Product name"``, ``null``)
