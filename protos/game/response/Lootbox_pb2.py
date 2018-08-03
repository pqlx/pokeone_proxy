# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game/response/Lootbox.proto

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
  name='game/response/Lootbox.proto',
  package='PSXAPI.Response580073471',
  syntax='proto2',
  serialized_pb=_b('\n\x1bgame/response/Lootbox.proto\x12\x18PSXAPI.Response580073471\"\xa0\x01\n\x19PREFIX_AGDFASBV1842323304\"\x82\x01\n\x08LootType\x12\r\n\tNoneValue\x10\x00\x12\t\n\x05Money\x10\x01\x12\x08\n\x04Gold\x10\x02\x12\x08\n\x04Item\x10\x03\x12\x0b\n\x07Pokemon\x10\x04\x12\n\n\x06\x43lothe\x10\x05\x12\x07\n\x03Hat\x10\x06\x12\t\n\x05Mount\x10\x07\x12\r\n\tSurfMount\x10\x08\x12\x0c\n\x08\x46lyMount\x10\t\"\x8d\x02\n\x07Lootbox\x12\\\n\x06\x41\x63tion\x18\x01 \x01(\x0e\x32\x41.PSXAPI.Response580073471.PREFIX_AGDFASBV1949913223.LootboxAction:\tNoneValue\x12X\n\x04Type\x18\x02 \x01(\x0e\x32?.PSXAPI.Response580073471.PREFIX_AGDFASBV1416211215.LootboxType:\tNoneValue\x12\x14\n\tRemaining\x18\x03 \x01(\r:\x01\x30\x12\x34\n\x05Rolls\x18\x04 \x03(\x0b\x32%.PSXAPI.Response580073471.LootboxRoll\"S\n\x19PREFIX_AGDFASBV1949913223\"6\n\rLootboxAction\x12\r\n\tNoneValue\x10\x00\x12\n\n\x06Opened\x10\x01\x12\n\n\x06Update\x10\x02\"\xc7\x01\n\x0bLootboxRoll\x12Y\n\x08LootType\x18\x01 \x01(\x0e\x32<.PSXAPI.Response580073471.PREFIX_AGDFASBV1842323304.LootType:\tNoneValue\x12\x0e\n\x03Num\x18\x02 \x01(\x05:\x01\x30\x12\x18\n\tDuplicate\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x18\n\rDuplicateGold\x18\x04 \x01(\r:\x01\x30\x12\x19\n\x0e\x44uplicateMoney\x18\x05 \x01(\r:\x01\x30\"P\n\x19PREFIX_AGDFASBV1416211215\"3\n\x0bLootboxType\x12\r\n\tNoneValue\x10\x00\x12\t\n\x05Small\x10\x01\x12\n\n\x06Normal\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PREFIX_AGDFASBV1842323304_LOOTTYPE = _descriptor.EnumDescriptor(
  name='LootType',
  full_name='PSXAPI.Response580073471.PREFIX_AGDFASBV1842323304.LootType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoneValue', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Money', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Gold', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Item', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Pokemon', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Clothe', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Hat', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Mount', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SurfMount', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FlyMount', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=88,
  serialized_end=218,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1842323304_LOOTTYPE)

_PREFIX_AGDFASBV1949913223_LOOTBOXACTION = _descriptor.EnumDescriptor(
  name='LootboxAction',
  full_name='PSXAPI.Response580073471.PREFIX_AGDFASBV1949913223.LootboxAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoneValue', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Opened', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Update', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=521,
  serialized_end=575,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1949913223_LOOTBOXACTION)

_PREFIX_AGDFASBV1416211215_LOOTBOXTYPE = _descriptor.EnumDescriptor(
  name='LootboxType',
  full_name='PSXAPI.Response580073471.PREFIX_AGDFASBV1416211215.LootboxType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoneValue', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Small', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Normal', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=808,
  serialized_end=859,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1416211215_LOOTBOXTYPE)


_PREFIX_AGDFASBV1842323304 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1842323304',
  full_name='PSXAPI.Response580073471.PREFIX_AGDFASBV1842323304',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1842323304_LOOTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=218,
)


