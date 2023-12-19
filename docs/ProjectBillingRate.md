# ProjectBillingRate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**activity_class_rec_id** | **int** |  | [optional] 
**hourly_rate** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**member_rec_id** | **int** |  | [optional] 
**project_rec_id** | **int** |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.project_billing_rate import ProjectBillingRate

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBillingRate from a JSON string
project_billing_rate_instance = ProjectBillingRate.from_json(json)
# print the JSON string representation of the object
print ProjectBillingRate.to_json()

# convert the object into a dict
project_billing_rate_dict = project_billing_rate_instance.to_dict()
# create an instance of ProjectBillingRate from a dict
project_billing_rate_form_dict = project_billing_rate.from_dict(project_billing_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


