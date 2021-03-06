from io import BytesIO
from kqml import KQMLObject
from .util import safe_decode

class KQMLString(object):
    def __init__(self, data=None):
        if data is None:
            self.data = ''
        else:
            self.data = safe_decode(data)

    def __len__(self):
        return len(self.data)

    def char_at(self, n):
        return self.data[n]

    def equals(self, obj):
        if not isinstance(obj, KQMLString):
            return False
        else:
            return obj.data == self.data

    def write(self, out):
        out.write(b'"')
        for ch in self.data:
            if ch == '"':
                out.write(b'\\')
            out.write(ch.encode())
        out.write(b'"')

    def to_string(self):
        out = BytesIO()
        self.write(out)
        return safe_decode(out.getvalue())

    def string_value(self):
        return self.data

    def __str__(self):
        return safe_decode(self.to_string())

    def __repr__(self):
        s = self.__str__()
        s = s.replace('\n', '\\n')
        return s

    def __getitem__(self, *args):
        return self.data.__getitem__(*args)

