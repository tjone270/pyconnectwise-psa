# BillingStatusInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.billing_status_info import BillingStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BillingStatusInfo from a JSON string
billing_status_info_instance = BillingStatusInfo.from_json(json)
# print the JSON string representation of the object
print BillingStatusInfo.to_json()

# convert the object into a dict
billing_status_info_dict = billing_status_info_instance.to_dict()
# create an instance of BillingStatusInfo from a dict
billing_status_info_form_dict = billing_status_info.from_dict(billing_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


