Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
>>> t=time.process_time()
>>> n=100000000
>>> value=10
>>> for i in range(n):
	value2=value*value
elapsed_time=time.process_time()-t
SyntaxError: invalid syntax
>>> elapsed_time=time.process_time()-t
>>> print("N=",n,"value bits=",value.bit_length(),"time=",elapsed_time)
N= 100000000 value bits= 4 time= 0.4994160000000003
>>> 
