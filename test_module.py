''' this is a dummy module used to test module_explorer.py '''

def my_fully_annoed_func(my_string: str, my_bool: bool, my_int: int) -> int:
    ''' anotated test func '''
    my_string = "hello world"
    my_bool = True
    my_int = 0
    return my_int

def my_no_anno_func(my_var0, my_var1):
    ''' no anno test func.
    it has a really long form docstring
    just to show that docs are being printed
    as they should
            even lines like this
    '''
    my_var0 = my_var1
    my_var1 = my_var0
    return my_var0

def my_mixed_annoed_func(my_var0, my_var1: int) -> int:
    ''' parially annotated '''
    my_var0 = "is great!"
    my_var1 = len(my_var0)
    return 0

def my_no_arg_func():
    ''' nothing to see here '''
    return "hello world"

def just_ret_annoed_func() -> str:
    '''only return annotation'''
    return "hello world"