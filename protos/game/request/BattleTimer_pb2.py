# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BattleTimer.proto

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
  name='BattleTimer.proto',
  package='PSXAPI.Request10',
  syntax='proto2',
  serialized_pb=_b('\n\x11\x42\x61ttleTimer.proto\x12\x10PSXAPI.Request10\"\r\n\x0b\x42\x61ttleTimer')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BATTLETIMER = _descriptor.Descriptor(
  name='BattleTimer',
  full_name='PSXAPI.Request10.BattleTimer',
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
  serialized_start=39,
  serialized_end=52,
)

DESCRIPTOR.message_types_by_name['BattleTimer'] = _BATTLETIMER

BattleTimer = _reflection.GeneratedProtocolMessageType('BattleTimer', (_message.Message,), dict(
  DESCRIPTOR = _BATTLETIMER,
  __module__ = 'BattleTimer_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request10.BattleTimer)
  ))
_sym_db.RegisterMessage(BattleTimer)


# @@protoc_insertion_point(module_scope)
