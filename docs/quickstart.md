# 🚀Quick start
- Say we have the following workflow
```python
from pyDecLog import arguments
from pyDecLog import signature
from pyDecLog import message
from pyDecLog import timing
from pyDecLog import lprint
from pyDecLog import description
import time

def workflow():

    # Set console level to the same level of the message level so it is shown in the console
    lprint(console_log_level="info").info("Workflow starts!")

    # Decorate function as needed
    @doscription
    @signature
    @arguments
    @timing
    @message
    def sum_two_int(first, second=2):
        """Sum two numbers."""

        print("Some message on console")
        result = first + second
        time.sleep(2)
        print("Result is: " + str(result))
        return result

    sum_tow_int(1, 1)

    # Set console level to the same level of the message so it is shown in the console
    lprint(console_log_level="info").info("Workflow ends!")


if __name__ == "__main__":
    workflow()
```
- Upon execution the following is printed on console:
```shell
Workflow starts!
Workflow ends!
```
- Upon execution a `LOG.log` file is written:
```shell
2023/06/24 | 18:20:50 | ERROR Workflow starts!
2023/06/24 | 18:20:50 | DEBUG Method's description: Sum two numbers.
2023/06/24 | 18:20:50 | DEBUG Method's name: sum_
2023/06/24 | 18:20:50 | DEBUG Method's signature:(first, second=2)
2023/06/24 | 18:20:50 | DEBUG Method's name: sum_
2023/06/24 | 18:20:50 | DEBUG Method's args: (1, 1)
2023/06/24 | 18:20:50 | DEBUG Method's kwargs: {}
2023/06/24 | 18:20:52 | INFO Some message on console
2023/06/24 | 18:20:52 | INFO Result is: 2
2023/06/24 | 18:20:52 | DEBUG sum_ was executed in: 2.006 sec
2023/06/24 | 18:20:52 | ERROR Workflow ends!
```
