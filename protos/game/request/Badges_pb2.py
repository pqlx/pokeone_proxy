# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Badges.proto

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
  name='Badges.proto',
  package='PSXAPI.Request3',
  syntax='proto2',
  serialized_pb=_b('\n\x0c\x42\x61\x64ges.proto\x12\x0fPSXAPI.Request3\"\x08\n\x06\x42\x61\x64ges')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BADGES = _descriptor.Descriptor(
  name='Badges',
  full_name='PSXAPI.Request3.Badges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=33,
  serialized_end=41,
)

DESCRIPTOR.message_types_by_name['Badges'] = _BADGES

Badges = _reflection.GeneratedProtocolMessageType('Badges', (_message.Message,), dict(
  DESCRIPTOR = _BADGES,
  __module__ = 'Badges_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request3.Badges)
  ))
_sym_db.RegisterMessage(Badges)


# @@protoc_insertion_point(module_scope)
