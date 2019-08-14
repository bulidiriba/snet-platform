from snet_sdk import Snet
import network_analytics_robustness_pb2
import network_analytics_robustness_pb2_grpc

private_key = open('../../../../private_key.txt').readline()

identity = Snet(private_key=private_key)

channel_id = [channel_id]# the already initialized channel id of this service, if not initialize it in snet-cli 


try:
	client = identity.client("snet", "network-analytics-robustness", channel_id=channel_id)
	# if you change the network from kovan to ropsten or vice versa change also this channel_id to respective of that
	# by checking just in the terminal with snet channel print-initialized, because the channel_id of the same service 
	# to change the network go into snet_sdk/__init__.py then change in the snet_sdk_defaults
	# in different network is different
	# # client.open_channel()
except Exception as e:
	print("Error 1")
	print("\nEEEROOOR", e)

graph_2 = {
        "nodes": ["1","2","3","4","5","6"],
        "edges": [["1","2"],["1","4"],["2","3"],["2","5"],["3","4"],["3","6"],["4","6"]]
        }

source_node = '1'
target_node = '6'

edges_req = []
for e in graph_2["edges"]:
	edges_req.append(network_analytics_robustness_pb2.Edge(edge=e))

graph_in = network_analytics_robustness_pb2.Graph(nodes=graph_2["nodes"],edges=edges_req)

try:
	stub = network_analytics_robustness_pb2_grpc.NetworkAnalyticsRobustnessStub(client.grpc_channel)
	request = network_analytics_robustness_pb2.MinNodesToRemoveRequest(graph=graph_in, source_node=source_node,target_node=target_node)
	response = stub.MinNodesToRemove(request)
	print(response)
except Exception as e:
	print("\nError 2")
	print("EEEROOOR", str(e))