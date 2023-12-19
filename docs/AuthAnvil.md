# AuthAnvil


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**server_location_url** | **str** |  | 
**site_id** | **int** |  | 

## Example

```python
from connectwise_psa.models.auth_anvil import AuthAnvil

# TODO update the JSON string below
json = "{}"
# create an instance of AuthAnvil from a JSON string
auth_anvil_instance = AuthAnvil.from_json(json)
# print the JSON string representation of the object
print AuthAnvil.to_json()

# convert the object into a dict
auth_anvil_dict = auth_anvil_instance.to_dict()
# create an instance of AuthAnvil from a dict
auth_anvil_form_dict = auth_anvil.from_dict(auth_anvil_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


