__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""

from . import constants


def callback_wrapper(func):
    def new_func(*args, **kwargs):
        s, d = kwargs.get("status", None), kwargs.get("states", None)
        if (not s and not d) or (s and not d) or (not s and d):
            raise TypeError("Can not execute callback, missing argument(s) :\n"
                            "status:{s}, states:{d}"
                            .format(s='ok' if s else 'missing', d='ok' if d else 'missing'))
        return func(*args, **kwargs)
    return new_func


@callback_wrapper
def test_callback(**kwargs):
    print("I am a callback !")
    print("The status of the action is :", constants.convert_status_to_str(kwargs.get("status")))
    print("And the states were :", kwargs.get("states"))