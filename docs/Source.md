# Source


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**date_entered** | **datetime** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**entered_by** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.source import Source

# TODO update the JSON string below
json = "{}"
# create an instance of Source from a JSON string
source_instance = Source.from_json(json)
# print the JSON string representation of the object
print Source.to_json()

# convert the object into a dict
source_dict = source_instance.to_dict()
# create an instance of Source from a dict
source_form_dict = source.from_dict(source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


