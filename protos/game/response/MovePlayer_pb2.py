# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game/response/MovePlayer.proto

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
  name='game/response/MovePlayer.proto',
  package='PSXAPI.Response243615930',
  syntax='proto2',
  serialized_pb=_b('\n\x1egame/response/MovePlayer.proto\x12\x18PSXAPI.Response243615930\"*\n\x05\x45quip\x12\x11\n\x06\x43lothe\x18\x01 \x01(\x05:\x01\x30\x12\x0e\n\x03Hat\x18\x02 \x01(\x05:\x01\x30\";\n\x19PREFIX_AGDFASBV1910591611\"\x1e\n\x06Gender\x12\x08\n\x04Male\x10\x00\x12\n\n\x06\x46\x65male\x10\x01\"D\n\x19PREFIX_AGDFASBV1033176750\"\'\n\nMemberRank\x12\r\n\tNoneValue\x10\x00\x12\n\n\x06Member\x10\x01\"w\n\x05Mount\x12\x12\n\x07MountID\x18\x01 \x01(\x05:\x01\x30\x12Z\n\tMountType\x18\x02 \x01(\x0e\x32<.PSXAPI.Response243615930.PREFIX_AGDFASBV686405618.MountType:\tNoneValue\"Z\n\x18PREFIX_AGDFASBV686405618\">\n\tMountType\x12\r\n\tNoneValue\x10\x00\x12\x0b\n\x07Surfing\x10\x01\x12\x08\n\x04\x42ike\x10\x02\x12\x0b\n\x07Pokemon\x10\x03\"\xa5\x06\n\nMovePlayer\x12\x0b\n\x03Map\x18\x01 \x02(\t\x12\x10\n\x08Username\x18\x02 \x02(\t\x12\t\n\x01X\x18\x03 \x02(\x05\x12\t\n\x01Y\x18\x04 \x02(\x05\x12Y\n\x06\x41\x63tion\x18\x05 \x01(\x0e\x32\x44.PSXAPI.Response243615930.PREFIX_AGDFASBV1418837558.MovePlayerAction:\x03Set\x12.\n\x05Style\x18\x06 \x01(\x0b\x32\x1f.PSXAPI.Response243615930.Style\x12_\n\tDirection\x18\x07 \x01(\x0e\x32\x43.PSXAPI.Response243615930.PREFIX_AGDFASBV1103073431.PlayerDirection:\x07\x44\x65\x66\x61ult\x12.\n\x05\x45quip\x18\x08 \x01(\x0b\x32\x1f.PSXAPI.Response243615930.Equip\x12.\n\x05Mount\x18\t \x01(\x0b\x32\x1f.PSXAPI.Response243615930.Mount\x12\x13\n\x04\x41way\x18\n \x01(\x08:\x05\x66\x61lse\x12\x15\n\x06\x42\x61ttle\x18\x0b \x01(\x08:\x05\x66\x61lse\x12]\n\nMemberRank\x18\x0c \x01(\x0e\x32>.PSXAPI.Response243615930.PREFIX_AGDFASBV1033176750.MemberRank:\tNoneValue\x12[\n\tStaffRank\x18\r \x01(\x0e\x32=.PSXAPI.Response243615930.PREFIX_AGDFASBV1867716523.StaffRank:\tNoneValue\x12\x11\n\tGuildName\x18\x0e \x01(\t\x12\x13\n\x08\x45mblemId\x18\x0f \x01(\r:\x01\x30\x12\x10\n\x05Level\x18\x10 \x01(\r:\x01\x30\x12\x11\n\x06\x46ollow\x18\x11 \x01(\x05:\x01\x30\x12\x11\n\x06Height\x18\x12 \x01(\x05:\x01\x30\x12\x1c\n\x11\x46ollowPersonality\x18\x13 \x01(\x05:\x01\x30\x12\x14\n\x05Lobby\x18\x14 \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x0b\x46ollowShiny\x18\x15 \x01(\x08:\x05\x66\x61lse\"\x82\x01\n\x19PREFIX_AGDFASBV1418837558\"e\n\x10MovePlayerAction\x12\x07\n\x03Set\x10\x00\x12\x06\n\x02Up\x10\x01\x12\x08\n\x04\x44own\x10\x02\x12\x08\n\x04Left\x10\x03\x12\t\n\x05Right\x10\x04\x12\t\n\x05\x45nter\x10\x05\x12\t\n\x05Leave\x10\x06\x12\x0b\n\x07\x46ishing\x10\x07\"b\n\x19PREFIX_AGDFASBV1103073431\"E\n\x0fPlayerDirection\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\x06\n\x02Up\x10\x01\x12\x08\n\x04\x44own\x10\x02\x12\x08\n\x04Left\x10\x03\x12\t\n\x05Right\x10\x04\"h\n\x19PREFIX_AGDFASBV1867716523\"K\n\tStaffRank\x12\r\n\tNoneValue\x10\x00\x12\r\n\tDeveloper\x10\x01\x12\x11\n\rGameModerator\x10\x02\x12\r\n\tModerator\x10\x03\"\xa2\x01\n\x05Style\x12P\n\x06Gender\x18\x01 \x01(\x0e\x32:.PSXAPI.Response243615930.PREFIX_AGDFASBV1910591611.Gender:\x04Male\x12\x0f\n\x04Skin\x18\x02 \x01(\x05:\x01\x30\x12\x0f\n\x04\x45yes\x18\x03 \x01(\x05:\x01\x30\x12\x0f\n\x04Hair\x18\x04 \x01(\x05:\x01\x30\x12\x14\n\tHairColor\x18\x05 \x01(\x05:\x01\x30')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PREFIX_AGDFASBV1910591611_GENDER = _descriptor.EnumDescriptor(
  name='Gender',
  full_name='PSXAPI.Response243615930.PREFIX_AGDFASBV1910591611.Gender',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Male', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Female', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=133,
  serialized_end=163,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1910591611_GENDER)

