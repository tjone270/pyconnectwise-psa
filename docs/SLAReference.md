# SLAReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.sla_reference import SLAReference

# TODO update the JSON string below
json = "{}"
# create an instance of SLAReference from a JSON string
sla_reference_instance = SLAReference.from_json(json)
# print the JSON string representation of the object
print SLAReference.to_json()

# convert the object into a dict
sla_reference_dict = sla_reference_instance.to_dict()
# create an instance of SLAReference from a dict
sla_reference_form_dict = sla_reference.from_dict(sla_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


