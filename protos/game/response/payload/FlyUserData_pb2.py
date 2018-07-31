# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FlyUserData.proto

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
  name='FlyUserData.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x11\x46lyUserData.proto\"\xf0\x01\n\x0b\x46lyUserData\x12\x13\n\x08\x46lyMount\x18\x01 \x01(\x05:\x01\x30\x12\x13\n\x04\x41way\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x15\n\x06\x42\x61ttle\x18\x03 \x01(\x08:\x05\x66\x61lse\x12(\n\nMemberRank\x18\x04 \x01(\x0e\x32\x0b.MemberRank:\x07__None0\x12&\n\tStaffRank\x18\x05 \x01(\x0e\x32\n.StaffRank:\x07__None1\x12\x11\n\tGuildName\x18\x06 \x01(\t\x12\x13\n\x08\x45mblemId\x18\x07 \x01(\r:\x01\x30\x12\x10\n\x05Level\x18\x08 \x01(\r:\x01\x30\x12\x14\n\x05Lobby\x18\t \x01(\x08:\x05\x66\x61lse*%\n\nMemberRank\x12\x0b\n\x07__None0\x10\x00\x12\n\n\x06Member\x10\x01*I\n\tStaffRank\x12\x0b\n\x07__None1\x10\x00\x12\r\n\tDeveloper\x10\x01\x12\x11\n\rGameModerator\x10\x02\x12\r\n\tModerator\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MEMBERRANK = _descriptor.EnumDescriptor(
  name='MemberRank',
  full_name='MemberRank',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='__None0', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Member', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=264,
  serialized_end=301,
)
_sym_db.RegisterEnumDescriptor(_MEMBERRANK)

MemberRank = enum_type_wrapper.EnumTypeWrapper(_MEMBERRANK)
_STAFFRANK = _descriptor.EnumDescriptor(
  name='StaffRank',
  full_name='StaffRank',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='__None1', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Developer', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GameModerator', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Moderator', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=303,
  serialized_end=376,
)
_sym_db.RegisterEnumDescriptor(_STAFFRANK)

StaffRank = enum_type_wrapper.EnumTypeWrapper(_STAFFRANK)
__None0 = 0
Member = 1
__None1 = 0
Developer = 1
GameModerator = 2
Moderator = 3



_FLYUSERDATA = _descriptor.Descriptor(
  name='FlyUserData',
  full_name='FlyUserData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FlyMount', full_name='FlyUserData.FlyMount', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Away', full_name='FlyUserData.Away', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Battle', full_name='FlyUserData.Battle', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MemberRank', full_name='FlyUserData.MemberRank', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StaffRank', full_name='FlyUserData.StaffRank', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GuildName', full_name='FlyUserData.GuildName', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EmblemId', full_name='FlyUserData.EmblemId', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Level', full_name='FlyUserData.Level', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Lobby', full_name='FlyUserData.Lobby', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=22,
  serialized_end=262,
)

_FLYUSERDATA.fields_by_name['MemberRank'].enum_type = _MEMBERRANK
_FLYUSERDATA.fields_by_name['StaffRank'].enum_type = _STAFFRANK
DESCRIPTOR.message_types_by_name['FlyUserData'] = _FLYUSERDATA
DESCRIPTOR.enum_types_by_name['MemberRank'] = _MEMBERRANK
DESCRIPTOR.enum_types_by_name['StaffRank'] = _STAFFRANK

FlyUserData = _reflection.GeneratedProtocolMessageType('FlyUserData', (_message.Message,), dict(
  DESCRIPTOR = _FLYUSERDATA,
  __module__ = 'FlyUserData_pb2'
  # @@protoc_insertion_point(class_scope:FlyUserData)
  ))
_sym_db.RegisterMessage(FlyUserData)


# @@protoc_insertion_point(module_scope)
