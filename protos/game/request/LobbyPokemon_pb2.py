# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LobbyPokemon.proto

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
  name='LobbyPokemon.proto',
  package='PSXAPI.Request36',
  syntax='proto2',
  serialized_pb=_b('\n\x12LobbyPokemon.proto\x12\x10PSXAPI.Request36\"B\n\x0cLobbyPokemon\x12\x19\n\x0eSimultaneously\x18\x01 \x01(\x05:\x01\x30\x12\x17\n\x0cPokemonCount\x18\x02 \x01(\x05:\x01\x30')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LOBBYPOKEMON = _descriptor.Descriptor(
  name='LobbyPokemon',
  full_name='PSXAPI.Request36.LobbyPokemon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Simultaneously', full_name='PSXAPI.Request36.LobbyPokemon.Simultaneously', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PokemonCount', full_name='PSXAPI.Request36.LobbyPokemon.PokemonCount', index=1,
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
  serialized_start=40,
  serialized_end=106,
)

DESCRIPTOR.message_types_by_name['LobbyPokemon'] = _LOBBYPOKEMON

LobbyPokemon = _reflection.GeneratedProtocolMessageType('LobbyPokemon', (_message.Message,), dict(
  DESCRIPTOR = _LOBBYPOKEMON,
  __module__ = 'LobbyPokemon_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request36.LobbyPokemon)
  ))
_sym_db.RegisterMessage(LobbyPokemon)


# @@protoc_insertion_point(module_scope)
