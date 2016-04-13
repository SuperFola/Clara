__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""


SUCCESS = 1
RUNNING = 0
FAILURE = -1


def convert_status_to_str(status):
    if status == SUCCESS:
        return "achieved"
    elif status == RUNNING:
        return "still running"
    elif status == FAILURE:
        return "failed"
    return "status unknown"