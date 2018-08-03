# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game/response/Achievements.proto

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
  name='game/response/Achievements.proto',
  package='PSXAPI.Response807491418',
  syntax='proto2',
  serialized_pb=_b('\n game/response/Achievements.proto\x12\x18PSXAPI.Response807491418\"f\n\x0b\x41\x63hievement\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x13\n\x08Progress\x18\x02 \x01(\r:\x01\x30\x12\x36\n\x07Payload\x18\x03 \x03(\x0b\x32%.PSXAPI.Response807491418.Achievement\"h\n\x0c\x41\x63hievements\x12\x10\n\x08Username\x18\x01 \x01(\t\x12\x11\n\x06Points\x18\x02 \x01(\r:\x01\x30\x12\x33\n\x04List\x18\x03 \x03(\x0b\x32%.PSXAPI.Response807491418.Achievement')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ACHIEVEMENT = _descriptor.Descriptor(
  name='Achievement',
  full_name='PSXAPI.Response807491418.Achievement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='PSXAPI.Response807491418.Achievement.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Progress', full_name='PSXAPI.Response807491418.Achievement.Progress', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Payload', full_name='PSXAPI.Response807491418.Achievement.Payload', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=62,
  serialized_end=164,
)


_ACHIEVEMENTS = _descriptor.Descriptor(
  name='Achievements',
  full_name='PSXAPI.Response807491418.Achievements',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Username', full_name='PSXAPI.Response807491418.Achievements.Username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Points', full_name='PSXAPI.Response807491418.Achievements.Points', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='List', full_name='PSXAPI.Response807491418.Achievements.List', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=166,
  serialized_end=270,
)

_ACHIEVEMENT.fields_by_name['Payload'].message_type = _ACHIEVEMENT
_ACHIEVEMENTS.fields_by_name['List'].message_type = _ACHIEVEMENT
DESCRIPTOR.message_types_by_name['Achievement'] = _ACHIEVEMENT
DESCRIPTOR.message_types_by_name['Achievements'] = _ACHIEVEMENTS

Achievement = _reflection.GeneratedProtocolMessageType('Achievement', (_message.Message,), dict(
  DESCRIPTOR = _ACHIEVEMENT,
  __module__ = 'game.response.Achievements_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response807491418.Achievement)
  ))
_sym_db.RegisterMessage(Achievement)

Achievements = _reflection.GeneratedProtocolMessageType('Achievements', (_message.Message,), dict(
  DESCRIPTOR = _ACHIEVEMENTS,
  __module__ = 'game.response.Achievements_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response807491418.Achievements)
  ))
_sym_db.RegisterMessage(Achievements)


# @@protoc_insertion_point(module_scope)
