/* 



 * hello.c - Pthreads "hello, world" program 



 */



#include <pthread.h>

#include <iostream>



void *thread(void *vargp);



int main() 

{
	const long int numberThreads=3;

    pthread_t tid;

	std::cout << "Hello World from the main thread!" << std::endl;

    pthread_create(&tid, NULL, thread, NULL);

	pthread_join(tid, NULL);

    pthread_exit((void *)NULL);

}







void *thread(void *vargp) /* thread routine */

{

	std::cout << "Hello World from a thread created by the main thread!" << std::endl; 

    pthread_exit((void *)NULL);

	return NULL;

}
