import threading
import random
import time
import tkinter

class Filosofos(threading.Thread):
    running = True

    #Contruye filosofo
    def __init__(self, filosofo, izquierda, derecha):
        threading.Thread.__init__(self)
        self.name = filosofo
        self.izquierda = izquierda
        self.derecha = derecha

    #Waiting
    def run(self):
        while (self.running):
            #  filosofo sleep
            time.sleep(random.uniform(2, 12))
            print('%s Waiting' % self.name)
            self.eating()

    #Eating
    def eating(self):
        #t1, t2 tenedores
        t1, t2 = self.izquierda, self.derecha

        while self.running:
            t1.acquire(True)
            locked = t2.acquire(False)
            if locked: break
            t1.release()
            print('%s Get fork' % self.name)
            t1, t2 = t1, t2
        else:
            return

        self.eatstate()
        t2.release()
        t1.release()

    #Eating/Thinking
    def eatstate(self):
        print('%s Eating' % self.name)
        time.sleep(random.uniform(1, 10))
        print('%s Thinking' % self.name)


def LosFilosofos():

    #Inicia GUI, todo: hacer la GUI, si quitas esta parte, corre en consola. Al funcionar el programa entero vere si se puede optimizar
    root = tkinter.Tk()
    for r in range(6):
        for c in range(7):
            tkinter.Label(root, text='R%s/C%s' % (r, c), borderwidth=1).grid(row=r, column=c)
    root.mainloop()
    #Termina GUI



    tenedores = [threading.Lock() for n in range(5)]
    fofos = ('F1', 'F2', 'F3', 'F4', 'F5')

    #Se construyen los filosofos
    filosofos = [Filosofos(fofos[i], tenedores[i % 5], tenedores[(i + 1) % 5]) for i in range(5)]

    random.seed(765843)  #Py requiere seed para sacar random numbers

    Filosofos.running = True

    #Se corren los filosofos lol
    for p in filosofos: p.start()

    time.sleep(150) #sin esto se inician muy rapido y hay errores


    Filosofos.running = False
    print("Now we're finishing.")


LosFilosofos()
