# MemberDeactivationSalesActivity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**re_assign_to_member** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.member_deactivation_sales_activity import MemberDeactivationSalesActivity

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDeactivationSalesActivity from a JSON string
member_deactivation_sales_activity_instance = MemberDeactivationSalesActivity.from_json(json)
# print the JSON string representation of the object
print MemberDeactivationSalesActivity.to_json()

# convert the object into a dict
member_deactivation_sales_activity_dict = member_deactivation_sales_activity_instance.to_dict()
# create an instance of MemberDeactivationSalesActivity from a dict
member_deactivation_sales_activity_form_dict = member_deactivation_sales_activity.from_dict(member_deactivation_sales_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


