#!/usr/bin/python3

from typing import Any, Callable, Tuple

def safe_function(fct: Callable, *args: Tuple[Any]) -> Any:
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
##
