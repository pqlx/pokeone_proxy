# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game/request/Evs.proto

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
  name='game/request/Evs.proto',
  package='PSXAPI.Request1439515700',
  syntax='proto2',
  serialized_pb=_b('\n\x16game/request/Evs.proto\x12\x18PSXAPI.Request1439515700\x1a\tbcl.proto\"\xdd\x01\n\x03\x45vs\x12\x1a\n\x07Pokemon\x18\x01 \x01(\x0b\x32\t.bcl.Guid\x12U\n\x06\x41\x63tion\x18\x02 \x01(\x0e\x32<.PSXAPI.Request1439515700.PREFIX_AGDFASBV435401762.EvsAction:\x07Request\x12\r\n\x02Hp\x18\x03 \x01(\x05:\x01\x30\x12\x0e\n\x03\x41tk\x18\x04 \x01(\x05:\x01\x30\x12\x0e\n\x03\x44\x65\x66\x18\x05 \x01(\x05:\x01\x30\x12\x10\n\x05Speed\x18\x06 \x01(\x05:\x01\x30\x12\x10\n\x05SpAtk\x18\x07 \x01(\x05:\x01\x30\x12\x10\n\x05SpDef\x18\x08 \x01(\x05:\x01\x30\"J\n\x18PREFIX_AGDFASBV435401762\".\n\tEvsAction\x12\x0b\n\x07Request\x10\x00\x12\t\n\x05Skill\x10\x01\x12\t\n\x05Reset\x10\x02')
  ,
  dependencies=[bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PREFIX_AGDFASBV435401762_EVSACTION = _descriptor.EnumDescriptor(
  name='EvsAction',
  full_name='PSXAPI.Request1439515700.PREFIX_AGDFASBV435401762.EvsAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Request', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Skill', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Reset', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=315,
  serialized_end=361,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV435401762_EVSACTION)


_EVS = _descriptor.Descriptor(
  name='Evs',
  full_name='PSXAPI.Request1439515700.Evs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Pokemon', full_name='PSXAPI.Request1439515700.Evs.Pokemon', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Action', full_name='PSXAPI.Request1439515700.Evs.Action', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Hp', full_name='PSXAPI.Request1439515700.Evs.Hp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Atk', full_name='PSXAPI.Request1439515700.Evs.Atk', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Def', full_name='PSXAPI.Request1439515700.Evs.Def', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Speed', full_name='PSXAPI.Request1439515700.Evs.Speed', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SpAtk', full_name='PSXAPI.Request1439515700.Evs.SpAtk', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SpDef', full_name='PSXAPI.Request1439515700.Evs.SpDef', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=64,
  serialized_end=285,
)


_PREFIX_AGDFASBV435401762 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV435401762',
  full_name='PSXAPI.Request1439515700.PREFIX_AGDFASBV435401762',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV435401762_EVSACTION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=361,
)

_EVS.fields_by_name['Pokemon'].message_type = bcl__pb2._GUID
_EVS.fields_by_name['Action'].enum_type = _PREFIX_AGDFASBV435401762_EVSACTION
_PREFIX_AGDFASBV435401762_EVSACTION.containing_type = _PREFIX_AGDFASBV435401762
DESCRIPTOR.message_types_by_name['Evs'] = _EVS
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV435401762'] = _PREFIX_AGDFASBV435401762

Evs = _reflection.GeneratedProtocolMessageType('Evs', (_message.Message,), dict(
  DESCRIPTOR = _EVS,
  __module__ = 'game.request.Evs_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request1439515700.Evs)
  ))
_sym_db.RegisterMessage(Evs)

PREFIX_AGDFASBV435401762 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV435401762', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV435401762,
  __module__ = 'game.request.Evs_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request1439515700.PREFIX_AGDFASBV435401762)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV435401762)


# @@protoc_insertion_point(module_scope)
