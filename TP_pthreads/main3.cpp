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
#include <string>

float X,V;
float dT = 1;

pthread_mutex_t mut = PTHREAD_MUTEX_INITIALIZER;

void *thread1(void *vargp);
void *thread2(void *vargp);

typedef struct thread_info{
	pthread_t tid;
	int data;
	int id;
	//void * handle;
	}thread_info;


//int main(int argc, char **argv){
int main(){	
	const long int numberThreads = 2;//atoi(argv[1]);
	thread_info * tinfo; //TODO on peut implementaire malloc
    pthread_t tid;
    V = 2;

 	/* Allocate memory for pthread_create() arguments */
  tinfo = (thread_info *) calloc(numberThreads, sizeof(thread_info));
  if (tinfo == NULL)
      perror("calloc troubles !!");

	std::cout << "Hello World from the main thread!" << std::endl;
	for (int i = 0; i < numberThreads; i++){
	//TODO faire une rutine de verification d'erreur
		 tinfo[i].data = i*2;
		 tinfo[i].id = i;
		 pthread_create(&tinfo[i].tid,NULL,thread1,&tinfo[i]); 
		 pthread_create(&tinfo[++i].tid,NULL,thread2,&tinfo[++i]);
	}
	//TODO faire une rutine de verification d'erreur
	pthread_join(tid, NULL);

	//TODO faire une rutine de verification d'erreur
    pthread_exit((void *)NULL);

}



void *thread1(void * vargp) /* thread routine */
{
   thread_info *tinfo = (thread_info *) vargp;
	pthread_mutex_lock(&mut);
  	std::cout << "Hello World from thread "<< tinfo[0].id <<" created by the main thread!"<< std::endl;
  	X = V * dT + X;
  	pthread_mutex_unlock(&mut);

    pthread_exit((void *)NULL);

	return NULL;

}

void *thread2(void * vargp) /* thread routine */
{
   thread_info *tinfo = (thread_info *) vargp;
	pthread_mutex_lock(&mut);
  	std::cout << "Hello World from thread "<< tinfo[0].id <<" created by the main thread!"<< std::endl;
  	X = V * dT + X;
  	pthread_mutex_unlock(&mut);

    pthread_exit((void *)NULL);

	return NULL;

}
