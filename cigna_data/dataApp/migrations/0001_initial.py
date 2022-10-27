# Generated by Django 4.1.1 on 2022-09-06 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cigna_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SEQUENCE_NO', models.CharField(max_length=200)),
                ('ORDER_ID', models.CharField(max_length=200)),
                ('LIST_ID', models.BigIntegerField()),
                ('ULTIMATE_DUNS_NUMBER', models.BigIntegerField()),
                ('Choice1A_Decile', models.BigIntegerField()),
                ('Choice1A_p_1', models.FloatField()),
                ('Choice1B_p_sp', models.FloatField()),
                ('Choice1C_P_1', models.FloatField()),
                ('Choice1C_Decile', models.BigIntegerField()),
                ('Choice1C_CE_Selected_Individual_Mari_805', models.CharField(max_length=200)),
                ('BH_MedResp_resp_decile', models.BigIntegerField()),
                ('BH_MedResp_filler1', models.FloatField()),
                ('BH_MedResp_P_resp', models.FloatField()),
                ('BH_MedResp_filler2', models.FloatField()),
                ('Opt_P_Enroll_backend_target1', models.FloatField()),
                ('Opt_P_Enroll_prop_target1', models.FloatField()),
                ('Opt_Enroll_backend_decile', models.BigIntegerField()),
                ('Opt_Enroll_prop_decile', models.BigIntegerField()),
                ('Segmentation_into', models.BigIntegerField()),
                ('MZP_Individual_ID', models.BigIntegerField()),
                ('MZP_Household_ID', models.BigIntegerField()),
                ('Control', models.BigIntegerField()),
                ('Wave_1_OMD', models.BigIntegerField()),
                ('Wave_1_OMD_Creative_Code', models.CharField(max_length=200)),
                ('Wave_1_OMD_Code_on_Mail', models.FloatField()),
                ('Wave_2_OMD', models.BigIntegerField()),
                ('Wave_2_OMD_Creative_Code', models.FloatField()),
                ('Wave_2_OMD_Code_on_Mail', models.FloatField()),
                ('Wave_3_OMD', models.BigIntegerField()),
                ('Wave_4_OMD_Creative_Code', models.FloatField()),
                ('Wave_4_OMD_Code_on_Mail', models.FloatField()),
                ('Wave_4_OMD', models.BigIntegerField()),
                ('Wave_3_OMD_Creative_Code', models.FloatField()),
                ('Wave_3_OMD_Code_on_Mail', models.FloatField()),
                ('Wave_1_Mail', models.BigIntegerField()),
                ('Wave_1_Mail_Creative_Code', models.FloatField()),
                ('Wave_1_Mail_Code_on_Mail', models.FloatField()),
                ('Wave_1_Email', models.BigIntegerField()),
                ('Wave_1_Email_Creative_Code', models.FloatField()),
                ('Wave_1_Email_Code_on_Mail', models.FloatField()),
                ('Wave_1_Email_Deliverability_Indicator', models.CharField(max_length=300)),
                ('Wave_1_Email_Open', models.CharField(max_length=300)),
                ('Wave_1_Email_Click', models.CharField(max_length=300)),
                ('Wave_2_Mail', models.BigIntegerField()),
                ('Wave_2_Mail_Creative_Code', models.FloatField()),
                ('Wave_2_Mail_Code_on_Mail', models.FloatField()),
                ('Wave_2_Email', models.BigIntegerField()),
                ('Wave_2_Email_Creative_Code', models.CharField(max_length=300)),
                ('Wave_2_Email_Code_on_Mail', models.FloatField()),
                ('Wave_2_Email_Deliverability_Indicator', models.CharField(max_length=300)),
                ('Wave_2_Email_Open', models.CharField(max_length=300)),
                ('Wave_2_Email_Click', models.CharField(max_length=300)),
                ('Wave_3_Mail_Creative_Code', models.FloatField()),
                ('Wave_3_Mail_Code_on_Mail', models.FloatField()),
                ('Wave_3_Email', models.BigIntegerField()),
                ('Wave_3_Email_Creative_Code', models.CharField(max_length=300)),
                ('Wave_3_Email_Code_on_Mail', models.FloatField()),
                ('Wave_3_Email_Deliverability_Indicator', models.CharField(max_length=300)),
                ('Wave_3_Email_Open', models.CharField(max_length=300)),
                ('Wave_3_Email_Click', models.CharField(max_length=300)),
                ('Wave_4_Mail', models.BigIntegerField()),
                ('Wave_4_Mail_Creative_Code', models.FloatField()),
                ('Wave_4_Mail_Code_on_Mail', models.FloatField()),
                ('Wave_4_Email', models.BigIntegerField()),
                ('Wave_4_Email_Creative_Code', models.FloatField()),
                ('Wave_4_Email_Code_on_Mail', models.FloatField()),
                ('Wave_4_Email_Deliverability_Indicator', models.FloatField()),
                ('Wave_4_Email_Open', models.FloatField()),
                ('Wave_4_Email_Click', models.FloatField()),
                ('Wave_1_Social', models.BigIntegerField()),
                ('Wave_1_Social_Creative_Code', models.FloatField()),
                ('Wave_1_Social_Code_on_Mail', models.FloatField()),
                ('Wave_2_Social', models.BigIntegerField()),
                ('Wave_2_Social_Creative_Code', models.FloatField()),
                ('Wave_2_Social_Code_on_Mail', models.FloatField()),
                ('Wave_3_Social', models.BigIntegerField()),
                ('Wave_3_Social_Creative_Code', models.FloatField()),
                ('Wave_3_Social_Code_on_Mail', models.FloatField()),
                ('Wave_4_Social', models.BigIntegerField()),
                ('Wave_4_Social_Creative_Code', models.FloatField()),
                ('Wave_4_Social_Code_on_Mail', models.FloatField()),
                ('New_Customer_Match', models.BigIntegerField()),
                ('Individual_Enterprise_ID', models.FloatField()),
                ('CE_Match_Level', models.CharField(max_length=300)),
            ],
        ),
    ]