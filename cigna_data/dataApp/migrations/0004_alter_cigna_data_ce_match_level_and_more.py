# Generated by Django 4.1.1 on 2022-09-09 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataApp', '0003_alter_cigna_data_choice1c_ce_selected_individual_mari_805_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cigna_data',
            name='CE_Match_Level',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cigna_data',
            name='Wave_1_Email_Click',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cigna_data',
            name='Wave_1_Email_Creative_Code',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cigna_data',
            name='Wave_1_Email_Deliverability_Indicator',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cigna_data',
            name='Wave_1_Email_Open',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cigna_data',
            name='Wave_2_Email_Click',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cigna_data',
            name='Wave_2_Email_Creative_Code',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cigna_data',
            name='Wave_2_Email_Deliverability_Indicator',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cigna_data',
            name='Wave_2_Email_Open',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cigna_data',
            name='Wave_3_Email_Click',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cigna_data',
            name='Wave_3_Email_Creative_Code',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cigna_data',
            name='Wave_3_Email_Deliverability_Indicator',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='cigna_data',
            name='Wave_3_Email_Open',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
