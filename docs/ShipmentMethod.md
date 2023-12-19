# ShipmentMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**tracking_url** | **str** |  Max length: 200; | [optional] 

## Example

```python
from connectwise_psa.models.shipment_method import ShipmentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentMethod from a JSON string
shipment_method_instance = ShipmentMethod.from_json(json)
# print the JSON string representation of the object
print ShipmentMethod.to_json()

# convert the object into a dict
shipment_method_dict = shipment_method_instance.to_dict()
# create an instance of ShipmentMethod from a dict
shipment_method_form_dict = shipment_method.from_dict(shipment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


