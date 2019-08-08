from snet_sdk import Snet
import edgedetect_pb2
import edgedetect_pb2_grpc
import base64

private_key = open('../../private_key.txt').readline()
identity = Snet(private_key=private_key)


try:
	client = identity.client("snet", "holistic-edge-detection-service", channel_id=6258)
	# in kovan channel_id = 2410, in ropsten channel_id = 6258
	# if you change the network from kovan to ropsten or vice versa change also this channel_id to respective of that
	# by checking just in the terminal with snet channel print-initialized, because the channel_id of the same service 
	# to change the network go into snet_sdk/__init__.py then change in the snet_sdk_defaults
	# in different network is different
	#client.open_channel()
except Exception as e:
	print("Error 1")
	print("\nEEEROOOR", e)

with open('sample.png', 'rb') as f:
	img = f.read()
	image = base64.b64encode(img).decode('utf-8')

#client_test = ClientTest()
#stub = client_test.open_grpc_channel()
try:
	stub = edgedetect_pb2_grpc.EdgedetectStub(client.grpc_channel)
	image_file = edgedetect_pb2.ImageFile(image=image, image_type='RGB')
	image_result = stub.DetectEdge(image_file)
	print(response)
	binary_image = base64.b64decode(image_result.image)
	Image.frombytes(data=binary_image,size=(480,320),mode='RGB').save('img.png')

except Exception as e:
	print("\nError 2")
	print("EEEROOOR", str(e))
