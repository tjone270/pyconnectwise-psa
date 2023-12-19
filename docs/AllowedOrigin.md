# AllowedOrigin


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  Max length: 2000; | 
**id** | **int** |  | [optional] 
**last_update_utc** | **datetime** |  | [optional] 
**origin** | **str** |  Max length: 2000; | 
**updated_by** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.allowed_origin import AllowedOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedOrigin from a JSON string
allowed_origin_instance = AllowedOrigin.from_json(json)
# print the JSON string representation of the object
print AllowedOrigin.to_json()

# convert the object into a dict
allowed_origin_dict = allowed_origin_instance.to_dict()
# create an instance of AllowedOrigin from a dict
allowed_origin_form_dict = allowed_origin.from_dict(allowed_origin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


