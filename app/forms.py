from django import forms

# from app.models import UserProfile

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ("city", "country")

#     def save(self, user=None):
#         user_profile = super(UserProfileForm, self).save(commit=False)
#         if user:
#             user_profile.user = user
#         user_profile.save()
#         return user_profile


class NewDogTagForm(forms.Form):
    owner_name = forms.CharField()
    dog_name = forms.CharField()
    dog_birthday = forms.DateField()
