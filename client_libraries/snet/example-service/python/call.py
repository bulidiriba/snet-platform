
from snet_sdk import Snet

private_key = open('../../private_key.txt').readline()

identity = Snet(private_key=private_key)

channel_id = [channel_id]# the already initialized channel id of this service, if not initialize it in snet-cli 

try:
	client = identity.client("snet", "example_service", channel_id)
	print("Yeah No Error")
	#client.open_channel()
	print("channel created")
except Exception as e:
	print("Error 1")
	print("\nEEEROOOR", e)


try:
	import example_service_pb2
	import example_service_pb2_grpc
	#stub = client.grpc.example_service_pb2_grpc.CalculatorStub(client.grpc_channel)
	stub = example_service_pb2_grpc.CalculatorStub(client.grpc_channel)
	print("Stub initalized")
	request = example_service_pb2.Numbers(a=10, b=12)
	print("Number passed")
	result = stub.mul(request).value
	print(result)
except Exception as e:
	print("Error 2")
	print("\nEEEROOOR", e)