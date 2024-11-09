from django.core.exceptions import ValidationError
import re

# 英数字、アンダースコア、ハイフン、日本語のみ許可するバリデーション関数
def form_validation(value):
    allowed_pattern = r'^[\w\-ぁ-んァ-ン一-龥]+$'
    if not re.match(allowed_pattern, value):
        raise ValidationError('英数字、アンダースコア、ハイフン、日本語のみ使用可能です。')
