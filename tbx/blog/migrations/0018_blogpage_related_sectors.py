# Generated by Django 4.2.9 on 2024-02-06 10:33

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("taxonomy", "0002_sector_team_remove_service_contact_reasons_and_more"),
        ("blog", "0017_blogindexpage_theme_blogpage_theme"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpage",
            name="related_sectors",
            field=modelcluster.fields.ParentalManyToManyField(
                related_name="blog_posts", to="taxonomy.sector"
            ),
        ),
    ]
