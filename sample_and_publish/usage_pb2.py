# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: usage.proto

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
  name='usage.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0busage.proto\"$\n\x05Usage\x12\x0c\n\x04time\x18\x01 \x01(\x02\x12\r\n\x05usage\x18\x02 \x01(\x02\x62\x06proto3')
)




_USAGE = _descriptor.Descriptor(
  name='Usage',
  full_name='Usage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='Usage.time', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usage', full_name='Usage.usage', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=51,
)

DESCRIPTOR.message_types_by_name['Usage'] = _USAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Usage = _reflection.GeneratedProtocolMessageType('Usage', (_message.Message,), dict(
  DESCRIPTOR = _USAGE,
  __module__ = 'usage_pb2'
  # @@protoc_insertion_point(class_scope:Usage)
  ))
_sym_db.RegisterMessage(Usage)


# @@protoc_insertion_point(module_scope)
