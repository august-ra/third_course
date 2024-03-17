Bank operations formatter.
============================

### Info

It's a student's app which print a few record about bank's operations and transactions from its resource data.

1. __There is a module `main.py` which starts the job.__
2. __There is a module `utils.py` where several functions:__
   - reading a file data in JSON format.
   - getting some newest operations from previous step.
   - formatting dates and bank accounts info.
   - formatting records of operations.
3. __There is a module `test.py` with 100% coverage tests for whole module `utils.py`.__

### Running

For running app: use `python3 main.py`.\
For running tests: use `pytest` inside tests folder.
