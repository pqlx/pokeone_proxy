# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: JoinMapSession.proto

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
  name='JoinMapSession.proto',
  package='MAPAPI.Request2',
  syntax='proto2',
  serialized_pb=_b('\n\x14JoinMapSession.proto\x12\x0fMAPAPI.Request2\"!\n\x0eJoinMapSession\x12\x0f\n\x07MapName\x18\x01 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_JOINMAPSESSION = _descriptor.Descriptor(
  name='JoinMapSession',
  full_name='MAPAPI.Request2.JoinMapSession',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MapName', full_name='MAPAPI.Request2.JoinMapSession.MapName', index=0,
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
  serialized_start=41,
  serialized_end=74,
)

DESCRIPTOR.message_types_by_name['JoinMapSession'] = _JOINMAPSESSION

JoinMapSession = _reflection.GeneratedProtocolMessageType('JoinMapSession', (_message.Message,), dict(
  DESCRIPTOR = _JOINMAPSESSION,
  __module__ = 'JoinMapSession_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Request2.JoinMapSession)
  ))
_sym_db.RegisterMessage(JoinMapSession)


# @@protoc_insertion_point(module_scope)
