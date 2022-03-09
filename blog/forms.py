from django import forms
from blog.models import Article


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    author = forms.EmailField(label="Votre adresse mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez une copie", required=False)

    def clean_message(self):
        message = self.cleaned_data['message']
        if "pizza" in message:
            raise forms.ValidationError("On ne veut pas entendre parler de pizza")
        return message


    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        subject = cleaned_data.get('subject')
        message = cleaned_data.get('message')

        if subject and message:
            if "pizza" in subject or "pizza" in message:
                msg = "Vous parlez de pizzas dans le sujet et le message? Non merci"
                self.add_error("message", msg)

        return cleaned_data


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'author', 'content', 'category']
