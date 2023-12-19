# MemberAccrual


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**accrual_type** | **str** |  | 
**hours** | **float** |  | 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**reason** | **str** |  | 
**year** | **int** |  | 

## Example

```python
from connectwise_psa.models.member_accrual import MemberAccrual

# TODO update the JSON string below
json = "{}"
# create an instance of MemberAccrual from a JSON string
member_accrual_instance = MemberAccrual.from_json(json)
# print the JSON string representation of the object
print MemberAccrual.to_json()

# convert the object into a dict
member_accrual_dict = member_accrual_instance.to_dict()
# create an instance of MemberAccrual from a dict
member_accrual_form_dict = member_accrual.from_dict(member_accrual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


