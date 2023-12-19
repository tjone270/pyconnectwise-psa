# Imap


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**email_connector** | [**EmailConnectorReference**](EmailConnectorReference.md) |  | [optional] 
**failed_folder** | **str** |  Max length: 40; | 
**id** | **int** |  | [optional] 
**imap_name** | **str** |  Max length: 40; | 
**name** | **str** |  Max length: 200; | 
**password** | **str** |  Max length: 80; | [optional] 
**port** | **int** |  | 
**processed_name** | **str** |  Max length: 40; | 
**server** | **str** |  Max length: 200; | 
**ssl_flag** | **bool** |  | [optional] 
**user_name** | **str** |  Max length: 80; | 

## Example

```python
from connectwise_psa.models.imap import Imap

# TODO update the JSON string below
json = "{}"
# create an instance of Imap from a JSON string
imap_instance = Imap.from_json(json)
# print the JSON string representation of the object
print Imap.to_json()

# convert the object into a dict
imap_dict = imap_instance.to_dict()
# create an instance of Imap from a dict
imap_form_dict = imap.from_dict(imap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


