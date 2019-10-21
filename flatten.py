def deepflatten(iterable, depth=None, types=None, ignore=None):
    if depth is None:
        depth = float('inf')
    if depth == -1:
        yield iterable
    else:
        for x in iterable:
            if ignore is not None and isinstance(x, ignore):
                yield x
            if types is None:
                try:
                    iter(x)
                except TypeError:
                    yield x
                else:
                    for item in deepflatten(x, depth - 1, types, ignore):
                        yield item
            elif not isinstance(x, types):
                yield x
            else:
                for item in deepflatten(x, depth - 1, types, ignore):
                    yield item
                    