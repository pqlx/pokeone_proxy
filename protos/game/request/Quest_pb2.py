# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Quest.proto

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
  name='Quest.proto',
  package='PSXAPI.Request52',
  syntax='proto2',
  serialized_pb=_b('\n\x0bQuest.proto\x12\x10PSXAPI.Request52\"J\n\x05Quest\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x35\n\x06\x41\x63tion\x18\x02 \x01(\x0e\x32\x1d.PSXAPI.Request52.QuestAction:\x06__None*>\n\x0bQuestAction\x12\n\n\x06__None\x10\x00\x12\x0c\n\x08\x43omplete\x10\x01\x12\n\n\x06\x43\x61ncel\x10\x02\x12\t\n\x05Share\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_QUESTACTION = _descriptor.EnumDescriptor(
  name='QuestAction',
  full_name='PSXAPI.Request52.QuestAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='__None', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Complete', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Cancel', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Share', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=109,
  serialized_end=171,
)
_sym_db.RegisterEnumDescriptor(_QUESTACTION)

QuestAction = enum_type_wrapper.EnumTypeWrapper(_QUESTACTION)
__None = 0
Complete = 1
Cancel = 2
Share = 3



_QUEST = _descriptor.Descriptor(
  name='Quest',
  full_name='PSXAPI.Request52.Quest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='PSXAPI.Request52.Quest.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Action', full_name='PSXAPI.Request52.Quest.Action', index=1,
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
  serialized_start=33,
  serialized_end=107,
)

_QUEST.fields_by_name['Action'].enum_type = _QUESTACTION
DESCRIPTOR.message_types_by_name['Quest'] = _QUEST
DESCRIPTOR.enum_types_by_name['QuestAction'] = _QUESTACTION

Quest = _reflection.GeneratedProtocolMessageType('Quest', (_message.Message,), dict(
  DESCRIPTOR = _QUEST,
  __module__ = 'Quest_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request52.Quest)
  ))
_sym_db.RegisterMessage(Quest)


# @@protoc_insertion_point(module_scope)
