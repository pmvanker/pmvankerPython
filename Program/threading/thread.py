import threading
# threading module contain method current_thread that return object and on that
# we call getName method
print('Thread:',threading.current_thread().getName())
