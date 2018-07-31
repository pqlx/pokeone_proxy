# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Mount.proto

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
  name='Mount.proto',
  package='PSXAPI.Response55',
  syntax='proto2',
  serialized_pb=_b('\n\x0bMount.proto\x12\x11PSXAPI.Response55\"T\n\x05Mount\x12\x12\n\x07MountID\x18\x01 \x01(\x05:\x01\x30\x12\x37\n\tMountType\x18\x02 \x01(\x0e\x32\x1c.PSXAPI.Response55.MountType:\x06__None*;\n\tMountType\x12\n\n\x06__None\x10\x00\x12\x0b\n\x07Surfing\x10\x01\x12\x08\n\x04\x42ike\x10\x02\x12\x0b\n\x07Pokemon\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MOUNTTYPE = _descriptor.EnumDescriptor(
  name='MountType',
  full_name='PSXAPI.Response55.MountType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='__None', index=0, number=0,
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
  serialized_start=120,
  serialized_end=179,
)
_sym_db.RegisterEnumDescriptor(_MOUNTTYPE)

MountType = enum_type_wrapper.EnumTypeWrapper(_MOUNTTYPE)
__None = 0
Surfing = 1
Bike = 2
Pokemon = 3



_MOUNT = _descriptor.Descriptor(
  name='Mount',
  full_name='PSXAPI.Response55.Mount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MountID', full_name='PSXAPI.Response55.Mount.MountID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MountType', full_name='PSXAPI.Response55.Mount.MountType', index=1,
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
  serialized_start=34,
  serialized_end=118,
)

_MOUNT.fields_by_name['MountType'].enum_type = _MOUNTTYPE
DESCRIPTOR.message_types_by_name['Mount'] = _MOUNT
DESCRIPTOR.enum_types_by_name['MountType'] = _MOUNTTYPE

Mount = _reflection.GeneratedProtocolMessageType('Mount', (_message.Message,), dict(
  DESCRIPTOR = _MOUNT,
  __module__ = 'Mount_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response55.Mount)
  ))
_sym_db.RegisterMessage(Mount)


# @@protoc_insertion_point(module_scope)
