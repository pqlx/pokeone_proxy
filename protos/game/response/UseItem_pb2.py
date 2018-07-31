# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UseItem.proto

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
  name='UseItem.proto',
  package='PSXAPI.Response85',
  syntax='proto2',
  serialized_pb=_b('\n\rUseItem.proto\x12\x11PSXAPI.Response85\x1a\tbcl.proto\"p\n\x07UseItem\x12\x38\n\x06Result\x18\x01 \x01(\x0e\x32 .PSXAPI.Response85.UseItemResult:\x06\x46\x61iled\x12\x0f\n\x04Item\x18\x02 \x01(\x05:\x01\x30\x12\x1a\n\x07Pokemon\x18\x03 \x01(\x0b\x32\t.bcl.Guid*n\n\rUseItemResult\x12\n\n\x06\x46\x61iled\x10\x00\x12\x0b\n\x07Success\x10\x01\x12\x0f\n\x0bInvalidItem\x10\x02\x12\x12\n\x0eInvalidPokemon\x10\x03\x12\x0e\n\nNotInTrade\x10\x04\x12\x0f\n\x0bNotInBattle\x10\x05')
  ,
  dependencies=[bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_USEITEMRESULT = _descriptor.EnumDescriptor(
  name='UseItemResult',
  full_name='PSXAPI.Response85.UseItemResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Failed', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Success', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InvalidItem', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InvalidPokemon', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NotInTrade', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NotInBattle', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=161,
  serialized_end=271,
)
_sym_db.RegisterEnumDescriptor(_USEITEMRESULT)

UseItemResult = enum_type_wrapper.EnumTypeWrapper(_USEITEMRESULT)
Failed = 0
Success = 1
InvalidItem = 2
InvalidPokemon = 3
NotInTrade = 4
NotInBattle = 5



_USEITEM = _descriptor.Descriptor(
  name='UseItem',
  full_name='PSXAPI.Response85.UseItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Result', full_name='PSXAPI.Response85.UseItem.Result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Item', full_name='PSXAPI.Response85.UseItem.Item', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Pokemon', full_name='PSXAPI.Response85.UseItem.Pokemon', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=47,
  serialized_end=159,
)

_USEITEM.fields_by_name['Result'].enum_type = _USEITEMRESULT
_USEITEM.fields_by_name['Pokemon'].message_type = bcl__pb2._GUID
DESCRIPTOR.message_types_by_name['UseItem'] = _USEITEM
DESCRIPTOR.enum_types_by_name['UseItemResult'] = _USEITEMRESULT

UseItem = _reflection.GeneratedProtocolMessageType('UseItem', (_message.Message,), dict(
  DESCRIPTOR = _USEITEM,
  __module__ = 'UseItem_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response85.UseItem)
  ))
_sym_db.RegisterMessage(UseItem)


# @@protoc_insertion_point(module_scope)
