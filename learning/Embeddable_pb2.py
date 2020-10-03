# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Embeddable.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Embeddable.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x45mbeddable.proto\"\xb7\x07\n\nEmbeddable\x12\x0b\n\x01\x62\x18\x01 \x01(\x08H\x00\x12\x0b\n\x01n\x18\x02 \x01(\x05H\x00\x12\x0b\n\x01s\x18\x03 \x01(\tH\x00\x12 \n\x04pair\x18\x04 \x01(\x0b\x32\x10.Embeddable.PairH\x00\x12\"\n\x05maybe\x18\x05 \x01(\x0b\x32\x11.Embeddable.MaybeH\x00\x12 \n\x04list\x18\x06 \x01(\x0b\x32\x10.Embeddable.ListH\x00\x12\"\n\x05\x61rray\x18\x07 \x01(\x0b\x32\x11.Embeddable.ArrayH\x00\x12\x1e\n\x03set\x18\x08 \x01(\x0b\x32\x0f.Embeddable.SetH\x00\x12\x1e\n\x03map\x18\t \x01(\x0b\x32\x0f.Embeddable.MapH\x00\x12 \n\x04grid\x18\n \x01(\x0b\x32\x10.Embeddable.GridH\x00\x12\"\n\x05graph\x18\x0b \x01(\x0b\x32\x11.Embeddable.GraphH\x00\x12$\n\x06record\x18\x0c \x01(\x0b\x32\x12.Embeddable.RecordH\x00\x1a:\n\x04Pair\x12\x18\n\x03\x66st\x18\x01 \x01(\x0b\x32\x0b.Embeddable\x12\x18\n\x03snd\x18\x02 \x01(\x0b\x32\x0b.Embeddable\x1a!\n\x05Maybe\x12\x18\n\x03val\x18\x01 \x01(\x0b\x32\x0b.Embeddable\x1a\"\n\x04List\x12\x1a\n\x05\x65lems\x18\x01 \x03(\x0b\x32\x0b.Embeddable\x1a#\n\x05\x41rray\x12\x1a\n\x05\x65lems\x18\x01 \x03(\x0b\x32\x0b.Embeddable\x1a!\n\x03Set\x12\x1a\n\x05\x65lems\x18\x01 \x03(\x0b\x32\x0b.Embeddable\x1a\'\n\x03Map\x12 \n\x06\x61ssocs\x18\x01 \x03(\x0b\x32\x10.Embeddable.Pair\x1a@\n\x04Grid\x12\r\n\x05nRows\x18\x01 \x01(\x05\x12\r\n\x05nCols\x18\x02 \x01(\x05\x12\x1a\n\x05\x65lems\x18\x03 \x03(\x0b\x32\x0b.Embeddable\x1a\x96\x01\n\x05Graph\x12\x0e\n\x06nNodes\x18\x01 \x01(\x05\x12\x1a\n\x05nodes\x18\x02 \x03(\x0b\x32\x0b.Embeddable\x12%\n\x05\x65\x64ges\x18\x03 \x03(\x0b\x32\x16.Embeddable.Graph.Edge\x1a:\n\x04\x45\x64ge\x12\x0b\n\x03src\x18\x01 \x01(\x05\x12\x0b\n\x03\x64st\x18\x02 \x01(\x05\x12\x18\n\x03val\x18\x03 \x01(\x0b\x32\x0b.Embeddable\x1as\n\x06Record\x12\x0c\n\x04name\x18\x01 \x01(\t\x12(\n\x06\x66ields\x18\x02 \x03(\x0b\x32\x18.Embeddable.Record.Field\x1a\x31\n\x05\x46ield\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1a\n\x05value\x18\x02 \x01(\x0b\x32\x0b.EmbeddableB\x06\n\x04\x62odyb\x06proto3'
)


_EMBEDDABLE_PAIR = _descriptor.Descriptor(
  name='Pair',
  full_name='Embeddable.Pair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fst', full_name='Embeddable.Pair.fst', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='snd', full_name='Embeddable.Pair.snd', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=386,
  serialized_end=444,
)

_EMBEDDABLE_MAYBE = _descriptor.Descriptor(
  name='Maybe',
  full_name='Embeddable.Maybe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='Embeddable.Maybe.val', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=446,
  serialized_end=479,
)

_EMBEDDABLE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='Embeddable.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='elems', full_name='Embeddable.List.elems', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=481,
  serialized_end=515,
)

_EMBEDDABLE_ARRAY = _descriptor.Descriptor(
  name='Array',
  full_name='Embeddable.Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='elems', full_name='Embeddable.Array.elems', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=517,
  serialized_end=552,
)

