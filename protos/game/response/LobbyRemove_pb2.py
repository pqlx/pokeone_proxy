# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LobbyRemove.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='LobbyRemove.proto',
  package='PSXAPI.Response46',
  syntax='proto2',
  serialized_pb=_b('\n\x11LobbyRemove.proto\x12\x11PSXAPI.Response46\"W\n\x0bLobbyRemove\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12:\n\x06Reason\x18\x02 \x01(\x0e\x32$.PSXAPI.Response46.LobbyRemoveReason:\x04Left*)\n\x11LobbyRemoveReason\x12\x08\n\x04Left\x10\x00\x12\n\n\x06Kicked\x10\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_LOBBYREMOVEREASON = _descriptor.EnumDescriptor(
  name='LobbyRemoveReason',
  full_name='PSXAPI.Response46.LobbyRemoveReason',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Left', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Kicked', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=129,
  serialized_end=170,
)
_sym_db.RegisterEnumDescriptor(_LOBBYREMOVEREASON)

LobbyRemoveReason = enum_type_wrapper.EnumTypeWrapper(_LOBBYREMOVEREASON)
Left = 0
Kicked = 1



_LOBBYREMOVE = _descriptor.Descriptor(
  name='LobbyRemove',
  full_name='PSXAPI.Response46.LobbyRemove',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='PSXAPI.Response46.LobbyRemove.Name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Reason', full_name='PSXAPI.Response46.LobbyRemove.Reason', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=40,
  serialized_end=127,
)

_LOBBYREMOVE.fields_by_name['Reason'].enum_type = _LOBBYREMOVEREASON
DESCRIPTOR.message_types_by_name['LobbyRemove'] = _LOBBYREMOVE
DESCRIPTOR.enum_types_by_name['LobbyRemoveReason'] = _LOBBYREMOVEREASON

LobbyRemove = _reflection.GeneratedProtocolMessageType('LobbyRemove', (_message.Message,), dict(
  DESCRIPTOR = _LOBBYREMOVE,
  __module__ = 'LobbyRemove_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response46.LobbyRemove)
  ))
_sym_db.RegisterMessage(LobbyRemove)


# @@protoc_insertion_point(module_scope)
