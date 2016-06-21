from django_boto.s3 import upload
from django.core.files.uploadedfile import InMemoryUploadedFile

from PIL import Image
from StringIO import StringIO


def reformat_original(imageObject, size, ls, original_name):
    '''ls is 'long side' in pixels'''
    if ls > 600:
        new_size = (size[0]*600/ls, size[1]*600/ls)

        imageObject.resize(new_size, Image.ANTIALIAS)

    smallerImage_io = StringIO()

    imageObject.save(smallerImage_io, format='JPEG', quality=95)

    new_upload = InMemoryUploadedFile(
        smallerImage_io, None, original_name,
        'image/jpeg', smallerImage_io.len, None
    )

    return (new_upload)


def resize_upload_image(im, upload_pic):
    ''' The argument "im" is the PIL image object of upload_pic.
    Save quality=95 from http://stackoverflow.com/questions/1405602/how-to-adjust-the-quality-of-a-resized-image-in-python-imaging-library.'''
    size = im.size
    upload_name = upload_pic.name

    ls = max(size)
    # ls for long side
    
    new_upload = reformat_original(im, size, ls, upload_name)

    thumb_size = (size[0] * 128 / ls, size[1] * 128 / ls)

    im.thumbnail(thumb_size, Image.ANTIALIAS)
    
    thumb_name = upload_name.split('.')[0]+"_thumb.jpg"
    
    thumb_io = StringIO()

    im.save(thumb_io, format='JPEG', quality=95)
    
    thumb_file = InMemoryUploadedFile(thumb_io, None, thumb_name, 'image/jpeg', thumb_io.len, None)

    return new_upload, thumb_file, thumb_name


def image_process(upload_pic):
    im = Image.open(StringIO(upload_pic.read()))

    new_upload, thumb_file, thumb_name = resize_upload_image(im, upload_pic)
    
    upload_path=upload(new_upload)

    thumb_path=upload(thumb_file)

    return upload_path, thumb_path