/* 

 * hello.c - Pthreads "hello, world" program 

 */

#include <pthread.h>
#include <iostream>

void *thread(void *vargp);

int main() 
{
    const long int numberThreads=30;
    pthread_t tid;
	std::cout << "Hello World from the main thread!" << std::endl;
	for (long int i=0; i< numberThreads;i++)
        pthread_create(&tid, NULL, thread, (void*)i);
	pthread_join(tid, NULL);
    pthread_exit((void *)NULL);
}



void *thread(void *vargp) /* thread routine */
{
    long int id= (long int) vargp;
	std::cout << "Hello World from a thread "<< id <<" created by the main thread!" << std::endl; 
    pthread_exit((void *)NULL);
	return NULL;
}
