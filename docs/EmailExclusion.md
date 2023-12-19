# EmailExclusion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  Max length: 100; | 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.email_exclusion import EmailExclusion

# TODO update the JSON string below
json = "{}"
# create an instance of EmailExclusion from a JSON string
email_exclusion_instance = EmailExclusion.from_json(json)
# print the JSON string representation of the object
print EmailExclusion.to_json()

# convert the object into a dict
email_exclusion_dict = email_exclusion_instance.to_dict()
# create an instance of EmailExclusion from a dict
email_exclusion_form_dict = email_exclusion.from_dict(email_exclusion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