_EMBEDDABLE_SET = _descriptor.Descriptor(
  name='Set',
  full_name='Embeddable.Set',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='elems', full_name='Embeddable.Set.elems', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=554,
  serialized_end=587,
)

_EMBEDDABLE_MAP = _descriptor.Descriptor(
  name='Map',
  full_name='Embeddable.Map',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='assocs', full_name='Embeddable.Map.assocs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=589,
  serialized_end=628,
)

_EMBEDDABLE_GRID = _descriptor.Descriptor(
  name='Grid',
  full_name='Embeddable.Grid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nRows', full_name='Embeddable.Grid.nRows', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nCols', full_name='Embeddable.Grid.nCols', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='elems', full_name='Embeddable.Grid.elems', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=630,
  serialized_end=694,
)

_EMBEDDABLE_GRAPH_EDGE = _descriptor.Descriptor(
  name='Edge',
  full_name='Embeddable.Graph.Edge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='Embeddable.Graph.Edge.src', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dst', full_name='Embeddable.Graph.Edge.dst', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='val', full_name='Embeddable.Graph.Edge.val', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=789,
  serialized_end=847,
)

_EMBEDDABLE_GRAPH = _descriptor.Descriptor(
  name='Graph',
  full_name='Embeddable.Graph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nNodes', full_name='Embeddable.Graph.nNodes', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='Embeddable.Graph.nodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='edges', full_name='Embeddable.Graph.edges', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EMBEDDABLE_GRAPH_EDGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=697,
  serialized_end=847,
)

_EMBEDDABLE_RECORD_FIELD = _descriptor.Descriptor(
  name='Field',
  full_name='Embeddable.Record.Field',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Embeddable.Record.Field.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Embeddable.Record.Field.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=915,
  serialized_end=964,
)

_EMBEDDABLE_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='Embeddable.Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Embeddable.Record.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fields', full_name='Embeddable.Record.fields', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EMBEDDABLE_RECORD_FIELD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=849,
  serialized_end=964,
)

_EMBEDDABLE = _descriptor.Descriptor(
  name='Embeddable',
  full_name='Embeddable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='b', full_name='Embeddable.b', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='n', full_name='Embeddable.n', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='s', full_name='Embeddable.s', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pair', full_name='Embeddable.pair', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maybe', full_name='Embeddable.maybe', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='list', full_name='Embeddable.list', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='array', full_name='Embeddable.array', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='set', full_name='Embeddable.set', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='map', full_name='Embeddable.map', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grid', full_name='Embeddable.grid', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='graph', full_name='Embeddable.graph', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='record', full_name='Embeddable.record', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EMBEDDABLE_PAIR, _EMBEDDABLE_MAYBE, _EMBEDDABLE_LIST, _EMBEDDABLE_ARRAY, _EMBEDDABLE_SET, _EMBEDDABLE_MAP, _EMBEDDABLE_GRID, _EMBEDDABLE_GRAPH, _EMBEDDABLE_RECORD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='body', full_name='Embeddable.body',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=21,
  serialized_end=972,
)

