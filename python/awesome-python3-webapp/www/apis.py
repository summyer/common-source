# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:33:55 2018

@author: Administrator
"""

import json, logging, inspect,functools

class APIError(Exception):
    
    def __init__(self,error,data='',message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message
    
class APIValueError(APIError):
    
    def __init__(self,field,message=''):
        super(APIValueError, self).__init('value:invalid',field,message)
        
class APIPermissionError(APIError):
    
    def __init__(self,message=''):
        super(APIPermissionError, self).__init__('permission:forbidden','permission',message)