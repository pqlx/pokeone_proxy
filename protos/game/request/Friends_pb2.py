# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Friends.proto

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
  name='Friends.proto',
  package='PSXAPI.Request23',
  syntax='proto2',
  serialized_pb=_b('\n\rFriends.proto\x12\x10PSXAPI.Request23\"H\n\x07\x46riends\x12/\n\x06\x41\x63tion\x18\x01 \x02(\x0e\x32\x1f.PSXAPI.Request23.FriendsAction\x12\x0c\n\x04\x44\x61ta\x18\x02 \x01(\t*D\n\rFriendsAction\x12\x0e\n\nRequestAll\x10\x00\x12\x07\n\x03\x41\x64\x64\x10\x01\x12\n\n\x06Remove\x10\x02\x12\x0e\n\nSetMessage\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_FRIENDSACTION = _descriptor.EnumDescriptor(
  name='FriendsAction',
  full_name='PSXAPI.Request23.FriendsAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RequestAll', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Add', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Remove', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetMessage', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=109,
  serialized_end=177,
)
_sym_db.RegisterEnumDescriptor(_FRIENDSACTION)

FriendsAction = enum_type_wrapper.EnumTypeWrapper(_FRIENDSACTION)
RequestAll = 0
Add = 1
Remove = 2
SetMessage = 3



_FRIENDS = _descriptor.Descriptor(
  name='Friends',
  full_name='PSXAPI.Request23.Friends',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Action', full_name='PSXAPI.Request23.Friends.Action', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data', full_name='PSXAPI.Request23.Friends.Data', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=35,
  serialized_end=107,
)

_FRIENDS.fields_by_name['Action'].enum_type = _FRIENDSACTION
DESCRIPTOR.message_types_by_name['Friends'] = _FRIENDS
DESCRIPTOR.enum_types_by_name['FriendsAction'] = _FRIENDSACTION

Friends = _reflection.GeneratedProtocolMessageType('Friends', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDS,
  __module__ = 'Friends_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request23.Friends)
  ))
_sym_db.RegisterMessage(Friends)


# @@protoc_insertion_point(module_scope)
