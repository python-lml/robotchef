pip freeze
nosetests --with-cov --cover-package robotchef_cli --cover-package tests --with-doctest --doctest-extension=.rst README.rst tests docs/source robotchef_cli && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
