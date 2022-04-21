import inspect

class OnInitCallback:
    def __init__( 
        self,
     ):
     pass

    def __call__( self, func ):
        self.func = func
        self.check_args(func)
        
        def wrapper_f( *args, **kwargs ):
            func( *args, **kwargs )
        return wrapper_f

    def check_args(self, func):
        argspec = inspect.getfullargspec(func)
        if len(argspec.args) != 0:
            raise Exception("OnInit must be a function without arguments")

    def run(self):
        self.func()

class OnDeinitCallback:
    def __init__( 
        self,
     ):
     pass

    def __call__( self, func ):
        self.func = func
        self.argspec = inspect.getfullargspec(func)
        
        def wrapper_f( *args, **kwargs ):
            func( *args, **kwargs )
        return wrapper_f

    def check_args(self, func):
        argspec = inspect.getfullargspec(func)
        if len(argspec.args) != 0:
            raise Exception("OnInit must be a function without arguments")

    def run(self):
        self.func()

class OnTickCallback:
    def __init__( 
        self,
     ):
     pass

    def __call__( self, func ):
        self.func = func
        self.check_args(func)
        
        def wrapper_f( *args, **kwargs ):
            func( *args, **kwargs )
        return wrapper_f

    def check_args(self, func):
        argspec = inspect.getfullargspec(func)
        if len(argspec.args) != 1:
            raise Exception("OnTick must have exactly one argument")

    def run(self, tick_data):
        self.func(tick_data)
