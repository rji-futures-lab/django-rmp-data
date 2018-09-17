# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class RmpAccChem(models.Model):
    accchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    accident_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    quantity_lbs = models.DecimalField(max_digits=65535, decimal_places=65535)
    percent_weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    num_acc_flam = models.DecimalField(max_digits=65535, decimal_places=65535)
    cas = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_type = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'rmp_acc_chem'


class RmpAccFlam(models.Model):
    flammixchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    accchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_id = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'rmp_acc_flam'


class RmpChemCd(models.Model):
    chemical_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_name = models.CharField(max_length=-1)
    cas2 = models.CharField(max_length=-1, blank=True, null=True)
    threshold = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_type = models.BooleanField(blank=True, null=True)
    cbi_flag = models.BooleanField()
    chemical_owner = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rmp_chem_cd'


class RmpDeregCd(models.Model):
    dereg = models.DecimalField(max_digits=65535, decimal_places=65535)
    dereg_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_dereg_cd'


class RmpDochanCd(models.Model):
    dochan = models.CharField(max_length=-1)
    dochan_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_dochan_cd'


class RmpDoctypCd(models.Model):
    doctyp = models.CharField(max_length=-1)
    doctyp_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_doctyp_cd'


class RmpEventsCd(models.Model):
    events = models.CharField(max_length=-1)
    events_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_events_cd'


class RmpExecSumLen(models.Model):
    rmp_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    byte_count = models.DecimalField(max_digits=65535, decimal_places=65535)
    suspect_count = models.DecimalField(max_digits=65535, decimal_places=65535)
    line_count = models.DecimalField(max_digits=65535, decimal_places=65535)
    edited_yn = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'rmp_exec_sum_len'


class RmpLldescCd(models.Model):
    lldesc = models.CharField(max_length=-1)
    lldesc_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_lldesc_cd'


class RmpLlmethCd(models.Model):
    primary_key = models.DecimalField(max_digits=65535, decimal_places=65535)
    llmeth = models.CharField(max_length=-1)
    llmeth_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_llmeth_cd'


class RmpPhysCd(models.Model):
    phys = models.CharField(max_length=-1)
    phys_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_phys_cd'


class RmpPrevent2Chem(models.Model):
    primary_key = models.DecimalField(max_digits=65535, decimal_places=65535)
    prevent_2_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    procchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'rmp_prevent_2_chem'


class RmpPrevent3Chem(models.Model):
    primary_key = models.DecimalField(max_digits=65535, decimal_places=65535)
    prevent_3_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    procchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'rmp_prevent_3_chem'


class RmpProcChem(models.Model):
    procchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    process_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    quantity_lbs = models.DecimalField(max_digits=65535, decimal_places=65535)
    cbi_flag = models.BooleanField()
    num_alt_flam = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_alt_tox = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_prevent_2_chem = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_prevent_3_chem = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_proc_flam = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_worst_flam = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_worst_tox = models.DecimalField(max_digits=65535, decimal_places=65535)
    cas = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_type = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rmp_proc_chem'


class RmpProcFlam(models.Model):
    flammixchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    procchem_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    chemical_id = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'rmp_proc_flam'


class RmpProcNaics(models.Model):
    procnaics_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    process_id = models.DecimalField(max_digits=65535, decimal_places=65535)
    naics = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_prevent_2 = models.DecimalField(max_digits=65535, decimal_places=65535)
    num_prevent_3 = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'rmp_proc_naics'


class RmpRejectCd(models.Model):
    reject = models.CharField(max_length=-1)
    reject_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_reject_cd'


class RmpScenCd(models.Model):
    scen = models.CharField(max_length=-1)
    scen_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_scen_cd'


class RmpSubmitCd(models.Model):
    submit = models.CharField(max_length=-1)
    submit_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_submit_cd'


class RmpTopoCd(models.Model):
    topo = models.CharField(max_length=-1)
    topo_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_topo_cd'


class RmpWindCd(models.Model):
    wind = models.CharField(max_length=-1)
    wind_tr = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'rmp_wind_cd'
