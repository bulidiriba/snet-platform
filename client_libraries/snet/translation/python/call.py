from snet_sdk import Snet

private_key = open('../../private_key.txt').readline()

identity = Snet(private_key=private_key)

#import network_analytics_node_importance_pb2_grpc as napg
#import network_analytics_node_importance_pb2 as npb
import translate_pb2 as tp
import translate_pb2_grpc as tpg

translation = snet.client("snet", "translation", channel_id="6191")
translation.open_channel()
stub = tpg.TranslationStub(translation.grpc_channel)
request = tp.Request(text="Hello World.", source_language="en", target_language="de")
resp = stub.translate(request).translation
print(resp)
















# import snet

# #import snet.network-analytics-nodeimportance as networkanlytics

# # Define identity, ethereum endpoint, IPFS endpoint, session cache strategy
# identity = snet.PrivateKeyIdentity("path/to/private/key") 
# eth = snet.KovanEth()
# ipfs = snet.SnetIpfs()
# cache = snet.FileSystemSessionCache("path/to/cache/folder")
# session = snet.Session(identity=identity, eth=eth, ipfs=ipfs, cache=cache)

# # Check AGI tokens balance and MultiPartyEscrow contract balance of session
# # identity, and deposit tokens to the MultiPartyEscrow.
# print("AGI tokens available:", session.balance())
# session.deposit(1000)
# print("AGI tokens available:", session.balance())

# # Instantiate "Example Service" client and call the method.
# # example_service.Calculator is generated as prerequisite step, for example
# # user calls `snet sdk` command providing org_id and service_id to generate
# # snet.example_service package with all necessary stubs. All logic related to
# # opening channel, finding proper endpoint, switching between endpoints is
# # embedded into service stub.
# example_service = example_service.Calculator(session)
# numbers = example_service.Numbers(a=7, b=6)
# result = example_service.mul(numbers)
# print("Calculation result:", result.value)
# print("AGI tokens available:", session.balance())