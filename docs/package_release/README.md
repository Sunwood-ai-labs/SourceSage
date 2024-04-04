# Package release

## Build

```bash
python setup.py sdist bdist_wheel
```

## release

test
```bash
twine upload  --repository pypitest dist/*
```

main
```bash
twine upload  --repository pypi dist/*  
```
