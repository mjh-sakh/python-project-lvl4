from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, SetPasswordForm
from django.utils.translation import gettext as _


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label=_("Username"),
        help_text=_("Required field. Max length is 150 symbols. Letter, numbers only."),
        max_length=150,
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'title': _("Required field. Max length is 150 symbols. Letter, numbers only."),
            }),
        )
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


class CustomUserForm(SetPasswordForm):
    username = UsernameField(
        label=_("Username"),
        help_text=_("Required field. Max length is 150 symbols. Letter, numbers only."),
        max_length=150,
        widget=forms.TextInput(attrs={
            'autofocus': True,
            'title': _("Required field. Max length is 150 symbols. Letter, numbers only."),
            }),
        )
    first_name = forms.CharField(
        label=_('First name'),
        max_length=150,
        )
    last_name = forms.CharField(
        label=_('Last name'),
        max_length=150,
        )

    def save(self, commit=True):
        self.user.username = self.cleaned_data["username"]
        self.user.first_name = self.cleaned_data["first_name"]
        self.user.last_name = self.cleaned_data["last_name"]
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
