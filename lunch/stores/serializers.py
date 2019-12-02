from rest_framework import serializers
from stores.models import Store

class StoreSerializers(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Store
        # fields = '__all__'
        fields = ('id', 'name', 'notes')
        