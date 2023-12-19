# SLAInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.sla_info import SLAInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SLAInfo from a JSON string
sla_info_instance = SLAInfo.from_json(json)
# print the JSON string representation of the object
print SLAInfo.to_json()

# convert the object into a dict
sla_info_dict = sla_info_instance.to_dict()
# create an instance of SLAInfo from a dict
sla_info_form_dict = sla_info.from_dict(sla_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


