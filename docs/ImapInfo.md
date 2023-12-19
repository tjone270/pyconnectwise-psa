# ImapInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**email_connector** | [**EmailConnectorReference**](EmailConnectorReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.imap_info import ImapInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ImapInfo from a JSON string
imap_info_instance = ImapInfo.from_json(json)
# print the JSON string representation of the object
print ImapInfo.to_json()

# convert the object into a dict
imap_info_dict = imap_info_instance.to_dict()
# create an instance of ImapInfo from a dict
imap_info_form_dict = imap_info.from_dict(imap_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


