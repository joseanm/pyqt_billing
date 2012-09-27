#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
from decimal import Decimal

def ifValid( func ):
    u"""
    Decorador que retorna Decimal(0) si la linea no es valida, esto es más facil
     que usar "if valid else Decimal(0)" en todos lados
    """
    @functools.wraps( func )
    def wrapper( self ):
        return func( self ) if self.valid else Decimal( 0 )
    return wrapper

def return_decimal( func ):
    u"""
    Decorador que retorna Decimal siempre
    """
    @functools.wraps( func )
    def wrapper( self ):
        value = func( self )
        return   value if type( value ) == Decimal else Decimal( value )
    return wrapper

def if_edit_model( func ):
    u""""
    Este decorador ejecuta la función si editmodel is not None
    de otro modo pass
    """
    @functools.wraps( func )
    def wrapper( self, *args ):
        if self.editmodel is not None:
            return func( self, *args )

    return wrapper


