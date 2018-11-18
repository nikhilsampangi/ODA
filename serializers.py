from rest_framework import serializers
from diseaseidentification.models import latlng,tips,General_Medicine,Stock_availability,Medical_shop,Blood_Bank,Blood_avail

class BloodBankSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blood_Bank
        fields=('BB_id','BB_name','Lat','Long')

class BloodavailSerializer(serializers.ModelSerializer):
    BB_id=BloodBankSerializer()
    class Meta:
        model=Blood_avail
        fields=('Blood_grp','Availability','BB_id')

    def create(self, validated_data):
        blood_codes = validated_data.pop('BB_id')
        blood = Blood_Bank.objects.create(**blood_codes)
        detail = Blood_avail.objects.create(BB_id=blood,**validated_data)
        return detail



class MedicalshopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medical_shop
        fields=('shop_id','shop_name','Lattitude','Longitude')

class StockavailabilitySerializer(serializers.ModelSerializer):
    shop_id=MedicalshopSerializer()
    class Meta:
        model=Stock_availability
        fields=('Med_id','Medicine_name','Stock','shop_id')

    def create(self, validated_data):
        blood_codes = validated_data.pop('shop_id')
        blood = Medical_shop.objects.create(**blood_codes)
        detail = Stock_availability.objects.create(shop_id=blood,**validated_data)
        return detail
