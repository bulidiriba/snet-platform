# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: network_analytics_bipartite.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='network_analytics_bipartite.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!network_analytics_bipartite.proto\"\x14\n\x04\x45\x64ge\x12\x0c\n\x04\x65\x64ge\x18\x01 \x03(\t\"=\n\x05Graph\x12\r\n\x05nodes\x18\x01 \x03(\t\x12\x14\n\x05\x65\x64ges\x18\x02 \x03(\x0b\x32\x05.Edge\x12\x0f\n\x07weights\x18\x03 \x03(\x01\":\n\x0e\x42ipartiteNodes\x12\x13\n\x0b\x62ipartite_0\x18\x01 \x03(\t\x12\x13\n\x0b\x62ipartite_1\x18\x02 \x03(\t\"a\n\x0e\x42ipartiteGraph\x12\x13\n\x0b\x62ipartite_0\x18\x01 \x03(\t\x12\x13\n\x0b\x62ipartite_1\x18\x02 \x03(\t\x12\x14\n\x05\x65\x64ges\x18\x03 \x03(\x0b\x32\x05.Edge\x12\x0f\n\x07weights\x18\x04 \x03(\x01\"M\n\x15\x42ipartiteGraphRequest\x12\x1e\n\x05nodes\x18\x01 \x01(\x0b\x32\x0f.BipartiteNodes\x12\x14\n\x05\x65\x64ges\x18\x02 \x03(\x0b\x32\x05.Edge\"Z\n\x16\x42ipartiteGraphResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x1f\n\x06output\x18\x03 \x01(\x0b\x32\x0f.BipartiteGraph\"W\n\x16ProjecetedGraphRequest\x12\x1e\n\x05graph\x18\x01 \x01(\x0b\x32\x0f.BipartiteGraph\x12\r\n\x05nodes\x18\x02 \x03(\t\x12\x0e\n\x06weight\x18\x03 \x01(\t\"R\n\x17ProjecetedGraphResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x16\n\x06output\x18\x03 \x01(\x0b\x32\x06.Graph2\xa7\x01\n\x19NetworkAnalyticsBipartite\x12\x43\n\x0e\x42ipartiteGraph\x12\x16.BipartiteGraphRequest\x1a\x17.BipartiteGraphResponse\"\x00\x12\x45\n\x0eProjectedGraph\x12\x17.ProjecetedGraphRequest\x1a\x18.ProjecetedGraphResponse\"\x00\x62\x06proto3')
)




_EDGE = _descriptor.Descriptor(
  name='Edge',
  full_name='Edge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='edge', full_name='Edge.edge', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=57,
)


_GRAPH = _descriptor.Descriptor(
  name='Graph',
  full_name='Graph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='Graph.nodes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edges', full_name='Graph.edges', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weights', full_name='Graph.weights', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=120,
)


_BIPARTITENODES = _descriptor.Descriptor(
  name='BipartiteNodes',
  full_name='BipartiteNodes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bipartite_0', full_name='BipartiteNodes.bipartite_0', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bipartite_1', full_name='BipartiteNodes.bipartite_1', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=180,
)


_BIPARTITEGRAPH = _descriptor.Descriptor(
  name='BipartiteGraph',
  full_name='BipartiteGraph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bipartite_0', full_name='BipartiteGraph.bipartite_0', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bipartite_1', full_name='BipartiteGraph.bipartite_1', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edges', full_name='BipartiteGraph.edges', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weights', full_name='BipartiteGraph.weights', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=279,
)


_BIPARTITEGRAPHREQUEST = _descriptor.Descriptor(
  name='BipartiteGraphRequest',
  full_name='BipartiteGraphRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='BipartiteGraphRequest.nodes', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edges', full_name='BipartiteGraphRequest.edges', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=358,
)


_BIPARTITEGRAPHRESPONSE = _descriptor.Descriptor(
  name='BipartiteGraphResponse',
  full_name='BipartiteGraphResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='BipartiteGraphResponse.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='BipartiteGraphResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output', full_name='BipartiteGraphResponse.output', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=360,
  serialized_end=450,
)


_PROJECETEDGRAPHREQUEST = _descriptor.Descriptor(
  name='ProjecetedGraphRequest',
  full_name='ProjecetedGraphRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='graph', full_name='ProjecetedGraphRequest.graph', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='ProjecetedGraphRequest.nodes', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='ProjecetedGraphRequest.weight', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=452,
  serialized_end=539,
)


_PROJECETEDGRAPHRESPONSE = _descriptor.Descriptor(
  name='ProjecetedGraphResponse',
  full_name='ProjecetedGraphResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ProjecetedGraphResponse.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='ProjecetedGraphResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output', full_name='ProjecetedGraphResponse.output', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=541,
  serialized_end=623,
)

