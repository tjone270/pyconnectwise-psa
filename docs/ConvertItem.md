# ConvertItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**phase** | [**ProjectPhaseReference**](ProjectPhaseReference.md) |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**record_type** | **str** |  | 
**wbs_code** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.convert_item import ConvertItem

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertItem from a JSON string
convert_item_instance = ConvertItem.from_json(json)
# print the JSON string representation of the object
print ConvertItem.to_json()

# convert the object into a dict
convert_item_dict = convert_item_instance.to_dict()
# create an instance of ConvertItem from a dict
convert_item_form_dict = convert_item.from_dict(convert_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


