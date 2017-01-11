/* 



 * hello.c - Pthreads "hello, world" program 



 */



#include <pthread.h>

#include <iostream>
#include <pthread.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <ctype.h>


typedef struct thread_info{
	pthread_t tid;
	int data;
	int id;
	}thread_info;


void *thread(void *vargp);



int main() 

{
	const long int numberThreads=3;
	thread_info * tinfo; //TODO on peut implementaire malloc
    pthread_t tid;
    
 	/* Allocate memory for pthread_create() arguments */
  tinfo = (thread_info *) calloc(numberThreads, sizeof(thread_info));
  if (tinfo == NULL)
      perror("calloc troubles !!");

	std::cout << "Hello World from the main thread!" << std::endl;
	for (int i = 0; i < numberThreads; i++){
	//TODO faire une rutine de verification d'erreur
		 tinfo[i].data = i*2;
		 tinfo[i].id = i;
		 pthread_create(&tinfo[i].tid,NULL,thread,&tinfo[i]); //&tinfo  pour passer tout les structs
	}
	//TODO faire une rutine de verification d'erreur
	pthread_join(tid, NULL);

	//TODO faire une rutine de verification d'erreur
    pthread_exit((void *)NULL);

}



void *thread(void * vargp) /* thread routine */
{
   thread_info *tinfo = (thread_info *) vargp;

	std::cout << "Hello World from thread "<< tinfo[0].id <<" created by the main thread!"<< std::endl;


    pthread_exit((void *)NULL);

	return NULL;

}
