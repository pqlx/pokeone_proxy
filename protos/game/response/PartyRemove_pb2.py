# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PartyRemove.proto

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


import bcl_pb2 as bcl__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='PartyRemove.proto',
  package='PSXAPI.Response60',
  syntax='proto2',
  serialized_pb=_b('\n\x11PartyRemove.proto\x12\x11PSXAPI.Response60\x1a\tbcl.proto\"d\n\x0bPartyRemove\x12\x19\n\x06UserId\x18\x01 \x01(\x0b\x32\t.bcl.Guid\x12:\n\x06Reason\x18\x02 \x01(\x0e\x32$.PSXAPI.Response60.PartyRemoveReason:\x04Left*)\n\x11PartyRemoveReason\x12\x08\n\x04Left\x10\x00\x12\n\n\x06Kicked\x10\x01')
  ,
  dependencies=[bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PARTYREMOVEREASON = _descriptor.EnumDescriptor(
  name='PartyRemoveReason',
  full_name='PSXAPI.Response60.PartyRemoveReason',
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
  serialized_start=153,
  serialized_end=194,
)
_sym_db.RegisterEnumDescriptor(_PARTYREMOVEREASON)

PartyRemoveReason = enum_type_wrapper.EnumTypeWrapper(_PARTYREMOVEREASON)
Left = 0
Kicked = 1



_PARTYREMOVE = _descriptor.Descriptor(
  name='PartyRemove',
  full_name='PSXAPI.Response60.PartyRemove',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='UserId', full_name='PSXAPI.Response60.PartyRemove.UserId', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Reason', full_name='PSXAPI.Response60.PartyRemove.Reason', index=1,
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
  serialized_start=51,
  serialized_end=151,
)

_PARTYREMOVE.fields_by_name['UserId'].message_type = bcl__pb2._GUID
_PARTYREMOVE.fields_by_name['Reason'].enum_type = _PARTYREMOVEREASON
DESCRIPTOR.message_types_by_name['PartyRemove'] = _PARTYREMOVE
DESCRIPTOR.enum_types_by_name['PartyRemoveReason'] = _PARTYREMOVEREASON

PartyRemove = _reflection.GeneratedProtocolMessageType('PartyRemove', (_message.Message,), dict(
  DESCRIPTOR = _PARTYREMOVE,
  __module__ = 'PartyRemove_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response60.PartyRemove)
  ))
_sym_db.RegisterMessage(PartyRemove)


# @@protoc_insertion_point(module_scope)
