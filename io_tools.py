from binascii import hexlify

def avro_hexlify(reader):
  """Return the hex value, as a string, of a binary-encoded int or long."""
  bytes = []
  current_byte = reader.read(1)
  bytes.append(hexlify(current_byte))
  while (ord(current_byte) & 0x80) != 0:
    current_byte = reader.read(1)
    bytes.append(hexlify(current_byte))
  return ' '.join(bytes)

