
from snet_sdk import Snet
private_key = open('../../private_key.txt').readline()

identity = Snet(private_key=private_key)
channel_id = [channel_id]# the already initialized channel id of this service, if not initialize it in snet-cli 

try:
	client = identity.client("snet", "network-analytics-nodeimportance", channel_id=channel_id)
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
	request = network_analytics_node_importance_pb2.CentralNodeRequest(graph=graph_in)
	result = stub.CentralNodes(request)
	print(result)
except Exception as e:
	print("\nError 2")
	print("EEEROOOR", e)