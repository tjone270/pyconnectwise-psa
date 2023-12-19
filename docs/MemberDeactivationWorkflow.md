# MemberDeactivationWorkflow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**re_assign_to_member** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.member_deactivation_workflow import MemberDeactivationWorkflow

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDeactivationWorkflow from a JSON string
member_deactivation_workflow_instance = MemberDeactivationWorkflow.from_json(json)
# print the JSON string representation of the object
print MemberDeactivationWorkflow.to_json()

# convert the object into a dict
member_deactivation_workflow_dict = member_deactivation_workflow_instance.to_dict()
# create an instance of MemberDeactivationWorkflow from a dict
member_deactivation_workflow_form_dict = member_deactivation_workflow.from_dict(member_deactivation_workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


