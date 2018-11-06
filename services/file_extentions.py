import os
from django.core.exceptions import ValidationError

def validate_bulten_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
    	raise ValidationError(u'sadece %s uzantılı dosyaları yükleyebilirsiniz' % (valid_extensions))

def validate_image_extention(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.svg','.jpg','.png']
    if not ext.lower() in valid_extensions:
    	raise ValidationError(u'sadece %s uzantılı dosyaları yükleyebilirsiniz' % (valid_extensions))

def validate_excel_extention(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.xls','.xlsx']
    if not ext.lower() in valid_extensions:
    	raise ValidationError(u'sadece %s uzantılı dosyaları yükleyebilirsiniz' % (valid_extensions))