_GRAPH.fields_by_name['edges'].message_type = _EDGE
_BIPARTITEGRAPH.fields_by_name['edges'].message_type = _EDGE
_BIPARTITEGRAPHREQUEST.fields_by_name['nodes'].message_type = _BIPARTITENODES
_BIPARTITEGRAPHREQUEST.fields_by_name['edges'].message_type = _EDGE
_BIPARTITEGRAPHRESPONSE.fields_by_name['output'].message_type = _BIPARTITEGRAPH
_PROJECETEDGRAPHREQUEST.fields_by_name['graph'].message_type = _BIPARTITEGRAPH
_PROJECETEDGRAPHRESPONSE.fields_by_name['output'].message_type = _GRAPH
DESCRIPTOR.message_types_by_name['Edge'] = _EDGE
DESCRIPTOR.message_types_by_name['Graph'] = _GRAPH
DESCRIPTOR.message_types_by_name['BipartiteNodes'] = _BIPARTITENODES
DESCRIPTOR.message_types_by_name['BipartiteGraph'] = _BIPARTITEGRAPH
DESCRIPTOR.message_types_by_name['BipartiteGraphRequest'] = _BIPARTITEGRAPHREQUEST
DESCRIPTOR.message_types_by_name['BipartiteGraphResponse'] = _BIPARTITEGRAPHRESPONSE
DESCRIPTOR.message_types_by_name['ProjecetedGraphRequest'] = _PROJECETEDGRAPHREQUEST
DESCRIPTOR.message_types_by_name['ProjecetedGraphResponse'] = _PROJECETEDGRAPHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Edge = _reflection.GeneratedProtocolMessageType('Edge', (_message.Message,), dict(
  DESCRIPTOR = _EDGE,
  __module__ = 'network_analytics_bipartite_pb2'
  # @@protoc_insertion_point(class_scope:Edge)
  ))
_sym_db.RegisterMessage(Edge)

Graph = _reflection.GeneratedProtocolMessageType('Graph', (_message.Message,), dict(
  DESCRIPTOR = _GRAPH,
  __module__ = 'network_analytics_bipartite_pb2'
  # @@protoc_insertion_point(class_scope:Graph)
  ))
_sym_db.RegisterMessage(Graph)

BipartiteNodes = _reflection.GeneratedProtocolMessageType('BipartiteNodes', (_message.Message,), dict(
  DESCRIPTOR = _BIPARTITENODES,
  __module__ = 'network_analytics_bipartite_pb2'
  # @@protoc_insertion_point(class_scope:BipartiteNodes)
  ))
_sym_db.RegisterMessage(BipartiteNodes)

BipartiteGraph = _reflection.GeneratedProtocolMessageType('BipartiteGraph', (_message.Message,), dict(
  DESCRIPTOR = _BIPARTITEGRAPH,
  __module__ = 'network_analytics_bipartite_pb2'
  # @@protoc_insertion_point(class_scope:BipartiteGraph)
  ))
_sym_db.RegisterMessage(BipartiteGraph)

BipartiteGraphRequest = _reflection.GeneratedProtocolMessageType('BipartiteGraphRequest', (_message.Message,), dict(
  DESCRIPTOR = _BIPARTITEGRAPHREQUEST,
  __module__ = 'network_analytics_bipartite_pb2'
  # @@protoc_insertion_point(class_scope:BipartiteGraphRequest)
  ))
_sym_db.RegisterMessage(BipartiteGraphRequest)

BipartiteGraphResponse = _reflection.GeneratedProtocolMessageType('BipartiteGraphResponse', (_message.Message,), dict(
  DESCRIPTOR = _BIPARTITEGRAPHRESPONSE,
  __module__ = 'network_analytics_bipartite_pb2'
  # @@protoc_insertion_point(class_scope:BipartiteGraphResponse)
  ))
_sym_db.RegisterMessage(BipartiteGraphResponse)

ProjecetedGraphRequest = _reflection.GeneratedProtocolMessageType('ProjecetedGraphRequest', (_message.Message,), dict(
  DESCRIPTOR = _PROJECETEDGRAPHREQUEST,
  __module__ = 'network_analytics_bipartite_pb2'
  # @@protoc_insertion_point(class_scope:ProjecetedGraphRequest)
  ))
_sym_db.RegisterMessage(ProjecetedGraphRequest)

ProjecetedGraphResponse = _reflection.GeneratedProtocolMessageType('ProjecetedGraphResponse', (_message.Message,), dict(
  DESCRIPTOR = _PROJECETEDGRAPHRESPONSE,
  __module__ = 'network_analytics_bipartite_pb2'
  # @@protoc_insertion_point(class_scope:ProjecetedGraphResponse)
  ))
_sym_db.RegisterMessage(ProjecetedGraphResponse)



_NETWORKANALYTICSBIPARTITE = _descriptor.ServiceDescriptor(
  name='NetworkAnalyticsBipartite',
  full_name='NetworkAnalyticsBipartite',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=626,
  serialized_end=793,
  methods=[
  _descriptor.MethodDescriptor(
    name='BipartiteGraph',
    full_name='NetworkAnalyticsBipartite.BipartiteGraph',
    index=0,
    containing_service=None,
    input_type=_BIPARTITEGRAPHREQUEST,
    output_type=_BIPARTITEGRAPHRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ProjectedGraph',
    full_name='NetworkAnalyticsBipartite.ProjectedGraph',
    index=1,
    containing_service=None,
    input_type=_PROJECETEDGRAPHREQUEST,
    output_type=_PROJECETEDGRAPHRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NETWORKANALYTICSBIPARTITE)

DESCRIPTOR.services_by_name['NetworkAnalyticsBipartite'] = _NETWORKANALYTICSBIPARTITE

# @@protoc_insertion_point(module_scope)
