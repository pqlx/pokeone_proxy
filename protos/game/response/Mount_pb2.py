# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game/response/Mount.proto

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
  name='game/response/Mount.proto',
  package='PSXAPI.Response501659261',
  syntax='proto2',
  serialized_pb=_b('\n\x19game/response/Mount.proto\x12\x18PSXAPI.Response501659261\"x\n\x05Mount\x12\x12\n\x07MountID\x18\x01 \x01(\x05:\x01\x30\x12[\n\tMountType\x18\x02 \x01(\x0e\x32=.PSXAPI.Response501659261.PREFIX_AGDFASBV1238358761.MountType:\tNoneValue\"[\n\x19PREFIX_AGDFASBV1238358761\">\n\tMountType\x12\r\n\tNoneValue\x10\x00\x12\x0b\n\x07Surfing\x10\x01\x12\x08\n\x04\x42ike\x10\x02\x12\x0b\n\x07Pokemon\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PREFIX_AGDFASBV1238358761_MOUNTTYPE = _descriptor.EnumDescriptor(
  name='MountType',
  full_name='PSXAPI.Response501659261.PREFIX_AGDFASBV1238358761.MountType',
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
  serialized_start=206,
  serialized_end=268,
)
_sym_db.RegisterEnumDescriptor(_PREFIX_AGDFASBV1238358761_MOUNTTYPE)


_MOUNT = _descriptor.Descriptor(
  name='Mount',
  full_name='PSXAPI.Response501659261.Mount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MountID', full_name='PSXAPI.Response501659261.Mount.MountID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MountType', full_name='PSXAPI.Response501659261.Mount.MountType', index=1,
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
  serialized_start=55,
  serialized_end=175,
)


_PREFIX_AGDFASBV1238358761 = _descriptor.Descriptor(
  name='PREFIX_AGDFASBV1238358761',
  full_name='PSXAPI.Response501659261.PREFIX_AGDFASBV1238358761',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PREFIX_AGDFASBV1238358761_MOUNTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=268,
)

_MOUNT.fields_by_name['MountType'].enum_type = _PREFIX_AGDFASBV1238358761_MOUNTTYPE
_PREFIX_AGDFASBV1238358761_MOUNTTYPE.containing_type = _PREFIX_AGDFASBV1238358761
DESCRIPTOR.message_types_by_name['Mount'] = _MOUNT
DESCRIPTOR.message_types_by_name['PREFIX_AGDFASBV1238358761'] = _PREFIX_AGDFASBV1238358761

Mount = _reflection.GeneratedProtocolMessageType('Mount', (_message.Message,), dict(
  DESCRIPTOR = _MOUNT,
  __module__ = 'game.response.Mount_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response501659261.Mount)
  ))
_sym_db.RegisterMessage(Mount)

PREFIX_AGDFASBV1238358761 = _reflection.GeneratedProtocolMessageType('PREFIX_AGDFASBV1238358761', (_message.Message,), dict(
  DESCRIPTOR = _PREFIX_AGDFASBV1238358761,
  __module__ = 'game.response.Mount_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response501659261.PREFIX_AGDFASBV1238358761)
  ))
_sym_db.RegisterMessage(PREFIX_AGDFASBV1238358761)


# @@protoc_insertion_point(module_scope)
