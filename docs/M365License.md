# M365License


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.m365_license import M365License

# TODO update the JSON string below
json = "{}"
# create an instance of M365License from a JSON string
m365_license_instance = M365License.from_json(json)
# print the JSON string representation of the object
print M365License.to_json()

# convert the object into a dict
m365_license_dict = m365_license_instance.to_dict()
# create an instance of M365License from a dict
m365_license_form_dict = m365_license.from_dict(m365_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


