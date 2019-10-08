import tkinter
import logging
import boto3
from botocore.exceptions import ClientError
def retrieve_sqs_messages(sqs_queue_url, num_msgs=1, wait_time=0, visibility_time=5):
    """Retrieve messages from an SQS queue
    The retrieved messages are not deleted from the queue.
    :param sqs_queue_url: String URL of existing SQS queue
    :param num_msgs: Number of messages to retrieve (1-10)
    :param wait_time: Number of seconds to wait if no messages in queue
    :param visibility_time: Number of seconds to make retrieved messages
        hidden from subsequent retrieval requests
    :return: List of retrieved messages. If no messages are available, returned
        list is empty. If error, returns None.
    """
    # Validate number of messages to retrieve
    if num_msgs < 1:
        num_msgs = 1
    elif num_msgs > 10:
        num_msgs = 10
    # Retrieve messages from an SQS queue
    sqs_client = boto3.client('sqs',region_name="us-east-1")
    try:
        msgs = sqs_client.receive_message(QueueUrl=sqs_queue_url,
                                          MaxNumberOfMessages=num_msgs,
                                          WaitTimeSeconds=wait_time,
                                          VisibilityTimeout=visibility_time)
    except ClientError as e:
        logging.error(e)
        return None

    # Return the list of retrieved messages
    return msgs['Messages']
def delete_sqs_message(sqs_queue_url, msg_receipt_handle):
    """Delete a message from an SQS queue
    :param sqs_queue_url: String URL of existing SQS queue
    :param msg_receipt_handle: Receipt handle value of retrieved message
    """
    # Delete the message from the SQS queue
    sqs_client = boto3.client('sqs',region_name="us-east-1")
    sqs_client.delete_message(QueueUrl=sqs_queue_url,
                              ReceiptHandle=msg_receipt_handle)
def receive1():
    """Exercise retrieve_sqs_messages()"""
                       #接收信息的窗口
    # Assign this value before running the program
    sqs_queue_url = "https://sqs.us-east-1.amazonaws.com/255880930717/MyQueue"
    num_messages = 2
    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')
    # Retrieve SQS messages
    msgs = retrieve_sqs_messages(sqs_queue_url, num_messages)
    if msgs is not None:
        for msg in msgs:
         #   print (msgs)收到的消息为一个结构体。只用其中的部分信息
            logging.info(f'SQS: Message ID: {msg["MessageId"]}, '
                         f'Contents: {msg["Body"]}')
            # Remove the message from the queue
            print (msg["MessageId"])
            delete_sqs_message(sqs_queue_url, msg['ReceiptHandle'])

    return msg["Body"]