_EMBEDDABLE_PAIR.fields_by_name['fst'].message_type = _EMBEDDABLE
_EMBEDDABLE_PAIR.fields_by_name['snd'].message_type = _EMBEDDABLE
_EMBEDDABLE_PAIR.containing_type = _EMBEDDABLE
_EMBEDDABLE_MAYBE.fields_by_name['val'].message_type = _EMBEDDABLE
_EMBEDDABLE_MAYBE.containing_type = _EMBEDDABLE
_EMBEDDABLE_LIST.fields_by_name['elems'].message_type = _EMBEDDABLE
_EMBEDDABLE_LIST.containing_type = _EMBEDDABLE
_EMBEDDABLE_ARRAY.fields_by_name['elems'].message_type = _EMBEDDABLE
_EMBEDDABLE_ARRAY.containing_type = _EMBEDDABLE
_EMBEDDABLE_SET.fields_by_name['elems'].message_type = _EMBEDDABLE
_EMBEDDABLE_SET.containing_type = _EMBEDDABLE
_EMBEDDABLE_MAP.fields_by_name['assocs'].message_type = _EMBEDDABLE_PAIR
_EMBEDDABLE_MAP.containing_type = _EMBEDDABLE
_EMBEDDABLE_GRID.fields_by_name['elems'].message_type = _EMBEDDABLE
_EMBEDDABLE_GRID.containing_type = _EMBEDDABLE
_EMBEDDABLE_GRAPH_EDGE.fields_by_name['val'].message_type = _EMBEDDABLE
_EMBEDDABLE_GRAPH_EDGE.containing_type = _EMBEDDABLE_GRAPH
_EMBEDDABLE_GRAPH.fields_by_name['nodes'].message_type = _EMBEDDABLE
_EMBEDDABLE_GRAPH.fields_by_name['edges'].message_type = _EMBEDDABLE_GRAPH_EDGE
_EMBEDDABLE_GRAPH.containing_type = _EMBEDDABLE
_EMBEDDABLE_RECORD_FIELD.fields_by_name['value'].message_type = _EMBEDDABLE
_EMBEDDABLE_RECORD_FIELD.containing_type = _EMBEDDABLE_RECORD
_EMBEDDABLE_RECORD.fields_by_name['fields'].message_type = _EMBEDDABLE_RECORD_FIELD
_EMBEDDABLE_RECORD.containing_type = _EMBEDDABLE
_EMBEDDABLE.fields_by_name['pair'].message_type = _EMBEDDABLE_PAIR
_EMBEDDABLE.fields_by_name['maybe'].message_type = _EMBEDDABLE_MAYBE
_EMBEDDABLE.fields_by_name['list'].message_type = _EMBEDDABLE_LIST
_EMBEDDABLE.fields_by_name['array'].message_type = _EMBEDDABLE_ARRAY
_EMBEDDABLE.fields_by_name['set'].message_type = _EMBEDDABLE_SET
_EMBEDDABLE.fields_by_name['map'].message_type = _EMBEDDABLE_MAP
_EMBEDDABLE.fields_by_name['grid'].message_type = _EMBEDDABLE_GRID
_EMBEDDABLE.fields_by_name['graph'].message_type = _EMBEDDABLE_GRAPH
_EMBEDDABLE.fields_by_name['record'].message_type = _EMBEDDABLE_RECORD
_EMBEDDABLE.oneofs_by_name['body'].fields.append(
  _EMBEDDABLE.fields_by_name['b'])
_EMBEDDABLE.fields_by_name['b'].containing_oneof = _EMBEDDABLE.oneofs_by_name['body']
_EMBEDDABLE.oneofs_by_name['body'].fields.append(
  _EMBEDDABLE.fields_by_name['n'])
_EMBEDDABLE.fields_by_name['n'].containing_oneof = _EMBEDDABLE.oneofs_by_name['body']
_EMBEDDABLE.oneofs_by_name['body'].fields.append(
  _EMBEDDABLE.fields_by_name['s'])
_EMBEDDABLE.fields_by_name['s'].containing_oneof = _EMBEDDABLE.oneofs_by_name['body']
_EMBEDDABLE.oneofs_by_name['body'].fields.append(
  _EMBEDDABLE.fields_by_name['pair'])
_EMBEDDABLE.fields_by_name['pair'].containing_oneof = _EMBEDDABLE.oneofs_by_name['body']
_EMBEDDABLE.oneofs_by_name['body'].fields.append(
  _EMBEDDABLE.fields_by_name['maybe'])
_EMBEDDABLE.fields_by_name['maybe'].containing_oneof = _EMBEDDABLE.oneofs_by_name['body']
_EMBEDDABLE.oneofs_by_name['body'].fields.append(
  _EMBEDDABLE.fields_by_name['list'])
_EMBEDDABLE.fields_by_name['list'].containing_oneof = _EMBEDDABLE.oneofs_by_name['body']
_EMBEDDABLE.oneofs_by_name['body'].fields.append(
  _EMBEDDABLE.fields_by_name['array'])
_EMBEDDABLE.fields_by_name['array'].containing_oneof = _EMBEDDABLE.oneofs_by_name['body']
_EMBEDDABLE.oneofs_by_name['body'].fields.append(
  _EMBEDDABLE.fields_by_name['set'])
_EMBEDDABLE.fields_by_name['set'].containing_oneof = _EMBEDDABLE.oneofs_by_name['body']
_EMBEDDABLE.oneofs_by_name['body'].fields.append(
  _EMBEDDABLE.fields_by_name['map'])
_EMBEDDABLE.fields_by_name['map'].containing_oneof = _EMBEDDABLE.oneofs_by_name['body']
_EMBEDDABLE.oneofs_by_name['body'].fields.append(
  _EMBEDDABLE.fields_by_name['grid'])
_EMBEDDABLE.fields_by_name['grid'].containing_oneof = _EMBEDDABLE.oneofs_by_name['body']
_EMBEDDABLE.oneofs_by_name['body'].fields.append(
  _EMBEDDABLE.fields_by_name['graph'])
_EMBEDDABLE.fields_by_name['graph'].containing_oneof = _EMBEDDABLE.oneofs_by_name['body']
_EMBEDDABLE.oneofs_by_name['body'].fields.append(
  _EMBEDDABLE.fields_by_name['record'])
