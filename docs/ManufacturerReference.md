# ManufacturerReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.manufacturer_reference import ManufacturerReference

# TODO update the JSON string below
json = "{}"
# create an instance of ManufacturerReference from a JSON string
manufacturer_reference_instance = ManufacturerReference.from_json(json)
# print the JSON string representation of the object
print ManufacturerReference.to_json()

# convert the object into a dict
manufacturer_reference_dict = manufacturer_reference_instance.to_dict()
# create an instance of ManufacturerReference from a dict
manufacturer_reference_form_dict = manufacturer_reference.from_dict(manufacturer_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


