# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: maps/response/DebugMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='maps/response/DebugMessage.proto',
  package='MAPAPI.Response1273581065',
  syntax='proto2',
  serialized_pb=_b('\n maps/response/DebugMessage.proto\x12\x19MAPAPI.Response1273581065\"\x1f\n\x0c\x44\x65\x62ugMessage\x12\x0f\n\x07Message\x18\x01 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DEBUGMESSAGE = _descriptor.Descriptor(
  name='DebugMessage',
  full_name='MAPAPI.Response1273581065.DebugMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Message', full_name='MAPAPI.Response1273581065.DebugMessage.Message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['DebugMessage'] = _DEBUGMESSAGE

DebugMessage = _reflection.GeneratedProtocolMessageType('DebugMessage', (_message.Message,), dict(
  DESCRIPTOR = _DEBUGMESSAGE,
  __module__ = 'maps.response.DebugMessage_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response1273581065.DebugMessage)
  ))
_sym_db.RegisterMessage(DebugMessage)


# @@protoc_insertion_point(module_scope)
