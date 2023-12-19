# IntegratorLoginReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.integrator_login_reference import IntegratorLoginReference

# TODO update the JSON string below
json = "{}"
# create an instance of IntegratorLoginReference from a JSON string
integrator_login_reference_instance = IntegratorLoginReference.from_json(json)
# print the JSON string representation of the object
print IntegratorLoginReference.to_json()

# convert the object into a dict
integrator_login_reference_dict = integrator_login_reference_instance.to_dict()
# create an instance of IntegratorLoginReference from a dict
integrator_login_reference_form_dict = integrator_login_reference.from_dict(integrator_login_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


