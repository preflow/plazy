import time
import sys
from collections import OrderedDict
import functools
from .singleton import Singleton

class Timer(Singleton):
    def __init__(self):
        self.time_table = OrderedDict()
    
    def tic(self, key=None):
        if key not in self.time_table:
            self.time_table[key] = {
                'start_time': time.time(),
                'end_time': 0,
                'delta_time': 0,
                'tic_toc_num': 0
            }
        else:
            self.time_table[key]['start_time'] = time.time()
    
    def toc(self, key=None):
        if key not in self.time_table:
            raise Exception('Key (%s) not found in self.time_table' % key)
        
        end_time = time.time()        
        self.time_table[key]['end_time'] = end_time
        delta_time = end_time - self.time_table[key]['start_time']
        self.time_table[key]['delta_time'] += delta_time
        self.time_table[key]['tic_toc_num'] += 1
        return delta_time
    
    def toc_without_record(self, key=None):
        if key not in self.time_table:
            raise Exception('Key (%s) not found in self.time_table' % key)
        end_time = time.time()
        delta_time = end_time - self.time_table[key]['start_time']
        return delta_time
    
    def get(self, key=None):
        if key not in self.time_table:
            raise Exception('Key (%s) not found in self.time_table' % key)
        return self.time_table[key]
    
    def set(self, key, value):
        self.time_table.update({key: value})
    
    def get_delta_time(self, key=None):
        return self.get(key)['delta_time']

    def get_delta_time_with_default_value(self, key=None, default=0):
        if key not in self.time_table:
            return default
        return self.get_delta_time(key)
    
    def clear_timer(self, key=None):
        self.time_table.pop(key, None)
    
    def update(self, other_timer):
        self.time_table.update(other_timer.time_table)
    
    def merge(self, other_timer):
        for key in other_timer.time_table.keys():
            if key not in self.time_table.keys():
                self.time_table[key] = other_timer.time_table[key]
            else:
                self.time_table[key]['delta_time'] += other_timer.time_table[key]['delta_time']
                self.time_table[key]['tic_toc_num'] += other_timer.time_table[key]['tic_toc_num']

                other_timer.time_table[key]['delta_time'] = 0
                other_timer.time_table[key]['tic_toc_num'] = 0

    def print_time_table(self, fields=['delta_time', 'tic_toc_num'], headers=[]):
        print('\n'.join(headers))
        
        for k, v in self.time_table.items():
            values = []
            for f in fields:
                values.append('%s: %s' % (f, v[f]))
            print(k, '{ %s }' % (', '.join(values)))

    def print(self, fields=['delta_time', 'tic_toc_num'], headers=[]):
        self.print_time_table(fields, headers)
            
    def print_time_table_to_file(self, destination, fields=['delta_time', 'tic_toc_num'], headers=[]):
        sys.stdout = open(destination, 'a')
        self.print_time_table(fields=fields, headers=headers)
        print('\n')
        # switch stdout back to console
        sys.stdout = sys.__stdout__
        
g_timer = Timer()

def tictoc(key=None):
    def decorator_timer(func):
        @functools.wraps(func)
        def func_wrapper(*args, **kwargs):
            key_name = func.__qualname__ if not key else key
            g_timer.tic(key_name)
            value = func(*args, **kwargs)
            g_timer.toc(key_name)
            return value
        return func_wrapper
    return decorator_timer

def tic(key=None):
    return g_timer.tic(key)

def toc(key=None):
    return g_timer.toc(key)

def get_tictoc(is_dict=True):
    if is_dict:
        return dict(g_timer.time_table)
    return g_timer.time_table
