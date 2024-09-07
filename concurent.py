import threading
import script1
import script2

thread1 = threading.Thread(target=script1.change_teacher_id, args=(115, '200', 'Macroeconomics'))
thread2 = threading.Thread(target=script2.change_teacher_id, args=(115, '116', 'Macroeconomics'))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
