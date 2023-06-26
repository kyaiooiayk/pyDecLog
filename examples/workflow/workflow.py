from PyDecLog import arguments as arg
from PyDecLog import signature as sign
from PyDecLog import message as mes
from PyDecLog import timing as tim
from PyDecLog import lprint
from PyDecLog import description as doc
from PyDecLog import memory as mem
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
