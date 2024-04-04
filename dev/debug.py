"""
Debug functions
"""

import inspect

def line_info():
    """
    Get line of call
    """
    f = inspect.currentframe()
    i = inspect.getframeinfo(f.f_back)
    return (i.lineno)