from pyDecLog import arguments as arg
from pyDecLog import signature as sign
from pyDecLog import message as mes
from pyDecLog import timing as tim
from pyDecLog import lprint
from pyDecLog import description as doc
from pyDecLog import memory as mem
import time


def workflow():

    # Set console level to the same level of the message so it is shown in the console
    lprint(console_log_level="info").info("Workflow starts!")

    # Decorate function as needed
    @doc
    @sign
    @arg
    @tim
    @mes
    def sum_(first, second=2):
        """Sum two numbers."""

        print("Some message on console")
        result = first + second
        time.sleep(2)
        print("Result is: " + str(result))
        return result

    sum_(1, 1)

    # Set console level to the same level of the message so it is shown in the console
    lprint(console_log_level="info").info("Workflow ends!")


if __name__ == "__main__":
    workflow()
