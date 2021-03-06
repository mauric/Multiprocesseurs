# code inspired from example provided by Roger Pau Monn'e

import pyopencl as cl
import numpy
import numpy.linalg as la
import datetime
from time import time


# number of data
num_data=4*25000*128
fragment_size= 200
sequence = numpy.random.randint(0,20,num_data).astype(numpy.uint8)
fragment = numpy.random.randint(0,20,fragment_size).astype(numpy.uint8)

# just for test, inject fragment somewhere in sequence
sequence[100:100+fragment_size]=fragment
score = numpy.empty(num_data).astype(numpy.uint16)


ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx,
              properties=cl.command_queue_properties.PROFILING_ENABLE)

mf = cl.mem_flags

sequence_buf = cl.Buffer(ctx, mf.READ_ONLY, sequence.nbytes)
fragment_buf = cl.Buffer(ctx, mf.READ_ONLY, fragment.nbytes)
score_buf = cl.Buffer(ctx, mf.WRITE_ONLY, score.nbytes)
time1 = time()
cl.enqueue_write_buffer(queue, sequence_buf, sequence)
cl.enqueue_write_buffer(queue, fragment_buf, fragment)
prg = cl.Program(ctx, """
      __kernel void scanSequence(__global const uchar *sequence,
      __global const uchar *fragment, __global ushort *score, const uint size_data, const uint fragment_size)
      {
              int gid = get_global_id(0);
              ushort s=0;
              // TODO: implement a scan of fragment in current sequence element
              if(gid+fragment_size < size_data){
	              for(int i=0; i< fragment_size; i++){
	              	if(sequence[gid+i] == fragment[i])s = s+1;
	              }
	              score[gid]=s;
              }
              }
              """).build()

exec_evt = prg.scanSequence(queue, (num_data,), None,
                                                      sequence_buf,
                                                      fragment_buf,
                                                      score_buf,
                                                      numpy.uint32(num_data),
                                                      numpy.uint32(fragment_size))
exec_evt.wait()
elapsed = 1e-9*(exec_evt.profile.end - exec_evt.profile.start)
cl.enqueue_read_buffer(queue, score_buf, score).wait()
time2 = time()
execTime2 = time2 - time1
print("Execution time of test: %g s" % elapsed)
print("Execution time of test + memory transfert time: %g s" % execTime2)

print (score[90:110])
