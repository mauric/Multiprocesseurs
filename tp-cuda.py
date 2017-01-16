 
import pycuda.autoinit
import pycuda.driver as drv
import numpy

from pycuda.compiler import SourceModule


# Kernel definition and on-line compilation
mod = SourceModule("""
__global__ void mykernel(float *destination, float *source, float b)
{
  const int index = threadIdx.x;
  destination[index] = source[index]* b;
}
""")

mykernel = mod.get_function("mykernel")

# size of data
num_data= 400
# Any arbitrary value for this exercise
my_constant = 123.0

# number of blocks of thread
num_blocks = 1

# number of threads in a block
block_size = num_data

# produce a data set for this exercise
source = numpy.random.randn(num_data).astype(numpy.float32)

destination = numpy.empty_like(source)

# kernel call with implicit data transfer to the GPU and return result
mykernel(
        drv.Out(destination), drv.In(source),numpy.float32(my_constant),
        block=(block_size,1,1), grid=(num_blocks,1))

# CPU compute same result and display the difference with GPU computing result
print (destination-source * my_constant)