_PREFIX_AGDFASBV1033176750_MEMBERRANK = _descriptor.EnumDescriptor(
  name='MemberRank',
  full_name='PSXAPI.Response243615930.PREFIX_AGDFASBV1033176750.MemberRank',
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
  serialized_start=194,
  serialized_end=233,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1033176750_MEMBERRANK)

_PREFIX_AGDFASBV686405618_MOUNTTYPE = _descriptor.EnumDescriptor(
  name='MountType',
  full_name='PSXAPI.Response243615930.PREFIX_AGDFASBV686405618.MountType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NoneValue', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Surfing', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Bike', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Pokemon', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=384,
  serialized_end=446,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV686405618_MOUNTTYPE)

_PREFIX_AGDFASBV1418837558_MOVEPLAYERACTION = _descriptor.EnumDescriptor(
  name='MovePlayerAction',
  full_name='PSXAPI.Response243615930.PREFIX_AGDFASBV1418837558.MovePlayerAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Set', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Up', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Down', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Left', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Right', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Enter', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Leave', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Fishing', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1286,
  serialized_end=1387,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1418837558_MOVEPLAYERACTION)

_PREFIX_AGDFASBV1103073431_PLAYERDIRECTION = _descriptor.EnumDescriptor(
  name='PlayerDirection',
  full_name='PSXAPI.Response243615930.PREFIX_AGDFASBV1103073431.PlayerDirection',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Default', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Up', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Down', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Left', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Right', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1418,
  serialized_end=1487,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1103073431_PLAYERDIRECTION)

_PREFIX_AGDFASBV1867716523_STAFFRANK = _descriptor.EnumDescriptor(
  name='StaffRank',
  full_name='PSXAPI.Response243615930.PREFIX_AGDFASBV1867716523.StaffRank',
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
  serialized_start=1518,
  serialized_end=1593,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1867716523_STAFFRANK)


_EQUIP = _descriptor.Descriptor(
  name='Equip',
  full_name='PSXAPI.Response243615930.Equip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Clothe', full_name='PSXAPI.Response243615930.Equip.Clothe', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Hat', full_name='PSXAPI.Response243615930.Equip.Hat', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=60,
  serialized_end=102,
)


_PREFIX_AGDFASBV1910591611 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1910591611',
  full_name='PSXAPI.Response243615930.PREFIX_AGDFASBV1910591611',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1910591611_GENDER,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=163,
)


_PREFIX_AGDFASBV1033176750 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1033176750',
  full_name='PSXAPI.Response243615930.PREFIX_AGDFASBV1033176750',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1033176750_MEMBERRANK,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=233,
)


_MOUNT = _descriptor.Descriptor(
  name='Mount',
  full_name='PSXAPI.Response243615930.Mount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MountID', full_name='PSXAPI.Response243615930.Mount.MountID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MountType', full_name='PSXAPI.Response243615930.Mount.MountType', index=1,
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
  serialized_start=235,
  serialized_end=354,
)


