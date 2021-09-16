from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, PasswordChangeForm
# from django.
from django.utils.translation import gettext as _


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        help_text=_("Required field. Max length is 150 symbols. Letter, numbers only."),
        widget=forms.TextInput(attrs={
            'autofocus': True,
            # 'class': 'form-control',
            'maxlength': 150,
            'help_text': 'i am so sad',
            'show_help': True,
            'placeholder': _("username"),
            'title': _("Required field. Max length is 150 symbols. Letter, numbers only."),
    }))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        help_text=_("Password min length is 8 symbols."),
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'form-control',
            'placeholder': _("Password"),
            'title': _("Password min length is 8 symbols."),
        }),
    )


class CustomUserForm(PasswordChangeForm):
    pass
