# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game/response/payload/PokemonStats.proto

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
  name='game/response/payload/PokemonStats.proto',
  package='PSXAPI.Response.Payload2063384285',
  syntax='proto2',
  serialized_pb=_b('\n(game/response/payload/PokemonStats.proto\x12!PSXAPI.Response.Payload2063384285\"s\n\x0cPokemonStats\x12\r\n\x02HP\x18\x01 \x01(\x05:\x01\x30\x12\x0e\n\x03\x41tk\x18\x02 \x01(\x05:\x01\x30\x12\x0e\n\x03\x44\x65\x66\x18\x03 \x01(\x05:\x01\x30\x12\x10\n\x05SpAtk\x18\x04 \x01(\x05:\x01\x30\x12\x10\n\x05SpDef\x18\x05 \x01(\x05:\x01\x30\x12\x10\n\x05Speed\x18\x06 \x01(\x05:\x01\x30')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_POKEMONSTATS = _descriptor.Descriptor(
  name='PokemonStats',
  full_name='PSXAPI.Response.Payload2063384285.PokemonStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='HP', full_name='PSXAPI.Response.Payload2063384285.PokemonStats.HP', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Atk', full_name='PSXAPI.Response.Payload2063384285.PokemonStats.Atk', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Def', full_name='PSXAPI.Response.Payload2063384285.PokemonStats.Def', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SpAtk', full_name='PSXAPI.Response.Payload2063384285.PokemonStats.SpAtk', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SpDef', full_name='PSXAPI.Response.Payload2063384285.PokemonStats.SpDef', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Speed', full_name='PSXAPI.Response.Payload2063384285.PokemonStats.Speed', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=79,
  serialized_end=194,
)

DESCRIPTOR.message_types_by_name['PokemonStats'] = _POKEMONSTATS

PokemonStats = _reflection.GeneratedProtocolMessageType('PokemonStats', (_message.Message,), dict(
  DESCRIPTOR = _POKEMONSTATS,
  __module__ = 'game.response.payload.PokemonStats_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response.Payload2063384285.PokemonStats)
  ))
_sym_db.RegisterMessage(PokemonStats)


# @@protoc_insertion_point(module_scope)
