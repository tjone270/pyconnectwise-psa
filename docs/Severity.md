# Severity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**description** | **str** |  Max length: 200; | 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.severity import Severity

# TODO update the JSON string below
json = "{}"
# create an instance of Severity from a JSON string
severity_instance = Severity.from_json(json)
# print the JSON string representation of the object
print Severity.to_json()

# convert the object into a dict
severity_dict = severity_instance.to_dict()
# create an instance of Severity from a dict
severity_form_dict = severity.from_dict(severity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


