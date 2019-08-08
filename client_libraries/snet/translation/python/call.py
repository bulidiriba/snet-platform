from snet_sdk import Snet

private_key = open('../../private_key.txt').readline()

identity = Snet(private_key=private_key)
channel_id = [channel_id]# the already initialized channel id of this service, if not initialize it in snet-cli 

import translate_pb2 as tp
import translate_pb2_grpc as tpg

translation = snet.client("snet", "translation", channel_id=channel_id)
translation.open_channel()
stub = tpg.TranslationStub(translation.grpc_channel)
request = tp.Request(text="Hello World.", source_language="en", target_language="de")
resp = stub.translate(request).translation
print(resp)