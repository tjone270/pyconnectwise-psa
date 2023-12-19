# EmailConnectorInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**imap_setup** | [**ImapSetupReference**](ImapSetupReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.email_connector_info import EmailConnectorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EmailConnectorInfo from a JSON string
email_connector_info_instance = EmailConnectorInfo.from_json(json)
# print the JSON string representation of the object
print EmailConnectorInfo.to_json()

# convert the object into a dict
email_connector_info_dict = email_connector_info_instance.to_dict()
# create an instance of EmailConnectorInfo from a dict
email_connector_info_form_dict = email_connector_info.from_dict(email_connector_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