_EMBEDDABLE.fields_by_name['record'].containing_oneof = _EMBEDDABLE.oneofs_by_name['body']
DESCRIPTOR.message_types_by_name['Embeddable'] = _EMBEDDABLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Embeddable = _reflection.GeneratedProtocolMessageType('Embeddable', (_message.Message,), {

  'Pair' : _reflection.GeneratedProtocolMessageType('Pair', (_message.Message,), {
    'DESCRIPTOR' : _EMBEDDABLE_PAIR,
    '__module__' : 'Embeddable_pb2'
    # @@protoc_insertion_point(class_scope:Embeddable.Pair)
    })
  ,

  'Maybe' : _reflection.GeneratedProtocolMessageType('Maybe', (_message.Message,), {
    'DESCRIPTOR' : _EMBEDDABLE_MAYBE,
    '__module__' : 'Embeddable_pb2'
    # @@protoc_insertion_point(class_scope:Embeddable.Maybe)
    })
  ,

  'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
    'DESCRIPTOR' : _EMBEDDABLE_LIST,
    '__module__' : 'Embeddable_pb2'
    # @@protoc_insertion_point(class_scope:Embeddable.List)
    })
  ,

  'Array' : _reflection.GeneratedProtocolMessageType('Array', (_message.Message,), {
    'DESCRIPTOR' : _EMBEDDABLE_ARRAY,
    '__module__' : 'Embeddable_pb2'
    # @@protoc_insertion_point(class_scope:Embeddable.Array)
    })
  ,

  'Set' : _reflection.GeneratedProtocolMessageType('Set', (_message.Message,), {
    'DESCRIPTOR' : _EMBEDDABLE_SET,
    '__module__' : 'Embeddable_pb2'
    # @@protoc_insertion_point(class_scope:Embeddable.Set)
    })
  ,

  'Map' : _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), {
    'DESCRIPTOR' : _EMBEDDABLE_MAP,
    '__module__' : 'Embeddable_pb2'
    # @@protoc_insertion_point(class_scope:Embeddable.Map)
    })
  ,

  'Grid' : _reflection.GeneratedProtocolMessageType('Grid', (_message.Message,), {
    'DESCRIPTOR' : _EMBEDDABLE_GRID,
    '__module__' : 'Embeddable_pb2'
    # @@protoc_insertion_point(class_scope:Embeddable.Grid)
    })
  ,

  'Graph' : _reflection.GeneratedProtocolMessageType('Graph', (_message.Message,), {

    'Edge' : _reflection.GeneratedProtocolMessageType('Edge', (_message.Message,), {
      'DESCRIPTOR' : _EMBEDDABLE_GRAPH_EDGE,
      '__module__' : 'Embeddable_pb2'
      # @@protoc_insertion_point(class_scope:Embeddable.Graph.Edge)
      })
    ,
    'DESCRIPTOR' : _EMBEDDABLE_GRAPH,
    '__module__' : 'Embeddable_pb2'
    # @@protoc_insertion_point(class_scope:Embeddable.Graph)
    })
  ,

  'Record' : _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), {

    'Field' : _reflection.GeneratedProtocolMessageType('Field', (_message.Message,), {
      'DESCRIPTOR' : _EMBEDDABLE_RECORD_FIELD,
      '__module__' : 'Embeddable_pb2'
      # @@protoc_insertion_point(class_scope:Embeddable.Record.Field)
      })
    ,
    'DESCRIPTOR' : _EMBEDDABLE_RECORD,
    '__module__' : 'Embeddable_pb2'
    # @@protoc_insertion_point(class_scope:Embeddable.Record)
    })
  ,
  'DESCRIPTOR' : _EMBEDDABLE,
  '__module__' : 'Embeddable_pb2'
  # @@protoc_insertion_point(class_scope:Embeddable)
  })
_sym_db.RegisterMessage(Embeddable)
_sym_db.RegisterMessage(Embeddable.Pair)
_sym_db.RegisterMessage(Embeddable.Maybe)
_sym_db.RegisterMessage(Embeddable.List)
_sym_db.RegisterMessage(Embeddable.Array)
_sym_db.RegisterMessage(Embeddable.Set)
_sym_db.RegisterMessage(Embeddable.Map)
_sym_db.RegisterMessage(Embeddable.Grid)
_sym_db.RegisterMessage(Embeddable.Graph)
_sym_db.RegisterMessage(Embeddable.Graph.Edge)
_sym_db.RegisterMessage(Embeddable.Record)
_sym_db.RegisterMessage(Embeddable.Record.Field)


# @@protoc_insertion_point(module_scope)