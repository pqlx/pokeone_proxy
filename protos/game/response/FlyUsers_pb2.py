# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game/response/FlyUsers.proto

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
  name='game/response/FlyUsers.proto',
  package='PSXAPI.Response1713709382',
  syntax='proto2',
  serialized_pb=_b('\n\x1cgame/response/FlyUsers.proto\x12\x19PSXAPI.Response1713709382\"\x90\x01\n\x07\x46lyUser\x12\x10\n\x08Username\x18\x01 \x01(\t\x12=\n\x07\x41\x63tions\x18\x02 \x03(\x0b\x32,.PSXAPI.Response1713709382.FlyUserActionData\x12\x34\n\x04\x44\x61ta\x18\x03 \x01(\x0b\x32&.PSXAPI.Response1713709382.FlyUserData\"U\n\x19PREFIX_AGDFASBV1230127827\"8\n\rFlyUserAction\x12\x07\n\x03Set\x10\x00\x12\x08\n\x04Move\x10\x01\x12\t\n\x05\x45nter\x10\x02\x12\t\n\x05Leave\x10\x03\"\xaa\x01\n\x11\x46lyUserActionData\x12W\n\x06\x41\x63tion\x18\x01 \x01(\x0e\x32\x42.PSXAPI.Response1713709382.PREFIX_AGDFASBV1230127827.FlyUserAction:\x03Set\x12<\n\x08Position\x18\x02 \x01(\x0b\x32*.PSXAPI.Response1713709382.FlyUserPosition\"\xdb\x02\n\x0b\x46lyUserData\x12\x13\n\x08\x46lyMount\x18\x01 \x01(\x05:\x01\x30\x12\x13\n\x04\x41way\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x15\n\x06\x42\x61ttle\x18\x03 \x01(\x08:\x05\x66\x61lse\x12]\n\nMemberRank\x18\x04 \x01(\x0e\x32>.PSXAPI.Response1713709382.PREFIX_AGDFASBV824238674.MemberRank:\tNoneValue\x12\\\n\tStaffRank\x18\x05 \x01(\x0e\x32>.PSXAPI.Response1713709382.PREFIX_AGDFASBV1756282689.StaffRank:\tNoneValue\x12\x11\n\tGuildName\x18\x06 \x01(\t\x12\x13\n\x08\x45mblemId\x18\x07 \x01(\r:\x01\x30\x12\x10\n\x05Level\x18\x08 \x01(\r:\x01\x30\x12\x14\n\x05Lobby\x18\t \x01(\x08:\x05\x66\x61lse\"\x88\x01\n\x0f\x46lyUserPosition\x12\x0f\n\x04PosX\x18\x01 \x01(\x02:\x01\x30\x12\x0f\n\x04PosY\x18\x02 \x01(\x02:\x01\x30\x12\x0f\n\x04PosZ\x18\x03 \x01(\x02:\x01\x30\x12\x0f\n\x04RotX\x18\x04 \x01(\x02:\x01\x30\x12\x0f\n\x04RotY\x18\x05 \x01(\x02:\x01\x30\x12\x0f\n\x04RotZ\x18\x06 \x01(\x02:\x01\x30\x12\x0f\n\x04RotW\x18\x07 \x01(\x02:\x01\x30\"=\n\x08\x46lyUsers\x12\x31\n\x05Users\x18\x01 \x03(\x0b\x32\".PSXAPI.Response1713709382.FlyUser\"C\n\x18PREFIX_AGDFASBV824238674\"\'\n\nMemberRank\x12\r\n\tNoneValue\x10\x00\x12\n\n\x06Member\x10\x01\"h\n\x19PREFIX_AGDFASBV1756282689\"K\n\tStaffRank\x12\r\n\tNoneValue\x10\x00\x12\r\n\tDeveloper\x10\x01\x12\x11\n\rGameModerator\x10\x02\x12\r\n\tModerator\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PREFIX_AGDFASBV1230127827_FLYUSERACTION = _descriptor.EnumDescriptor(
  name='FlyUserAction',
  full_name='PSXAPI.Response1713709382.PREFIX_AGDFASBV1230127827.FlyUserAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Set', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Move', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enter', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Leave', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=235,
  serialized_end=291,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1230127827_FLYUSERACTION)

