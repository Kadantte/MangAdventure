from os.path import join, splitext


def _rename_file(old, new):
    return new + splitext(old)[-1]


def _uploader(filename, newname, subdirs):
    return join(join(*subdirs), _rename_file(filename, newname))


def cover_uploader(obj, filename):
    return _uploader(filename, 'cover', ['series', obj.slug])


def group_logo_uploader(obj, filename):
    return _uploader(filename, 'logo', ['groups', str(obj.id)])


def avatar_uploader(obj, filename):
    return _uploader(filename, 'avatar', ['users', str(obj.id)])


__all__ = ['cover_uploader', 'group_logo_uploader', 'avatar_uploader']
