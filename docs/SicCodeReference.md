# SicCodeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.sic_code_reference import SicCodeReference

# TODO update the JSON string below
json = "{}"
# create an instance of SicCodeReference from a JSON string
sic_code_reference_instance = SicCodeReference.from_json(json)
# print the JSON string representation of the object
print SicCodeReference.to_json()

# convert the object into a dict
sic_code_reference_dict = sic_code_reference_instance.to_dict()
# create an instance of SicCodeReference from a dict
sic_code_reference_form_dict = sic_code_reference.from_dict(sic_code_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


