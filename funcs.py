
import os
from uuid import uuid4
from sms_ir import SmsIr


class FileUpload:


    def __init__(self,dir,prefix):
        self.dir = dir
        self.prefix = prefix



    def upload_to(self,instance,filename):
        filename,ext=os.path.splitext(filename)
        return f'{self.dir}/{self.prefix}/{uuid4()}{filename}{ext}'


#==========================
def price_by_final_price(price,discount=0):
    pass





def send_success(number,name):
    pass

    sms_ir = SmsIr('he4QV5RJiXYsfgjHBpgjpJ2GMFtemy28GSEcDlCpEweK9q0ahroGcmgT5kexuJUR')

    result = sms_ir.send_verify_code(
    number= str(number),
    template_id=977780,
    parameters=[
        {

            "name" : "TEXT",
            "value": str(name)
        },

    ],
)








import socket

def has_internet_connection():
    """
    Check if the device has an active internet connection.

    Returns:
        bool: True if the device has an active internet connection, False otherwise.
    """
    try:
        # Try to connect to a well-known website
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass

    try:
        # Try to connect to a different well-known website
        socket.create_connection(("www.example.com", 80))
        return True
    except OSError:
        pass

    return False
# ===================================
