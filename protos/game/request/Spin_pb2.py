# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Spin.proto

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
  name='Spin.proto',
  package='PSXAPI.Request60',
  syntax='proto2',
  serialized_pb=_b('\n\nSpin.proto\x12\x10PSXAPI.Request60\"E\n\x04Spin\x12\r\n\x02ID\x18\x01 \x01(\x05:\x01\x30\x12.\n\x03\x42\x65t\x18\x02 \x01(\x0e\x32\x19.PSXAPI.Request60.SpinBet:\x06__None*6\n\x07SpinBet\x12\n\n\x06__None\x10\x00\x12\t\n\x05\x43oin1\x10\x01\x12\t\n\x05\x43oin2\x10\x02\x12\t\n\x05\x43oin3\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_SPINBET = _descriptor.EnumDescriptor(
  name='SpinBet',
  full_name='PSXAPI.Request60.SpinBet',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='__None', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Coin1', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Coin2', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Coin3', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=103,
  serialized_end=157,
)
_sym_db.RegisterEnumDescriptor(_SPINBET)

SpinBet = enum_type_wrapper.EnumTypeWrapper(_SPINBET)
__None = 0
Coin1 = 1
Coin2 = 2
Coin3 = 3



_SPIN = _descriptor.Descriptor(
  name='Spin',
  full_name='PSXAPI.Request60.Spin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='PSXAPI.Request60.Spin.ID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Bet', full_name='PSXAPI.Request60.Spin.Bet', index=1,
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
  serialized_start=32,
  serialized_end=101,
)

_SPIN.fields_by_name['Bet'].enum_type = _SPINBET
DESCRIPTOR.message_types_by_name['Spin'] = _SPIN
DESCRIPTOR.enum_types_by_name['SpinBet'] = _SPINBET

Spin = _reflection.GeneratedProtocolMessageType('Spin', (_message.Message,), dict(
  DESCRIPTOR = _SPIN,
  __module__ = 'Spin_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request60.Spin)
  ))
_sym_db.RegisterMessage(Spin)


# @@protoc_insertion_point(module_scope)
