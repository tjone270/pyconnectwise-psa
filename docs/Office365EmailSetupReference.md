# Office365EmailSetupReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.office365_email_setup_reference import Office365EmailSetupReference

# TODO update the JSON string below
json = "{}"
# create an instance of Office365EmailSetupReference from a JSON string
office365_email_setup_reference_instance = Office365EmailSetupReference.from_json(json)
# print the JSON string representation of the object
print Office365EmailSetupReference.to_json()

# convert the object into a dict
office365_email_setup_reference_dict = office365_email_setup_reference_instance.to_dict()
# create an instance of Office365EmailSetupReference from a dict
office365_email_setup_reference_form_dict = office365_email_setup_reference.from_dict(office365_email_setup_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


