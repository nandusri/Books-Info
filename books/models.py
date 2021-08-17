from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    author = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class CustomerMaster(models.Model):
    '''
    Name: CustomerMaster
    Table Name: customer_master
    Type: django.db.models
    Structure:
        1. id<Integer>: ID of Record. [Primary Key]
        2. customer_class_details<Varchar[255]>: customer_class_details field.
        3. customer_class_desc<Varchar[255]>: customer_class_desc field.
        4. customer_classification<Varchar[255]>: customer_classification field.
    '''
    id = models.AutoField(primary_key=True)
    customer_class_details = models.CharField(max_length=255)
    customer_class_desc = models.CharField(max_length=255)
    customer_classification = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'node_customer_master'

class Depot(models.Model):
    '''
    Name: Depot
    Table Name: depot
    Type: django.db.models
    Structure:
        1. id<Integer>: ID of Record. [Primary Key]
        2. depot_code<Varchar[255]>: depot_code field.
        3. depot_desc<Varchar[255]>: depot_desc field.
        4. created_on<Timestamp>: created_on field.
        5. updated_on<Timestamp>: updated_on field.
    '''
    id = models.AutoField(primary_key=True)
    depot_code = models.CharField(max_length=255)
    depot_desc = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'node_depot'

class Address(models.Model):
    '''
    Name: Address
    Table Name: address
    Type: django.db.models
    Structure:
        1. id<Integer>: ID of Record. [Primary Key]
        2. city_code<Varchar[255]>: city_code field.
        3. city_desc<Varchar[255]>: city_desc field.
        4. taluka_code<Varchar[255]>: taluka_code field.
        5. taluka_desc<Varchar[255]>: taluka_desc field.
        6. district_code<Varchar[255]>: district_code field.
        7. district_desc<Varchar[255]>: district_desc field.
        8. region_code<Varchar[255]>: region_code field.
        9. region_desc<Varchar[255]>: region_desc field.
        10. state_code<Varchar[255]>: state_code field.
        11. state_desc<Varchar[255]>: state_desc field.
        12. zone_code<Varchar[255]>: zone_code field.
        13. zone_desc<Varchar[255]>: zone_desc field.
        14. zone_geo_code<Varchar[255]>: zone_geo_code field.
        15. country<Varchar[255]>: country field.
        16. postal_code<Varchar[255]>: postal_code field.
        17. address1<Varchar[255]>: address1 field.
        18. address2<Varchar[255]>: address2 field.
        19. lat<Varchar[255]>: lat field.
        20. lng<Varchar[255]>: lng field.
    '''
    id = models.AutoField(primary_key=True)
    city_code = models.CharField(max_length=255)
    city_desc = models.CharField(max_length=255)
    taluka_code = models.CharField(max_length=255)
    taluka_desc = models.CharField(max_length=255)
    district_code = models.CharField(max_length=255)
    district_desc = models.CharField(max_length=255)
    region_code = models.CharField(max_length=255)
    region_desc = models.CharField(max_length=255)
    state_code = models.CharField(max_length=255)
    state_desc = models.CharField(max_length=255)
    zone_code = models.CharField(max_length=255)
    zone_desc = models.CharField(max_length=255)
    zone_geo_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)  # Can reduce length
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)  # Can use float
    lng = models.CharField(max_length=255)  # Can use float

    class Meta:
        db_table = 'node_address'


class Customer(models.Model):
    '''
    Name: Customer
    Table Name: customer
    Type: django.db.models
    Structure:
        1. id<Integer>: ID of Record. [Primary Key]
        2. address_id<Varchar[255]>: ForeignKey associated to the id of address in Address model.
        3. cust_master_id<Varchar[255]>: cust_master_id field.
        4. depot_id<Varchar[255]>: depot_id field.
        5. created_by<Varchar[255]>: created_by field.
        6. created_on<Varchar[255]>: created_on field.
        7. modified_on<Varchar[255]>: modified_on field.
        8. scenario<Varchar[255]>: scenario field.
        9. status<Varchar[255]>: status field.
        10. exception_flag<Varchar[255]>: exception_flag field.
        11. exception_msg<Varchar[255]>: exception_msg field.
        12. validated_by<Varchar[255]>: validated_by field.
    '''
    id = models.AutoField(primary_key=True)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    cust_master_id = models.ForeignKey(CustomerMaster, on_delete=models.CASCADE)
    depot_id = models.ForeignKey(Depot, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True) # Can use timestamp
    modified_on = models.CharField(max_length=255) # Can use timestamp
    scenario = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    exception_flag = models.CharField(max_length=255)
    exception_msg = models.CharField(max_length=255)
    validated_by = models.CharField(max_length=255)

    class Meta:
        db_table = 'node_customer'

class Facility(models.Model):
    '''
    Name: Facility
    Table Name: facility
    Type: django.db.models
    Structure:
        1. id<Integer>: ID of Record. [Primary Key]
        2. address_id<Varchar[255]>: ForeignKey associated to the id of address in Address model.
        3. depot_id<Varchar[255]>: ForeignKey associated to the id of depot in Depot model.
        4. facility<Varchar[255]>: facility field.
        5. facility_code<Varchar[255]>: facility_code field.
        6. facility_desc<Varchar[255]>: facility_desc field.
        7. facility_processing<Varchar[255]>: facility_processing field.
        8. facility_sub_type<Varchar[255]>: facility_sub_type field.
        9. fixed_cost<Varchar[255]>: fixed_cost field.
        10. handling_charge_hook<Varchar[255]>: handling_charge_hook field.
        11. handling_charge_non_hook<Varchar[255]>: handling_charge_non_hook field.
        12. capacity<Varchar[255]>: capacity field.
        13. created_on<Varchar[255]>: created_on field.
        14. modified_on<Varchar[255]>: modified_on field.
        15. scenario<Varchar[255]>: scenario field.
        16. status<Varchar[255]>: status field.
        17. exception_flag<Varchar[255]>: exception_flag field.
        18. exception_msg<Varchar[255]>: exception_msg field.
        19. validated_by<Varchar[255]>: validated_by field.
        20. mfg_code<Varchar[255]>: mfg_code field.
        21. plant_category<Varchar[255]>: plant_category field.
        22. godown_location<Varchar[255]>: godown_location field.
        23. i2_code<Varchar[255]>: i2_code field.
    '''
    id = models.AutoField(primary_key=True)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    depot_id = models.ForeignKey(Depot, on_delete=models.CASCADE)
    facility = models.CharField(max_length=255)
    facility_code = models.CharField(max_length=255)
    facility_desc = models.CharField(max_length=255)
    facility_processing = models.CharField(max_length=255)
    facility_sub_type = models.CharField(max_length=255)
    fixed_cost = models.CharField(max_length=255) # Can use IntegerField
    handling_charge_hook = models.CharField(max_length=255)
    handling_charge_non_hook = models.CharField(max_length=255)
    capacity = models.CharField(max_length=255) # Can use IntegerField
    created_on = models.DateTimeField(auto_now_add=True) # Can use timestamp
    modified_on = models.CharField(max_length=255) # Can use timestamp
    scenario = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    exception_flag = models.CharField(max_length=255)
    exception_msg = models.CharField(max_length=255)
    validated_by = models.CharField(max_length=255)
    mfg_code = models.CharField(max_length=255)
    plant_category = models.CharField(max_length=255)
    godown_location = models.CharField(max_length=255)
    i2_code = models.CharField(max_length=255)

    class Meta:
        db_table = 'node_facility'