_PREFIX_AGDFASBV824238674_MEMBERRANK = _descriptor.EnumDescriptor(
  name='MemberRank',
  full_name='PSXAPI.Response1713709382.PREFIX_AGDFASBV824238674.MemberRank',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoneValue', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Member', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1046,
  serialized_end=1085,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV824238674_MEMBERRANK)

_PREFIX_AGDFASBV1756282689_STAFFRANK = _descriptor.EnumDescriptor(
  name='StaffRank',
  full_name='PSXAPI.Response1713709382.PREFIX_AGDFASBV1756282689.StaffRank',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoneValue', index=0, number=0,
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
  serialized_start=1116,
  serialized_end=1191,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1756282689_STAFFRANK)


_FLYUSER = _descriptor.Descriptor(
  name='FlyUser',
  full_name='PSXAPI.Response1713709382.FlyUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Username', full_name='PSXAPI.Response1713709382.FlyUser.Username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Actions', full_name='PSXAPI.Response1713709382.FlyUser.Actions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data', full_name='PSXAPI.Response1713709382.FlyUser.Data', index=2,
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
  serialized_start=60,
  serialized_end=204,
)


_PREFIX_AGDFASBV1230127827 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1230127827',
  full_name='PSXAPI.Response1713709382.PREFIX_AGDFASBV1230127827',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1230127827_FLYUSERACTION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=291,
)


_FLYUSERACTIONDATA = _descriptor.Descriptor(
  name='FlyUserActionData',
  full_name='PSXAPI.Response1713709382.FlyUserActionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Action', full_name='PSXAPI.Response1713709382.FlyUserActionData.Action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Position', full_name='PSXAPI.Response1713709382.FlyUserActionData.Position', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=294,
  serialized_end=464,
)


_FLYUSERDATA = _descriptor.Descriptor(
  name='FlyUserData',
  full_name='PSXAPI.Response1713709382.FlyUserData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FlyMount', full_name='PSXAPI.Response1713709382.FlyUserData.FlyMount', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Away', full_name='PSXAPI.Response1713709382.FlyUserData.Away', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Battle', full_name='PSXAPI.Response1713709382.FlyUserData.Battle', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MemberRank', full_name='PSXAPI.Response1713709382.FlyUserData.MemberRank', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StaffRank', full_name='PSXAPI.Response1713709382.FlyUserData.StaffRank', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GuildName', full_name='PSXAPI.Response1713709382.FlyUserData.GuildName', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EmblemId', full_name='PSXAPI.Response1713709382.FlyUserData.EmblemId', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Level', full_name='PSXAPI.Response1713709382.FlyUserData.Level', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Lobby', full_name='PSXAPI.Response1713709382.FlyUserData.Lobby', index=8,
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
  serialized_start=467,
  serialized_end=814,
)


_FLYUSERPOSITION = _descriptor.Descriptor(
  name='FlyUserPosition',
  full_name='PSXAPI.Response1713709382.FlyUserPosition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PosX', full_name='PSXAPI.Response1713709382.FlyUserPosition.PosX', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PosY', full_name='PSXAPI.Response1713709382.FlyUserPosition.PosY', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PosZ', full_name='PSXAPI.Response1713709382.FlyUserPosition.PosZ', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RotX', full_name='PSXAPI.Response1713709382.FlyUserPosition.RotX', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RotY', full_name='PSXAPI.Response1713709382.FlyUserPosition.RotY', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RotZ', full_name='PSXAPI.Response1713709382.FlyUserPosition.RotZ', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RotW', full_name='PSXAPI.Response1713709382.FlyUserPosition.RotW', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
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
  serialized_start=817,
  serialized_end=953,
)


_FLYUSERS = _descriptor.Descriptor(
  name='FlyUsers',
  full_name='PSXAPI.Response1713709382.FlyUsers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Users', full_name='PSXAPI.Response1713709382.FlyUsers.Users', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=955,
  serialized_end=1016,
)


_PREFIX_AGDFASBV824238674 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV824238674',
  full_name='PSXAPI.Response1713709382.PREFIX_AGDFASBV824238674',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV824238674_MEMBERRANK,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1018,
  serialized_end=1085,
)


_PREFIX_AGDFASBV1756282689 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1756282689',
  full_name='PSXAPI.Response1713709382.PREFIX_AGDFASBV1756282689',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1756282689_STAFFRANK,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1087,
  serialized_end=1191,
)