_LOOTBOX = _descriptor.Descriptor(
  name='Lootbox',
  full_name='PSXAPI.Response580073471.Lootbox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Action', full_name='PSXAPI.Response580073471.Lootbox.Action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Type', full_name='PSXAPI.Response580073471.Lootbox.Type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Remaining', full_name='PSXAPI.Response580073471.Lootbox.Remaining', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Rolls', full_name='PSXAPI.Response580073471.Lootbox.Rolls', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=221,
  serialized_end=490,
)


_PREFIX_AGDFASBV1949913223 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1949913223',
  full_name='PSXAPI.Response580073471.PREFIX_AGDFASBV1949913223',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1949913223_LOOTBOXACTION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=492,
  serialized_end=575,
)


_LOOTBOXROLL = _descriptor.Descriptor(
  name='LootboxRoll',
  full_name='PSXAPI.Response580073471.LootboxRoll',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='LootType', full_name='PSXAPI.Response580073471.LootboxRoll.LootType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Num', full_name='PSXAPI.Response580073471.LootboxRoll.Num', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Duplicate', full_name='PSXAPI.Response580073471.LootboxRoll.Duplicate', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DuplicateGold', full_name='PSXAPI.Response580073471.LootboxRoll.DuplicateGold', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DuplicateMoney', full_name='PSXAPI.Response580073471.LootboxRoll.DuplicateMoney', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=578,
  serialized_end=777,
)


_PREFIX_AGDFASBV1416211215 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1416211215',
  full_name='PSXAPI.Response580073471.PREFIX_AGDFASBV1416211215',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1416211215_LOOTBOXTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=779,
  serialized_end=859,
)

_PREFIX_AGDFASBV1842323304_LOOTTYPE.containing_type = _PREFIX_AGDFASBV1842323304
_LOOTBOX.fields_by_name['Action'].enum_type = _PREFIX_AGDFASBV1949913223_LOOTBOXACTION
_LOOTBOX.fields_by_name['Type'].enum_type = _PREFIX_AGDFASBV1416211215_LOOTBOXTYPE
_LOOTBOX.fields_by_name['Rolls'].message_type = _LOOTBOXROLL
_PREFIX_AGDFASBV1949913223_LOOTBOXACTION.containing_type = _PREFIX_AGDFASBV1949913223
_LOOTBOXROLL.fields_by_name['LootType'].enum_type = _PREFIX_AGDFASBV1842323304_LOOTTYPE
_PREFIX_AGDFASBV1416211215_LOOTBOXTYPE.containing_type = _PREFIX_AGDFASBV1416211215
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1842323304'] = _PREFIX_AGDFASBV1842323304
DESCRIPTOR.message_types_by_name['Lootbox'] = _LOOTBOX
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1949913223'] = _PREFIX_AGDFASBV1949913223
DESCRIPTOR.message_types_by_name['LootboxRoll'] = _LOOTBOXROLL
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1416211215'] = _PREFIX_AGDFASBV1416211215

PREFIX_AGDFASBV1842323304 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1842323304', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1842323304,
  __module__ = 'game.response.Lootbox_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response580073471.PREFIX_AGDFASBV1842323304)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1842323304)

Lootbox = _reflection.GeneratedProtocolMessageType('Lootbox', (_message.Message,), dict(
  DESCRIPTOR = _LOOTBOX,
  __module__ = 'game.response.Lootbox_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response580073471.Lootbox)
  ))
_sym_db.RegisterMessage(Lootbox)

PREFIX_AGDFASBV1949913223 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1949913223', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1949913223,
  __module__ = 'game.response.Lootbox_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response580073471.PREFIX_AGDFASBV1949913223)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1949913223)

LootboxRoll = _reflection.GeneratedProtocolMessageType('LootboxRoll', (_message.Message,), dict(
  DESCRIPTOR = _LOOTBOXROLL,
  __module__ = 'game.response.Lootbox_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response580073471.LootboxRoll)
  ))
_sym_db.RegisterMessage(LootboxRoll)

PREFIX_AGDFASBV1416211215 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1416211215', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1416211215,
  __module__ = 'game.response.Lootbox_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response580073471.PREFIX_AGDFASBV1416211215)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1416211215)


# @@protoc_insertion_point(module_scope)
