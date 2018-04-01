from struct import *
from zlib import *


class PNGChunk:

    def __init__(self, size, name, cdata):
        self.__dict__.update(locals())

    def __repr__(self):
        return "(%s:%s)" % (self.name, self.size)

    @property
    def crc(self):
        combined = bytes()
        combined += pack("4s", self.name)
        combined += self.cdata
        combined = crc32(combined)
        return pack(">I", combined)

    def output(self):
        combined = bytes()
        combined += pack(">I", self.size)
        combined += pack("4s", self.name)
        combined += self.cdata
        combined += self.crc
        return combined
        

        

class PNG:

    def __getitem__(self, key):
        return self.chunks[key]


    def file(self, filename):
        self.load(open(filename, 'rb').read())


    def load(self, data, ignoreHeader=False):
        if not isinstance(data, bytes):
            raise TypeError

        if data[0:8] == b'\x89PNG\r\n\x1a\n':
            data = data[8:]
        else:
            if ignoreHeader:
                pass
            else:
                raise ValueError("Invalid PNG Header!")

        chunks = []
        i = 0
        while i < len(data):
            size, = unpack(">I", data[i:i+4])
            i+=4
            name, = unpack("4s", data[i:i+4])
            i+=4
            cdata = data[i:i+size]
            i+=size
            crc = data[i:i+4]
            i+=4
            chunks.append( PNGChunk(size, name, cdata) )

            if chunks[-1].crc != crc:
                print("Invalid crc found in %s" % (name))

        self.chunks = chunks            
        self._data = data


    def output(self):
        output = b'\x89PNG\r\n\x1a\n' #Don't forget to add header back!
        for chunk in self.chunks:
            output += chunk.output()
        return output
            







png = PNG()
png.file('test.png')
d = png._data
