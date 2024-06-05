# Generated by Django 4.2.11 on 2024-06-04 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0008_add_navigation_title_override"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personindexpage",
            name="theme",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "None"),
                    ("theme-coral", "Coral"),
                    ("theme-lagoon", "Lagoon"),
                    ("theme-banana", "Banana"),
                    ("theme-earth", "Earth"),
                ],
                help_text="The theme will be applied to this page and all of its descendants. If no theme is selected, it will be derived from this page's ancestors.",
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="personpage",
            name="theme",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "None"),
                    ("theme-coral", "Coral"),
                    ("theme-lagoon", "Lagoon"),
                    ("theme-banana", "Banana"),
                    ("theme-earth", "Earth"),
                ],
                help_text="The theme will be applied to this page and all of its descendants. If no theme is selected, it will be derived from this page's ancestors.",
                max_length=25,
            ),
        ),
    ]
