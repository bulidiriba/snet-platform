
from snet_sdk import Snet

private_key = open('../../private_key.txt').readline()

identity = Snet(private_key=private_key)


try:
	#client = identity.client("snet", "face-detect", channel_id=6249, endpoi)
	client = identity.client("snet", "example_service")
	print("Yeah No Error")
	#print("AGI tokens available:", identity.balance())
	client.open_channel()
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