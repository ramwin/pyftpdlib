import sys
import os

PY3 = sys.version_info[0] == 3

if PY3:
    import builtins

    def u(s):
        return s

    def b(s):
        return s.encode("latin-1")

    MAXSIZE = sys.maxsize
    print_ = getattr(builtins, "print")
    getcwdu = os.getcwd
    unicode = str
    xrange = range
else:
    def u(s):
        return unicode(s, "unicode_escape")

    def b(s):
        return s

    def print_(s):
        sys.stdout.write(s + '\n')
        sys.stdout.flush()

    MAXSIZE = sys.maxsize
    getcwdu = os.getcwdu
    unicode = unicode
    xrange = xrange


_default = object()
try:
    next = next
except NameError:
    def next(iterable, default=_default):
        if default == _default:
            return iterable.next()
        else:
            try:
                return iterable.next()
            except StopIteration:
                return default