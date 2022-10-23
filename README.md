# Python-Code-Snippets

A coding play-place for snippets of my helper code

## SQLAlchemy

### DictToModel.py

Functions to assist in converting a flat Python Dictionary (Dict) to an SQLAlchemy model.py type class definition.  
Intended to be passed the body of a result returned by an API, and return class text.

Todo: expand to allow creation from nested dicts
After generating class, and using with database, analyse TEXT lengths and consider changing to String(x) where X is at least MAX Length (Where a max length is expected)
