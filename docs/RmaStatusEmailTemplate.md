# RmaStatusEmailTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**body** | **str** |  | 
**copy_sender_flag** | **bool** |  | [optional] 
**email_address** | **str** |  Max length: 100; | [optional] 
**first_name** | **str** |  Max length: 100; | [optional] 
**id** | **int** |  | [optional] 
**last_name** | **str** |  Max length: 100; | [optional] 
**status** | [**RmaStatusReference**](RmaStatusReference.md) |  | [optional] 
**subject** | **str** |  Max length: 200; | 
**use_sender_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.rma_status_email_template import RmaStatusEmailTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of RmaStatusEmailTemplate from a JSON string
rma_status_email_template_instance = RmaStatusEmailTemplate.from_json(json)
# print the JSON string representation of the object
print RmaStatusEmailTemplate.to_json()

# convert the object into a dict
rma_status_email_template_dict = rma_status_email_template_instance.to_dict()
# create an instance of RmaStatusEmailTemplate from a dict
rma_status_email_template_form_dict = rma_status_email_template.from_dict(rma_status_email_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


