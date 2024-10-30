from task_2 import GCD, GCD_rec
import time


rec = time.time()
print(GCD_rec(5000,10000))
rec_time = time.time() - rec
print(f"Speed of recursion : {rec_time:.10f} sec")

itera = time.time()
print(GCD(5000, 10000))
iter_time = time.time() - itera
print(f"Speed of iteration : {iter_time:.10f} sec")