# RmaStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**closed_flag** | **bool** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**email_template** | [**RmaStatusEmailTemplateReference**](RmaStatusEmailTemplateReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**sort_order** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.rma_status import RmaStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RmaStatus from a JSON string
rma_status_instance = RmaStatus.from_json(json)
# print the JSON string representation of the object
print RmaStatus.to_json()

# convert the object into a dict
rma_status_dict = rma_status_instance.to_dict()
# create an instance of RmaStatus from a dict
rma_status_form_dict = rma_status.from_dict(rma_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


