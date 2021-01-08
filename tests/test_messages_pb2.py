# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_messages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_messages.proto',
  package='tests',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13test_messages.proto\x12\x05tests\"\x0b\n\tTestProto\"$\n\x0fTestResultProto\x12\x11\n\tvalue_str\x18\x01 \x01(\t\"!\n\x0cUnknownProto\x12\x11\n\tvalue_str\x18\x01 \x01(\t\"3\n\nTestPerson\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\"I\n\x13TestGreetingRequest\x12!\n\x06person\x18\x01 \x01(\x0b\x32\x11.tests.TestPerson\x12\x0f\n\x07message\x18\x02 \x01(\t\"(\n\x14TestGreetingResponse\x12\x10\n\x08greeting\x18\x03 \x01(\tb\x06proto3'
)




_TESTPROTO = _descriptor.Descriptor(
  name='TestProto',
  full_name='tests.TestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=30,
  serialized_end=41,
)


_TESTRESULTPROTO = _descriptor.Descriptor(
  name='TestResultProto',
  full_name='tests.TestResultProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value_str', full_name='tests.TestResultProto.value_str', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=43,
  serialized_end=79,
)


_UNKNOWNPROTO = _descriptor.Descriptor(
  name='UnknownProto',
  full_name='tests.UnknownProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value_str', full_name='tests.UnknownProto.value_str', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=81,
  serialized_end=114,
)


_TESTPERSON = _descriptor.Descriptor(
  name='TestPerson',
  full_name='tests.TestPerson',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='tests.TestPerson.first_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='tests.TestPerson.last_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=116,
  serialized_end=167,
)


_TESTGREETINGREQUEST = _descriptor.Descriptor(
  name='TestGreetingRequest',
  full_name='tests.TestGreetingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person', full_name='tests.TestGreetingRequest.person', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='tests.TestGreetingRequest.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=169,
  serialized_end=242,
)


_TESTGREETINGRESPONSE = _descriptor.Descriptor(
  name='TestGreetingResponse',
  full_name='tests.TestGreetingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='greeting', full_name='tests.TestGreetingResponse.greeting', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=244,
  serialized_end=284,
)

_TESTGREETINGREQUEST.fields_by_name['person'].message_type = _TESTPERSON
DESCRIPTOR.message_types_by_name['TestProto'] = _TESTPROTO
DESCRIPTOR.message_types_by_name['TestResultProto'] = _TESTRESULTPROTO
DESCRIPTOR.message_types_by_name['UnknownProto'] = _UNKNOWNPROTO
DESCRIPTOR.message_types_by_name['TestPerson'] = _TESTPERSON
DESCRIPTOR.message_types_by_name['TestGreetingRequest'] = _TESTGREETINGREQUEST
DESCRIPTOR.message_types_by_name['TestGreetingResponse'] = _TESTGREETINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestProto = _reflection.GeneratedProtocolMessageType('TestProto', (_message.Message,), {
  'DESCRIPTOR' : _TESTPROTO,
  '__module__' : 'test_messages_pb2'
  # @@protoc_insertion_point(class_scope:tests.TestProto)
  })
_sym_db.RegisterMessage(TestProto)

TestResultProto = _reflection.GeneratedProtocolMessageType('TestResultProto', (_message.Message,), {
  'DESCRIPTOR' : _TESTRESULTPROTO,
  '__module__' : 'test_messages_pb2'
  # @@protoc_insertion_point(class_scope:tests.TestResultProto)
  })
_sym_db.RegisterMessage(TestResultProto)

UnknownProto = _reflection.GeneratedProtocolMessageType('UnknownProto', (_message.Message,), {
  'DESCRIPTOR' : _UNKNOWNPROTO,
  '__module__' : 'test_messages_pb2'
  # @@protoc_insertion_point(class_scope:tests.UnknownProto)
  })
_sym_db.RegisterMessage(UnknownProto)

TestPerson = _reflection.GeneratedProtocolMessageType('TestPerson', (_message.Message,), {
  'DESCRIPTOR' : _TESTPERSON,
  '__module__' : 'test_messages_pb2'
  # @@protoc_insertion_point(class_scope:tests.TestPerson)
  })
_sym_db.RegisterMessage(TestPerson)

TestGreetingRequest = _reflection.GeneratedProtocolMessageType('TestGreetingRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTGREETINGREQUEST,
  '__module__' : 'test_messages_pb2'
  # @@protoc_insertion_point(class_scope:tests.TestGreetingRequest)
  })
_sym_db.RegisterMessage(TestGreetingRequest)

TestGreetingResponse = _reflection.GeneratedProtocolMessageType('TestGreetingResponse', (_message.Message,), {
  'DESCRIPTOR' : _TESTGREETINGRESPONSE,
  '__module__' : 'test_messages_pb2'
  # @@protoc_insertion_point(class_scope:tests.TestGreetingResponse)
  })
_sym_db.RegisterMessage(TestGreetingResponse)


# @@protoc_insertion_point(module_scope)
