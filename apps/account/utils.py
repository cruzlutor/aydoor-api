# -*- coding: utf-8 -*-
import os
from django.utils.text import slugify
import hashlib
import time

def upload_avatar(instance, filename):
    hash = hashlib.sha1()
    hash.update(str(time.time()))   
    filename_base, filename_ext = os.path.splitext(filename)
    return 'avatars/%s%s%s' % (
        slugify(instance.email)+'_avatar_',
        str(hash.hexdigest()),
        filename_ext.lower(),
    )