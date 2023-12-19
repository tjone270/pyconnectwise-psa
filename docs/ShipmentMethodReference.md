# ShipmentMethodReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.shipment_method_reference import ShipmentMethodReference

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentMethodReference from a JSON string
shipment_method_reference_instance = ShipmentMethodReference.from_json(json)
# print the JSON string representation of the object
print ShipmentMethodReference.to_json()

# convert the object into a dict
shipment_method_reference_dict = shipment_method_reference_instance.to_dict()
# create an instance of ShipmentMethodReference from a dict
shipment_method_reference_form_dict = shipment_method_reference.from_dict(shipment_method_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


