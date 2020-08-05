from django import forms
from .models import OB

# 모델폼을 상속받아서 모델폼이 되었음
class OBFrom(forms.ModelForm):
# 어떤 모델과 대응되는지 말해줌
    class Meta:
        model = OB
        fields = ( "title", "image", "content")

# 모델 폼 커스텀
# init - 내장함수 - (해당 클레스에 들어오는 여러가지 인자를 받을 수 있는 파라미터)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['image'].label = "사진"
        self.fields['content'].label = "자기소개서 내용"
        self.fields['title'].widget.attrs.update({
            'class': 'OB_title', 
            'placeholder': '제목',
        })
