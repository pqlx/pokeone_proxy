# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Ping.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bcl_pb2 as bcl__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Ping.proto',
  package='PSXAPI.Request49',
  syntax='proto2',
  serialized_pb=_b('\n\nPing.proto\x12\x10PSXAPI.Request49\x1a\tbcl.proto\"*\n\x04Ping\x12\"\n\x0b\x44\x61teTimeUtc\x18\x01 \x02(\x0b\x32\r.bcl.DateTime')
  ,
  dependencies=[bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='PSXAPI.Request49.Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='DateTimeUtc', full_name='PSXAPI.Request49.Ping.DateTimeUtc', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=43,
  serialized_end=85,
)

_PING.fields_by_name['DateTimeUtc'].message_type = bcl__pb2._DATETIME
DESCRIPTOR.message_types_by_name['Ping'] = _PING

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), dict(
  DESCRIPTOR = _PING,
  __module__ = 'Ping_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request49.Ping)
  ))
_sym_db.RegisterMessage(Ping)


# @@protoc_insertion_point(module_scope)
