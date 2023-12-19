# Certification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.certification import Certification

# TODO update the JSON string below
json = "{}"
# create an instance of Certification from a JSON string
certification_instance = Certification.from_json(json)
# print the JSON string representation of the object
print Certification.to_json()

# convert the object into a dict
certification_dict = certification_instance.to_dict()
# create an instance of Certification from a dict
certification_form_dict = certification.from_dict(certification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


