# Package related commands

Ref: https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives

```bash
# package
python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel

# distribute
python3 -m pip install --user --upgrade twine
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# install
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-your-username
```