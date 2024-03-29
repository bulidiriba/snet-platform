# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image_retrival.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='image_retrival.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14image_retrival.proto\"0\n\x0bImageFileIn\x12\r\n\x05image\x18\x01 \x01(\t\x12\x12\n\nsimilarity\x18\x04 \x01(\t\"m\n\x0cImageFileOut\x12\x11\n\timageOut1\x18\x04 \x01(\t\x12\x11\n\timageOut2\x18\x05 \x01(\t\x12\x11\n\timageOut3\x18\x06 \x01(\t\x12\x11\n\timageOut4\x18\x07 \x01(\t\x12\x11\n\timageOut5\x18\x08 \x01(\t2<\n\x0cSimilarImage\x12,\n\x0b\x46indSimilar\x12\x0c.ImageFileIn\x1a\r.ImageFileOut\"\x00\x62\x06proto3')
)




_IMAGEFILEIN = _descriptor.Descriptor(
  name='ImageFileIn',
  full_name='ImageFileIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='ImageFileIn.image', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='similarity', full_name='ImageFileIn.similarity', index=1,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=24,
  serialized_end=72,
)


_IMAGEFILEOUT = _descriptor.Descriptor(
  name='ImageFileOut',
  full_name='ImageFileOut',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='imageOut1', full_name='ImageFileOut.imageOut1', index=0,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imageOut2', full_name='ImageFileOut.imageOut2', index=1,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imageOut3', full_name='ImageFileOut.imageOut3', index=2,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imageOut4', full_name='ImageFileOut.imageOut4', index=3,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imageOut5', full_name='ImageFileOut.imageOut5', index=4,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=74,
  serialized_end=183,
)

DESCRIPTOR.message_types_by_name['ImageFileIn'] = _IMAGEFILEIN
DESCRIPTOR.message_types_by_name['ImageFileOut'] = _IMAGEFILEOUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageFileIn = _reflection.GeneratedProtocolMessageType('ImageFileIn', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEFILEIN,
  __module__ = 'image_retrival_pb2'
  # @@protoc_insertion_point(class_scope:ImageFileIn)
  ))
_sym_db.RegisterMessage(ImageFileIn)

ImageFileOut = _reflection.GeneratedProtocolMessageType('ImageFileOut', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEFILEOUT,
  __module__ = 'image_retrival_pb2'
  # @@protoc_insertion_point(class_scope:ImageFileOut)
  ))
_sym_db.RegisterMessage(ImageFileOut)



_SIMILARIMAGE = _descriptor.ServiceDescriptor(
  name='SimilarImage',
  full_name='SimilarImage',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=185,
  serialized_end=245,
  methods=[
  _descriptor.MethodDescriptor(
    name='FindSimilar',
    full_name='SimilarImage.FindSimilar',
    index=0,
    containing_service=None,
    input_type=_IMAGEFILEIN,
    output_type=_IMAGEFILEOUT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIMILARIMAGE)

DESCRIPTOR.services_by_name['SimilarImage'] = _SIMILARIMAGE

# @@protoc_insertion_point(module_scope)
