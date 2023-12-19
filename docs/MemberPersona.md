# MemberPersona


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**job_role_percentage** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**name** | **str** |  | [optional] 
**persona_id** | **int** |  | 

## Example

```python
from connectwise_psa.models.member_persona import MemberPersona

# TODO update the JSON string below
json = "{}"
# create an instance of MemberPersona from a JSON string
member_persona_instance = MemberPersona.from_json(json)
# print the JSON string representation of the object
print MemberPersona.to_json()

# convert the object into a dict
member_persona_dict = member_persona_instance.to_dict()
# create an instance of MemberPersona from a dict
member_persona_form_dict = member_persona.from_dict(member_persona_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


