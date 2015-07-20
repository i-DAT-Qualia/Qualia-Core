import uuid
import os

def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    ext = filename.split('.')[1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("uploads/images/", filename)