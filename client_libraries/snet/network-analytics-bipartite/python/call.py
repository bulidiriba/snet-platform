import snet
#import snet.example_service as example_service

from snet_sdk import Snet

private_key = open('../../private_key.txt').readline()

identity = Snet(private_key=private_key)

try:
	#client = identity.client("snet", "face-detect", channel_id=6249, endpoi)
	client = identity.client("snet", "face-detect")
	print("Yeah No Error")
	#print("AGI tokens available:", identity.balance())
	client.open_channel()
	print("channel created")
except Exception as e:
	print("Error 1")
	print("\nEEEROOOR", e)

try:
	import network_analytics_bipartite_pb2 as nb
	import network_analytics_bipartite_pb2_grpc as nbg
	stub = nbg.NetworkAnalyticsBipartiteStub(client.grpc_channel)
	print("Stub initalized")
	request = nb.Numbers(a=10, b=12)
	print("Number passed")
	result = stub.add(request)
	print(result)
except Exception as e:
	print("Error 2")
	print("\nEEEROOOR", e)
