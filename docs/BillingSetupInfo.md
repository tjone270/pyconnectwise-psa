# BillingSetupInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**remit_name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.billing_setup_info import BillingSetupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BillingSetupInfo from a JSON string
billing_setup_info_instance = BillingSetupInfo.from_json(json)
# print the JSON string representation of the object
print BillingSetupInfo.to_json()

# convert the object into a dict
billing_setup_info_dict = billing_setup_info_instance.to_dict()
# create an instance of BillingSetupInfo from a dict
billing_setup_info_form_dict = billing_setup_info.from_dict(billing_setup_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


