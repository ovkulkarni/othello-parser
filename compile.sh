#!/bin/bash

python setup.py egg_info
python setup.py sdist
python setup.py bdist_wheel
