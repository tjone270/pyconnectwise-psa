# RmaStatusReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.rma_status_reference import RmaStatusReference

# TODO update the JSON string below
json = "{}"
# create an instance of RmaStatusReference from a JSON string
rma_status_reference_instance = RmaStatusReference.from_json(json)
# print the JSON string representation of the object
print RmaStatusReference.to_json()

# convert the object into a dict
rma_status_reference_dict = rma_status_reference_instance.to_dict()
# create an instance of RmaStatusReference from a dict
rma_status_reference_form_dict = rma_status_reference.from_dict(rma_status_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


