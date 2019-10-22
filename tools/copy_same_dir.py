#!/usr/bin/env python
# encoding:utf-8

"""
复制相同的目录结构,不复制文件内容

2019-10-15
"""
import os


def copy_dir(old_dir, new_dir):
    child_dir = os.listdir(old_dir)
    for d in child_dir:
        n_d = os.path.join(old_dir, d)
        n_r = os.path.join(new_dir, d)
        if os.path.isdir(n_d):
            if not os.path.exists(n_r):
                os.mkdir(n_r)
            copy_dir(n_d, n_r)
        else:
            n_f = os.path.join(new_dir, d)
            os.system('touch {}'.format(n_f))


if __name__ == "__main__":
    copy_dir('source_dir', 'target_dir')
