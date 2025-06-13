from modeltranslation.translator import translator, TranslationOptions
from .models import Post

class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'excerpt',)

translator.register(Post, PostTranslationOptions)