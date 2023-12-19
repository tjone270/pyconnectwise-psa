# GLPath


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**database_name** | **str** |  Max length: 100; | [optional] 
**id** | **int** |  | [optional] 
**last_payment_sync** | **datetime** |  | [optional] 
**last_payment_sync_by** | [**MemberReference**](MemberReference.md) |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**path** | **str** |  Max length: 255; | [optional] 
**sql_server_name** | **str** |  Max length: 255; | [optional] 

## Example

```python
from connectwise_psa.models.gl_path import GLPath

# TODO update the JSON string below
json = "{}"
# create an instance of GLPath from a JSON string
gl_path_instance = GLPath.from_json(json)
# print the JSON string representation of the object
print GLPath.to_json()

# convert the object into a dict
gl_path_dict = gl_path_instance.to_dict()
# create an instance of GLPath from a dict
gl_path_form_dict = gl_path.from_dict(gl_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


