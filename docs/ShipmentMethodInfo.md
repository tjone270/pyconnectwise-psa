# ShipmentMethodInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.shipment_method_info import ShipmentMethodInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentMethodInfo from a JSON string
shipment_method_info_instance = ShipmentMethodInfo.from_json(json)
# print the JSON string representation of the object
print ShipmentMethodInfo.to_json()

# convert the object into a dict
shipment_method_info_dict = shipment_method_info_instance.to_dict()
# create an instance of ShipmentMethodInfo from a dict
shipment_method_info_form_dict = shipment_method_info.from_dict(shipment_method_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


