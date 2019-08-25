# tinylogger
An easy use and more powerful android style logging util

## Installation
To install tinylogger run this command:
```
pip install tinylogger
```
or [download](https://github.com/frankzhangv5/tinylogger-dist/releases) Package then run this command:
```
pip install tinylogger-1.0.0-py3-none-any.whl
```

## Usage
### Basic Usage
The typical usage of this library is like the following:
```
from tinylogger.log import Log

if __name__ == "__main__":
    Log.d("test")
```
> output to stdout and log file in current work dir
```
2019-08-25 07:49:48.780000 - INFO  - log.py    (_get_instance:69): log path: D:\
develop\test\log_20190825_074948.txt
2019-08-25 07:49:48.782000 - DEBUG - test.py   (__main__  :8): test
```

### Full Usage
Or like this:
```
import os
import logging
from tinylogger.log import Log


if __name__ == "__main__":
    Log.setup(os.path.join(os.getcwd(), "log"), logging.DEBUG)
    Log.d("test")
```
> output to stdout and log file in current work dir
```
2019-08-25 07:52:32.514000 - INFO  - log.py    (setup     :78): log path: D:\dev
elop\test\log\log_20190825_075232.txt
2019-08-25 07:52:32.515000 - DEBUG - test.py   (__main__  :8): test
```

### Quiet print
If you don't want to print log in stdout, then setup as below:
```
Log.setup(os.path.join(os.getcwd(), "log", True), 
```

### Custom Configs
```
setup(cls, log_dir=os.path.join(os.getcwd()), log_level=logging.DEBUG, quiet=False)
```
```
log_dir: the dir to write log file
log_level: control log msg to log file expect stdout
quiet: do not print log in stdout
```

## Distribute
```
cd path/to/tinylogger-dist/
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python setup.py bdist_wheel
twine upload dist/*
```
