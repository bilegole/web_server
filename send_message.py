from multiprocessing import process,queues
def send_message(qup):
    plain_string = []
    while not qup.empty():
        plain_string.append(qup.get())
        pass