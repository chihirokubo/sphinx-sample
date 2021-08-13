# quick start guide

```
/code
├── .vscode
│    └── settings.json
└── my_project
      ├── docs
      │    └── empty
      ├── package
      │    ├── __init__.py
      │    ├── sample_module1.py
      │    └── sample_module2.py
      └── main.py
```

## prepare
```
$ cd /code/my_project
```

```
$ sphinx-apidoc -F -o ./docs .
```

## edit my_project/docs/conf.py
```
- # import sys
- # sys.path.insert(0, '/code/my_project')
+ import sys
+ sys.path.insert(0, '/code/my_project')
```

```
- extensions = [
-     "sphinx.ext.autodoc",
-     "sphinx.ext.viewcode",
-     "sphinx.ext.todo",
- ]
+ extensions = [
+     "sphinx.ext.autodoc",
+     "sphinx.ext.viewcode",
+     "sphinx.ext.todo",
+     "sphinx.ext.napoleon",
+ ]
```

```
- html_theme = "alabaster"
+ html_theme = "sphinx_rtd_theme"
```

## make html file
```
$ sphinx-build -a ./docs ./docs/_build
```

open .docs/_build/index.html in browser