_PREFIX_AGDFASBV686405618 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV686405618',
  full_name='PSXAPI.Response243615930.PREFIX_AGDFASBV686405618',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV686405618_MOUNTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=356,
  serialized_end=446,
)


_MOVEPLAYER = _descriptor.Descriptor(
  name='MovePlayer',
  full_name='PSXAPI.Response243615930.MovePlayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Map', full_name='PSXAPI.Response243615930.MovePlayer.Map', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Username', full_name='PSXAPI.Response243615930.MovePlayer.Username', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='X', full_name='PSXAPI.Response243615930.MovePlayer.X', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Y', full_name='PSXAPI.Response243615930.MovePlayer.Y', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Action', full_name='PSXAPI.Response243615930.MovePlayer.Action', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Style', full_name='PSXAPI.Response243615930.MovePlayer.Style', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Direction', full_name='PSXAPI.Response243615930.MovePlayer.Direction', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Equip', full_name='PSXAPI.Response243615930.MovePlayer.Equip', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Mount', full_name='PSXAPI.Response243615930.MovePlayer.Mount', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Away', full_name='PSXAPI.Response243615930.MovePlayer.Away', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Battle', full_name='PSXAPI.Response243615930.MovePlayer.Battle', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MemberRank', full_name='PSXAPI.Response243615930.MovePlayer.MemberRank', index=11,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StaffRank', full_name='PSXAPI.Response243615930.MovePlayer.StaffRank', index=12,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GuildName', full_name='PSXAPI.Response243615930.MovePlayer.GuildName', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EmblemId', full_name='PSXAPI.Response243615930.MovePlayer.EmblemId', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Level', full_name='PSXAPI.Response243615930.MovePlayer.Level', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Follow', full_name='PSXAPI.Response243615930.MovePlayer.Follow', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Height', full_name='PSXAPI.Response243615930.MovePlayer.Height', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FollowPersonality', full_name='PSXAPI.Response243615930.MovePlayer.FollowPersonality', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Lobby', full_name='PSXAPI.Response243615930.MovePlayer.Lobby', index=19,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FollowShiny', full_name='PSXAPI.Response243615930.MovePlayer.FollowShiny', index=20,
      number=21, type=8, cpp_type=7, label=1,
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
  serialized_start=449,
  serialized_end=1254,
)


_PREFIX_AGDFASBV1418837558 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1418837558',
  full_name='PSXAPI.Response243615930.PREFIX_AGDFASBV1418837558',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1418837558_MOVEPLAYERACTION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1257,
  serialized_end=1387,
)


_PREFIX_AGDFASBV1103073431 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1103073431',
  full_name='PSXAPI.Response243615930.PREFIX_AGDFASBV1103073431',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1103073431_PLAYERDIRECTION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1389,
  serialized_end=1487,
)


_PREFIX_AGDFASBV1867716523 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1867716523',
  full_name='PSXAPI.Response243615930.PREFIX_AGDFASBV1867716523',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1867716523_STAFFRANK,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1489,
  serialized_end=1593,
)


_STYLE = _descriptor.Descriptor(
  name='Style',
  full_name='PSXAPI.Response243615930.Style',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Gender', full_name='PSXAPI.Response243615930.Style.Gender', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Skin', full_name='PSXAPI.Response243615930.Style.Skin', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Eyes', full_name='PSXAPI.Response243615930.Style.Eyes', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Hair', full_name='PSXAPI.Response243615930.Style.Hair', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HairColor', full_name='PSXAPI.Response243615930.Style.HairColor', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=1596,
  serialized_end=1758,
)

