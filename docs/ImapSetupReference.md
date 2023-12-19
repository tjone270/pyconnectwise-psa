# ImapSetupReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.imap_setup_reference import ImapSetupReference

# TODO update the JSON string below
json = "{}"
# create an instance of ImapSetupReference from a JSON string
imap_setup_reference_instance = ImapSetupReference.from_json(json)
# print the JSON string representation of the object
print ImapSetupReference.to_json()

# convert the object into a dict
imap_setup_reference_dict = imap_setup_reference_instance.to_dict()
# create an instance of ImapSetupReference from a dict
imap_setup_reference_form_dict = imap_setup_reference.from_dict(imap_setup_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


