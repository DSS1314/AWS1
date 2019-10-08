import logging
import tkinter
import boto3
from botocore.exceptions import ClientError
from tkinter import messagebox

def send_sqs_message(sqs_queue_url, msg_body):
    """
    :param sqs_queue_url: String URL of existing SQS queue
    :param msg_body: String message body
    :return: Dictionary containing information about the sent message. If
        error, returns None.
    """
    # Send the SQS message
    sqs_client = boto3.client('sqs',region_name="us-east-1")
    try:
        msg = sqs_client.send_message(QueueUrl=sqs_queue_url,
                                      MessageBody=msg_body)
    except ClientError as e:
        logging.error(e)
        return None
    return msg
def send1(message):
    """Exercise send_sqs_message()"""
    # Assign this value before running the program
    sqs_queue_url = "https://sqs.us-east-1.amazonaws.com/255880930717/MyQueue"
    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')
    # Send some SQS messages
   # for i in range(1, 2):
                    #定义sendwindow类的对象，调用rtnkey函数
    msg_body =message
    #input_send.get()        #将文本框内的消息作为要发送的信息
    msg = send_sqs_message(sqs_queue_url, msg_body)
    if msg is not None:
        logging.info(f'Sent SQS message ID: {msg["MessageId"]}')
    tkinter.mainloop()
