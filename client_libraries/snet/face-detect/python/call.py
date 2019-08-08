import snet
#import snet.example_service as example_service

from snet_sdk import Snet

private_key = open('../../private_key.txt').readline()

identity = Snet(private_key=private_key)