_FLYUSER.fields_by_name['Actions'].message_type = _FLYUSERACTIONDATA
_FLYUSER.fields_by_name['Data'].message_type = _FLYUSERDATA
_PREFIX_AGDFASBV1230127827_FLYUSERACTION.containing_type = _PREFIX_AGDFASBV1230127827
_FLYUSERACTIONDATA.fields_by_name['Action'].enum_type = _PREFIX_AGDFASBV1230127827_FLYUSERACTION
_FLYUSERACTIONDATA.fields_by_name['Position'].message_type = _FLYUSERPOSITION
_FLYUSERDATA.fields_by_name['MemberRank'].enum_type = _PREFIX_AGDFASBV824238674_MEMBERRANK
_FLYUSERDATA.fields_by_name['StaffRank'].enum_type = _PREFIX_AGDFASBV1756282689_STAFFRANK
_FLYUSERS.fields_by_name['Users'].message_type = _FLYUSER
_PREFIX_AGDFASBV824238674_MEMBERRANK.containing_type = _PREFIX_AGDFASBV824238674
_PREFIX_AGDFASBV1756282689_STAFFRANK.containing_type = _PREFIX_AGDFASBV1756282689
DESCRIPTOR.message_types_by_name['FlyUser'] = _FLYUSER
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1230127827'] = _PREFIX_AGDFASBV1230127827
DESCRIPTOR.message_types_by_name['FlyUserActionData'] = _FLYUSERACTIONDATA
DESCRIPTOR.message_types_by_name['FlyUserData'] = _FLYUSERDATA
DESCRIPTOR.message_types_by_name['FlyUserPosition'] = _FLYUSERPOSITION
DESCRIPTOR.message_types_by_name['FlyUsers'] = _FLYUSERS
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV824238674'] = _PREFIX_AGDFASBV824238674
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1756282689'] = _PREFIX_AGDFASBV1756282689

FlyUser = _reflection.GeneratedProtocolMessageType('FlyUser', (_message.Message,), dict(
  DESCRIPTOR = _FLYUSER,
  __module__ = 'game.response.FlyUsers_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1713709382.FlyUser)
  ))
_sym_db.RegisterMessage(FlyUser)

PREFIX_AGDFASBV1230127827 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1230127827', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1230127827,
  __module__ = 'game.response.FlyUsers_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1713709382.PREFIX_AGDFASBV1230127827)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1230127827)

FlyUserActionData = _reflection.GeneratedProtocolMessageType('FlyUserActionData', (_message.Message,), dict(
  DESCRIPTOR = _FLYUSERACTIONDATA,
  __module__ = 'game.response.FlyUsers_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1713709382.FlyUserActionData)
  ))
_sym_db.RegisterMessage(FlyUserActionData)

FlyUserData = _reflection.GeneratedProtocolMessageType('FlyUserData', (_message.Message,), dict(
  DESCRIPTOR = _FLYUSERDATA,
  __module__ = 'game.response.FlyUsers_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1713709382.FlyUserData)
  ))
_sym_db.RegisterMessage(FlyUserData)

FlyUserPosition = _reflection.GeneratedProtocolMessageType('FlyUserPosition', (_message.Message,), dict(
  DESCRIPTOR = _FLYUSERPOSITION,
  __module__ = 'game.response.FlyUsers_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1713709382.FlyUserPosition)
  ))
_sym_db.RegisterMessage(FlyUserPosition)

FlyUsers = _reflection.GeneratedProtocolMessageType('FlyUsers', (_message.Message,), dict(
  DESCRIPTOR = _FLYUSERS,
  __module__ = 'game.response.FlyUsers_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1713709382.FlyUsers)
  ))
_sym_db.RegisterMessage(FlyUsers)

PREFIX_AGDFASBV824238674 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV824238674', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV824238674,
  __module__ = 'game.response.FlyUsers_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1713709382.PREFIX_AGDFASBV824238674)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV824238674)

PREFIX_AGDFASBV1756282689 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1756282689', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1756282689,
  __module__ = 'game.response.FlyUsers_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response1713709382.PREFIX_AGDFASBV1756282689)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1756282689)


# @@protoc_insertion_point(module_scope)
