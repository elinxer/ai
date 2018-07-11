#!/usr/bin/python3

# 自定义异常


class CustomError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
