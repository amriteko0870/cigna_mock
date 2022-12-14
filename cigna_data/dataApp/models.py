from django.db import models

# Create your models here.

class cigna_data(models.Model):
    SEQUENCE_NO = models.CharField(max_length=200,null=True)
    ORDER_ID = models.CharField(max_length=200,null=True)
    LIST_ID = models.BigIntegerField(null=True)
    ULTIMATE_DUNS_NUMBER = models.BigIntegerField(null=True)
    Choice1A_Decile = models.BigIntegerField(null=True)
    Choice1A_p_1 = models.FloatField(null=True)
    Choice1B_p_sp = models.FloatField(null=True)
    Choice1C_P_1 = models.FloatField(null=True)
    Choice1C_Decile = models.BigIntegerField(null=True)
    Choice1C_CE_Selected_Individual_Mari_805 = models.CharField(max_length=200,null=True)
    BH_MedResp_resp_decile = models.BigIntegerField(null=True)
    BH_MedResp_filler1 = models.FloatField(null=True)
    BH_MedResp_P_resp = models.FloatField(null=True)
    BH_MedResp_filler2 = models.FloatField(null=True)
    Opt_P_Enroll_backend_target1 = models.FloatField(null=True)
    Opt_P_Enroll_prop_target1 = models.FloatField(null=True)
    Opt_Enroll_backend_decile = models.BigIntegerField(null=True)
    Opt_Enroll_prop_decile = models.BigIntegerField(null=True)
    Segmentation_into = models.BigIntegerField(null=True)
    MZP_Individual_ID = models.BigIntegerField(null=True)
    MZP_Household_ID = models.BigIntegerField(null=True)
    Control = models.BigIntegerField(null=True)
    Wave_1_OMD = models.BigIntegerField(null=True)
    Wave_1_OMD_Creative_Code = models.CharField(max_length=200,null=True)
    Wave_1_OMD_Code_on_Mail = models.FloatField(null=True)
    Wave_2_OMD = models.BigIntegerField(null=True)
    Wave_2_OMD_Creative_Code = models.FloatField(null=True)
    Wave_2_OMD_Code_on_Mail = models.FloatField(null=True)
    Wave_3_OMD = models.BigIntegerField(null=True)
    Wave_4_OMD_Creative_Code = models.FloatField(null=True)
    Wave_4_OMD_Code_on_Mail = models.FloatField(null=True)
    Wave_4_OMD = models.BigIntegerField(null=True)
    Wave_3_OMD_Creative_Code = models.FloatField(null=True)
    Wave_3_OMD_Code_on_Mail = models.FloatField(null=True)
    Wave_1_Mail = models.BigIntegerField(null=True)
    Wave_1_Mail_Creative_Code = models.FloatField(null=True)
    Wave_1_Mail_Code_on_Mail = models.FloatField(null=True)
    Wave_1_Email = models.BigIntegerField(null=True)
    Wave_1_Email_Creative_Code = models.CharField(max_length=300,null=True)
    Wave_1_Email_Code_on_Mail = models.FloatField(null=True)
    Wave_1_Email_Deliverability_Indicator = models.CharField(max_length=300,null=True)
    Wave_1_Email_Open = models.CharField(max_length=300,null=True)
    Wave_1_Email_Click = models.CharField(max_length=300,null=True)
    Wave_2_Mail = models.BigIntegerField(null=True)
    Wave_2_Mail_Creative_Code = models.FloatField(null=True)
    Wave_2_Mail_Code_on_Mail = models.FloatField(null=True)
    Wave_2_Email = models.BigIntegerField(null=True)
    Wave_2_Email_Creative_Code = models.CharField(max_length=300,null=True)
    Wave_2_Email_Code_on_Mail = models.FloatField(null=True)
    Wave_2_Email_Deliverability_Indicator = models.CharField(max_length=300,null=True)
    Wave_2_Email_Open = models.CharField(max_length=300,null=True)
    Wave_2_Email_Click = models.CharField(max_length=300,null=True)
    Wave_3_Mail = models.BigIntegerField(null=True)
    Wave_3_Mail_Creative_Code = models.FloatField(null=True)
    Wave_3_Mail_Code_on_Mail = models.FloatField(null=True)
    Wave_3_Email = models.BigIntegerField(null=True)
    Wave_3_Email_Creative_Code = models.CharField(max_length=300,null=True)
    Wave_3_Email_Code_on_Mail = models.FloatField(null=True)
    Wave_3_Email_Deliverability_Indicator = models.CharField(max_length=300,null=True)
    Wave_3_Email_Open = models.CharField(max_length=300,null=True)
    Wave_3_Email_Click = models.CharField(max_length=300,null=True)
    Wave_4_Mail = models.BigIntegerField(null=True)
    Wave_4_Mail_Creative_Code = models.FloatField(null=True)
    Wave_4_Mail_Code_on_Mail = models.FloatField(null=True)
    Wave_4_Email = models.BigIntegerField(null=True)
    Wave_4_Email_Creative_Code = models.FloatField(null=True)
    Wave_4_Email_Code_on_Mail = models.FloatField(null=True)
    Wave_4_Email_Deliverability_Indicator = models.FloatField(null=True)
    Wave_4_Email_Open = models.FloatField(null=True)
    Wave_4_Email_Click = models.FloatField(null=True)
    Wave_1_Social = models.BigIntegerField(null=True)
    Wave_1_Social_Creative_Code = models.FloatField(null=True)
    Wave_1_Social_Code_on_Mail = models.FloatField(null=True)
    Wave_2_Social = models.BigIntegerField(null=True)
    Wave_2_Social_Creative_Code = models.FloatField(null=True)
    Wave_2_Social_Code_on_Mail = models.FloatField(null=True)
    Wave_3_Social = models.BigIntegerField(null=True)
    Wave_3_Social_Creative_Code = models.FloatField(null=True)
    Wave_3_Social_Code_on_Mail = models.FloatField(null=True)
    Wave_4_Social = models.BigIntegerField(null=True)
    Wave_4_Social_Creative_Code = models.FloatField(null=True)
    Wave_4_Social_Code_on_Mail = models.FloatField(null=True)
    New_Customer_Match = models.BigIntegerField(null=True)
    Individual_Enterprise_ID = models.FloatField(null=True)
    CE_Match_Level = models.CharField(max_length=300,null=True)