# CertificationReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.certification_reference import CertificationReference

# TODO update the JSON string below
json = "{}"
# create an instance of CertificationReference from a JSON string
certification_reference_instance = CertificationReference.from_json(json)
# print the JSON string representation of the object
print CertificationReference.to_json()

# convert the object into a dict
certification_reference_dict = certification_reference_instance.to_dict()
# create an instance of CertificationReference from a dict
certification_reference_form_dict = certification_reference.from_dict(certification_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


