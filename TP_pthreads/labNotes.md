# Microprocesseurs


## Exercice de démarrage

### Compiler et lancer l'exécutable avec la commande :
	g++ main.cpp -lpthread -O3 -o tp_pthread

### Que pouvons nous constater sur la sortie de la console?
mcaceres@lochan1:~/Multiprocesseurs/TP_pthreads$ ./tp_pthread 
Hello World from the main thread!
Hello World from a thread created by the main thread!

L execution d'un thread principal et la creation d'une autre thread 
a partir du precent



## Multiples Threads

## Modifiez le fichier main.cpp pour lancer un nombre quelconque de pthreads. Ce nombre devra être défini par une constante (ici bas le nombre de threads est 3): 
	const long int numberThreads=3;


Chaque thread secondaire devra afficher dans le message son numéro de création id:
std::cout << "Hello World from thread "<< id<<" created by the main thread!"<< std::endl;
Utilisez le paramètre passé au thread à sa création pour transmettre le numéro id.
Lancez plusieurs exécutions avec un nombre de threads différents.
Que constatez vous sur la sortie de la console?

On voit un decalage dans l' impression, parce que l'acces  a la console
est sequenciel 


## Protection de la sortie par des Mutex

Pour protéger les sorties consoles utilisez un Mutex que vous verrouillerez avant
les appels à std::cout et que vous déverrouillerez après ces appels.
• Vérifiez que les phrases ne sont plus coupées quelque soit le nombre de threads
     lancés.



























