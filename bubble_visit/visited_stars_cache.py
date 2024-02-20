import struct


def bytes_from_ids(system_ids: list[int]) -> bytes:
    array = bytearray(b"VisitedStars\0\0\0\0")

    array += struct.pack("i", 200)
    array += struct.pack("i", 48)  # header size in bytes
    array += struct.pack("i", len(system_ids))  # total entries
    array += struct.pack("i", 16)  # bytes per entry

    array += struct.pack("q", 0)  # player id
    array += struct.pack("q", 0)  # trade data id

    for system_id in system_ids:
        array += system_entry(system_id)

    array += b"\xDE\xC0\xFE\x5A\xDE\xC0\xFE\x5A"

    return bytes(array)


def system_entry(system_id: int) -> bytes:
    array = bytearray()

    array += struct.pack("q", system_id)  # system id
    array += struct.pack("i", 1)  # visit count
    array += struct.pack("i", 0)  # date?

    return bytes(array)