_PREFIX_AGDFASBV1910591611_GENDER.containing_type = _PREFIX_AGDFASBV1910591611
_PREFIX_AGDFASBV1033176750_MEMBERRANK.containing_type = _PREFIX_AGDFASBV1033176750
_MOUNT.fields_by_name['MountType'].enum_type = _PREFIX_AGDFASBV686405618_MOUNTTYPE
_PREFIX_AGDFASBV686405618_MOUNTTYPE.containing_type = _PREFIX_AGDFASBV686405618
_MOVEPLAYER.fields_by_name['Action'].enum_type = _PREFIX_AGDFASBV1418837558_MOVEPLAYERACTION
_MOVEPLAYER.fields_by_name['Style'].message_type = _STYLE
_MOVEPLAYER.fields_by_name['Direction'].enum_type = _PREFIX_AGDFASBV1103073431_PLAYERDIRECTION
_MOVEPLAYER.fields_by_name['Equip'].message_type = _EQUIP
_MOVEPLAYER.fields_by_name['Mount'].message_type = _MOUNT
_MOVEPLAYER.fields_by_name['MemberRank'].enum_type = _PREFIX_AGDFASBV1033176750_MEMBERRANK
_MOVEPLAYER.fields_by_name['StaffRank'].enum_type = _PREFIX_AGDFASBV1867716523_STAFFRANK
_PREFIX_AGDFASBV1418837558_MOVEPLAYERACTION.containing_type = _PREFIX_AGDFASBV1418837558
_PREFIX_AGDFASBV1103073431_PLAYERDIRECTION.containing_type = _PREFIX_AGDFASBV1103073431
_PREFIX_AGDFASBV1867716523_STAFFRANK.containing_type = _PREFIX_AGDFASBV1867716523
_STYLE.fields_by_name['Gender'].enum_type = _PREFIX_AGDFASBV1910591611_GENDER
DESCRIPTOR.message_types_by_name['Equip'] = _EQUIP
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1910591611'] = _PREFIX_AGDFASBV1910591611
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1033176750'] = _PREFIX_AGDFASBV1033176750
DESCRIPTOR.message_types_by_name['Mount'] = _MOUNT
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV686405618'] = _PREFIX_AGDFASBV686405618
DESCRIPTOR.message_types_by_name['MovePlayer'] = _MOVEPLAYER
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1418837558'] = _PREFIX_AGDFASBV1418837558
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1103073431'] = _PREFIX_AGDFASBV1103073431
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1867716523'] = _PREFIX_AGDFASBV1867716523
DESCRIPTOR.message_types_by_name['Style'] = _STYLE

Equip = _reflection.GeneratedProtocolMessageType('Equip', (_message.Message,), dict(
  DESCRIPTOR = _EQUIP,
  __module__ = 'game.response.MovePlayer_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response243615930.Equip)
  ))
_sym_db.RegisterMessage(Equip)

PREFIX_AGDFASBV1910591611 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1910591611', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1910591611,
  __module__ = 'game.response.MovePlayer_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response243615930.PREFIX_AGDFASBV1910591611)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1910591611)

PREFIX_AGDFASBV1033176750 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1033176750', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1033176750,
  __module__ = 'game.response.MovePlayer_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response243615930.PREFIX_AGDFASBV1033176750)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1033176750)

Mount = _reflection.GeneratedProtocolMessageType('Mount', (_message.Message,), dict(
  DESCRIPTOR = _MOUNT,
  __module__ = 'game.response.MovePlayer_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response243615930.Mount)
  ))
_sym_db.RegisterMessage(Mount)

PREFIX_AGDFASBV686405618 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV686405618', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV686405618,
  __module__ = 'game.response.MovePlayer_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response243615930.PREFIX_AGDFASBV686405618)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV686405618)

MovePlayer = _reflection.GeneratedProtocolMessageType('MovePlayer', (_message.Message,), dict(
  DESCRIPTOR = _MOVEPLAYER,
  __module__ = 'game.response.MovePlayer_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response243615930.MovePlayer)
  ))
_sym_db.RegisterMessage(MovePlayer)

PREFIX_AGDFASBV1418837558 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1418837558', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1418837558,
  __module__ = 'game.response.MovePlayer_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response243615930.PREFIX_AGDFASBV1418837558)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1418837558)

PREFIX_AGDFASBV1103073431 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1103073431', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1103073431,
  __module__ = 'game.response.MovePlayer_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response243615930.PREFIX_AGDFASBV1103073431)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1103073431)

PREFIX_AGDFASBV1867716523 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1867716523', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1867716523,
  __module__ = 'game.response.MovePlayer_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response243615930.PREFIX_AGDFASBV1867716523)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1867716523)

Style = _reflection.GeneratedProtocolMessageType('Style', (_message.Message,), dict(
  DESCRIPTOR = _STYLE,
  __module__ = 'game.response.MovePlayer_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response243615930.Style)
  ))
_sym_db.RegisterMessage(Style)


# @@protoc_insertion_point(module_scope)
