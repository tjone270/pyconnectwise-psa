# ServiceItemReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_item_reference import ServiceItemReference

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceItemReference from a JSON string
service_item_reference_instance = ServiceItemReference.from_json(json)
# print the JSON string representation of the object
print ServiceItemReference.to_json()

# convert the object into a dict
service_item_reference_dict = service_item_reference_instance.to_dict()
# create an instance of ServiceItemReference from a dict
service_item_reference_form_dict = service_item_reference.from_dict(service_item_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


