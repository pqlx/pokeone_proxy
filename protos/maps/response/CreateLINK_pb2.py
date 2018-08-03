# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: maps/response/CreateLINK.proto

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
  name='maps/response/CreateLINK.proto',
  package='MAPAPI.Response1817839937',
  syntax='proto2',
  serialized_pb=_b('\n\x1emaps/response/CreateLINK.proto\x12\x19MAPAPI.Response1817839937\x1a\tbcl.proto\"`\n\nCreateLINK\x12\x16\n\x07\x44\x65stroy\x18\x01 \x01(\x08:\x05\x66\x61lse\x12:\n\x06Object\x18\x02 \x01(\x0b\x32*.MAPAPI.Response1817839937.NPCObjectStruct\"R\n\x0fNPCObjectStruct\x12\x0c\n\x01x\x18\x01 \x01(\x05:\x01\x30\x12\x0c\n\x01y\x18\x02 \x01(\x05:\x01\x30\x12\x0c\n\x01z\x18\x03 \x01(\x05:\x01\x30\x12\x15\n\x02ID\x18\x04 \x01(\x0b\x32\t.bcl.Guid')
  ,
  dependencies=[bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CREATELINK = _descriptor.Descriptor(
  name='CreateLINK',
  full_name='MAPAPI.Response1817839937.CreateLINK',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Destroy', full_name='MAPAPI.Response1817839937.CreateLINK.Destroy', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Object', full_name='MAPAPI.Response1817839937.CreateLINK.Object', index=1,
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
  serialized_start=72,
  serialized_end=168,
)


_NPCOBJECTSTRUCT = _descriptor.Descriptor(
  name='NPCObjectStruct',
  full_name='MAPAPI.Response1817839937.NPCObjectStruct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='MAPAPI.Response1817839937.NPCObjectStruct.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='MAPAPI.Response1817839937.NPCObjectStruct.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='MAPAPI.Response1817839937.NPCObjectStruct.z', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ID', full_name='MAPAPI.Response1817839937.NPCObjectStruct.ID', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=170,
  serialized_end=252,
)

_CREATELINK.fields_by_name['Object'].message_type = _NPCOBJECTSTRUCT
_NPCOBJECTSTRUCT.fields_by_name['ID'].message_type = bcl__pb2._GUID
DESCRIPTOR.message_types_by_name['CreateLINK'] = _CREATELINK
DESCRIPTOR.message_types_by_name['NPCObjectStruct'] = _NPCOBJECTSTRUCT

CreateLINK = _reflection.GeneratedProtocolMessageType('CreateLINK', (_message.Message,), dict(
  DESCRIPTOR = _CREATELINK,
  __module__ = 'maps.response.CreateLINK_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response1817839937.CreateLINK)
  ))
_sym_db.RegisterMessage(CreateLINK)

NPCObjectStruct = _reflection.GeneratedProtocolMessageType('NPCObjectStruct', (_message.Message,), dict(
  DESCRIPTOR = _NPCOBJECTSTRUCT,
  __module__ = 'maps.response.CreateLINK_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response1817839937.NPCObjectStruct)
  ))
_sym_db.RegisterMessage(NPCObjectStruct)


# @@protoc_insertion_point(module_scope)
