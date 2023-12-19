# IntegratorTag


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**text** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.integrator_tag import IntegratorTag

# TODO update the JSON string below
json = "{}"
# create an instance of IntegratorTag from a JSON string
integrator_tag_instance = IntegratorTag.from_json(json)
# print the JSON string representation of the object
print IntegratorTag.to_json()

# convert the object into a dict
integrator_tag_dict = integrator_tag_instance.to_dict()
# create an instance of IntegratorTag from a dict
integrator_tag_form_dict = integrator_tag.from_dict(integrator_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


