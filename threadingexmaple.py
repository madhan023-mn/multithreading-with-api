import threading
import time

def process_invoice(invoice_no):
    print(f"Process invoice {invoice_no}")
    time.sleep(2)
    print(f"Process invoice {invoice_no} completed")

start=time.time()

t1=threading.Thread(target=process_invoice,args=(1,))
t2=threading.Thread(target=process_invoice,args=(2,))
t3=threading.Thread(target=process_invoice,args=(3,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end=time.time()
print(f"Total time {end-start}")

