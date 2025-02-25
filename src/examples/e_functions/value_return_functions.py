VALUE = 100 #global variable

def test_config():
    return True

def echo_variable(num):
    return num

def read_global_variable():
    print(VALUE)

def write_global_variable():
    global VALUE
    VALUE = 50 #local variable
    print(VALUE)