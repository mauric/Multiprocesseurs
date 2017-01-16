import numpy
from time import time
from scipy import weave
sizeX = 1000000
numberIterations =1000
X = numpy.random.rand(sizeX).astype(numpy.float32)
Y = numpy.empty(sizeX).astype(numpy.float32)

# C++ reference code
referenceCode="""
#line 11 "saxpy.py" // helpful for debug
void saxpy(int n, float alpha, float *X, float *Y)
{
	int i;
	for (i=0; i<n; i++)
		Y[i] += alpha * X[i];
}
"""
mainCode="""

for(int j=0; j< numberIterations;j++)
  saxpy(sizeX, 0.001f, X, Y);
  
"""

def BenchmarkCode(name, mainCode, saxpyCode,X,Y):
	# init
	Y[:]=0.5
	X[:]=1.0
	# start chronometer
	start_time = time()
	#use this to compile directly C++ code. 
	# fix for bug http://projects.scipy.org/scipy/ticket/1143 adding support code as comment in main code
	weave.inline(mainCode+"/* " + saxpyCode + " */"	, ['Y','X','sizeX', 'numberIterations'], 
				 compiler = 'gcc', support_code=saxpyCode,
				 verbose=2,
		         extra_compile_args=['-msse2 -fopenmp'],
		         extra_link_args=['-msse2 -fopenmp'],
		         headers=['<xmmintrin.h>'])
	# stop chronometer             
	stop_time = time()
	execution_time= stop_time - start_time
	print("execution time for "+name+" code = "+ str(execution_time))
	return execution_time


referenceTime=BenchmarkCode('Reference', mainCode, referenceCode,X,Y)
print(Y[0])
SSECode="""
#line 49 "saxpy.py" // helpful for debug
void saxpy(int n, float alpha, float *X, float *Y)
{
	int i;
	__m128  a  = _mm_set_ps(alpha,alpha,alpha,alpha);
	__m128  mul,add,ld;
	
	for (i=0; i<n-4; i=i+4){
			_mm_store_ps(Y+i,_mm_add_ps(_mm_load_ps(Y+i),_mm_mul_ps(a,_mm_load_ps(X+i))));

		}
	}
"""

SSETime=BenchmarkCode('SSE', mainCode, SSECode,X,Y)

print("speed up for SSE = " + str(referenceTime/SSETime))
print(Y[0])
