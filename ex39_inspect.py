#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio, os, inspect, logging, functools

#如果url处理函数需要传入关键字参数，且默认是空得话，获取这个key
def get_required_kw_args(fn):
	args = []
	params = inspect.signature(fn).parameters
	for name, param in params.items():
		if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
			args.append(name)	
	return tuple(args)

#如果url处理函数需要传入关键字参数，获取这个key
def get_named_kw_args(fn):
	args = []
	params = inspect.signature(fn).parameters
	for name, param in params.items():
		if param.kind == inspect.Parameter.KEYWORD_ONLY:
			args.append(name)	
	return tuple(args)

#如果url处理函数需要传入关键字参数，返回True
def has_named_kw_args(fn):
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            return True

#如果url处理函数的参数是**kw，返回True
def has_var_kw_arg(fn):
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.VAR_KEYWORD:
            return True

##如果url处理函数的参数是request，返回True
def has_request_arg(fn):
    sig = inspect.signature(fn)
    params = sig.parameters
    found = False
    for name, param in params.items():
        if name == 'request':
            found = True
            continue
        if found and (param.kind != inspect.Parameter.VAR_POSITIONAL and param.kind != inspect.Parameter.KEYWORD_ONLY and param.kind != inspect.Parameter.VAR_KEYWORD):
            raise ValueError('request parameter must be the last named parameter in function: %s%s' % (fn.__name__, str(sig)))
    
    return found

class FnHandler(object):
	"""docstring for RequestHandler"""
	def __init__(self, app, fn):
		self._app = app
		self._func = fn
		#下面的一系列是为了检测url处理函数的参数类型
		self._has_request_arg = has_request_arg(fn)
		self._has_var_kw_arg = has_var_kw_arg(fn)
		self._has_named_kw_arg = has_named_kw_args(fn)
		self._named_kw_args = get_named_kw_args(fn)
		self._required_kw_args = get_required_kw_args(fn)

	def __call__(self):
		print ('self._app:', self._app)
		print ('self._func:', self._func)
		print ('_has_request_arg:', self._has_request_arg)
		print ('_has_var_kw_arg:', self._has_var_kw_arg)
		print ('_has_named_kw_arg:', self._has_named_kw_arg)
		print ('_named_kw_args:', self._named_kw_args)
		print ('_required_kw_args:', self._required_kw_args)
		params = inspect.signature(self._func).parameters
		print ('params:', params)
		print ('dir(params):\n', dir(params))
		for k, v in params.items():
			print ('Items:', k, '== ',v, ': kind == ', v.kind)
			print ('dir(v):\n', dir(v))

def hello(a, b, c, d = 'd-', *arg, **kw):
	pass
	print (a, b, c, d, **kw)

def hello2(a, b):
	return a*b



fh1 = FnHandler(app = None, fn = hello)
fh1()
fh2 = FnHandler(app = None, fn = hello2)
fh2()