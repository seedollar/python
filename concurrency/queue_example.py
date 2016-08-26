# Shows how you can use a queue using the multiprocessing library

import multiprocessing as mp

def washer(dishes, output):
    for dish in dishes:
        print("Washing", dish, "dish")
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print("Drying", dish, "dish")
        input.task_done()

dish_queue = mp.JoinableQueue()
dryer_process = mp.Process(target=dryer, args=(dish_queue,))
dryer_process.daemon = True
dryer_process.start()

dishes = ['salad', 'dessert', 'entree', 'bread']
washer(dishes, dish_queue)
print("dish_queue size: ", dish_queue.qsize())
dish_queue.join()

