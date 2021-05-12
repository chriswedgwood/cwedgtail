# Generated by Django 3.1.8 on 2021-05-11 13:01

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210511_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('python', 'python'), ('javascript', 'javascript'), ('css', 'css'), ('markup', 'markup'), ('SQL', 'SQL')])), ('text', wagtail.core.blocks.TextBlock())]))]),
        ),
    ]