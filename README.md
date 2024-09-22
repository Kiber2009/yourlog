# yourlog
## About
yourlog is a simple python logging library
## Usage example

```python
import yourlog

logger = yourlog.Logger()

logger.add_listener("lastest.log")
logger.add_listener(print)

logger.debug("Debug there")
logger.info("Info there")
logger.warn("Warn there")
logger.error("Error there")
logger.fatal("Fatal there")

logger.custom("Custom type", "Custom there")
```
## Installing
```shell
pip install yourlog
```
## Building from source code
* Clone the repo
  ```shell
  git clone https://github.com/Kiber2009/yourlog.git
  cd yourlog
  ```
* Make sure you have the latest version of PyPA’s build installed
  ```shell
  python -m pip install --upgrade build
  ```
* Build the lib
  ```shell
  python -m build
  ```