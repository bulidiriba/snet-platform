#import snet
#import snet.example_service as example_service
from snet_sdk import Snet
#import "~./snet/config"
#snet = Snet(private_key=config.private_key)
#snet = Snet(private_key=str('4e51e1cc30aae65758d4eb9edc46dad7b34a8f25ffa941e1dcbb15a34935a488'))
private_key = open('../../private_key.txt').readline()

identity = Snet(private_key=private_key)

try:
	#client = identity.client("snet", "face-detect", channel_id=6249, endpoi)
	client = identity.client("snet", "network-analytics-nodeimportance", channel_id=6211)
	# in kovan channel_id=2414, in ropsten channel_id=6211
	#print("Yeah No Error")
	#print("AGI tokens available:", identity.balance())
	#client.open_channel()
	#print("channel created")
except Exception as e:
	print("Error 1")
	print("\nEEEROOOR", e)

import network_analytics_node_importance_pb2
import network_analytics_node_importance_pb2_grpc

graph = {
        "nodes": ["1","2","3","4","5","6"],
        "edges": [["1","2"],["1","4"],["2","3"],["2","5"],["3","4"],["3","6"],["4","6"]]}

edges_req = []
for e in graph["edges"]:
	edges_req.append(network_analytics_node_importance_pb2.Edge(edge=e))

graph_in = network_analytics_node_importance_pb2.Graph(nodes=graph["nodes"],edges=edges_req)

try:

	stub = network_analytics_node_importance_pb2_grpc.NetworkAnalyticsNodeImportanceStub(client.grpc_channel)
	#print("Stub initalized")
	request = network_analytics_node_importance_pb2.CentralNodeRequest(graph=graph_in)
	#graph='"graph": {"nodes": ["1","2","3","4","5","6"], "edges": [{"edge": ["1","2"]},{"edge": ["1","4"]},{"edge": ["2","3"]},{"edge": ["2","5"]},{"edge": ["3","4"]},{"edge": ["3","6"]},{"edge": ["4","6"]}]}', source_node="1", target_node="6")
	#print("Graph Passed")
	result = stub.CentralNodes(request)
	print(result)
except Exception as e:
	print("\nError 2")
	print("EEEROOOR", e)


"""
try:
	import translate_pb2 as tp
	import translate_pb2_grpc as tpg
	stub = tpg.TranslationStub(translation.grpc_channel)
	request = tp.Request(text="Hello World.", source_language="en", target_language="de")
	resp = stub.translate(request).translation
	print(resp)
except Exception as e:
	print("Error 1")
	print("\nEEEROOOR", e)
"""

"""

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
"""


"""
try:
	### snet-sdk-python with full grpc specification
	import face_detect_pb2_grpc
	import face_detect_pb2
	stub = face_detect_pb2_grpc.FaceDetectStub(client.grpc_channel)
	request = face_detect_pb2.Request(image=face_detect_pb2.ImageRGB(content='cat.jpeg'))
	faces = stub.FindFace(request)

	### simple-sdk version
	#stub = client.get_stub()
	#request_cls = client.get_request(method='FindFace')
	#request = request_cls(image={content=...})
	#rez = stub.FindFace(request)

except Exception as e:
	print("Error 2")
	print("\nEEEROOOR", e)
"""