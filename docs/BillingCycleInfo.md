# BillingCycleInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.billing_cycle_info import BillingCycleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BillingCycleInfo from a JSON string
billing_cycle_info_instance = BillingCycleInfo.from_json(json)
# print the JSON string representation of the object
print BillingCycleInfo.to_json()

# convert the object into a dict
billing_cycle_info_dict = billing_cycle_info_instance.to_dict()
# create an instance of BillingCycleInfo from a dict
billing_cycle_info_form_dict = billing_cycle_info.from_dict(billing_cycle_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


