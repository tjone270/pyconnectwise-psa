# GoogleEmailSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**client_id** | **str** |  Max length: 200; | [optional] 
**email_connector** | [**EmailConnectorReference**](EmailConnectorReference.md) |  | [optional] 
**failed_folder** | **str** |  Max length: 40; | 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**inbox_folder** | **str** |  Max length: 40; | 
**name** | **str** |  Max length: 200; | 
**private_key** | **str** |  Max length: 4000; | [optional] 
**processed_folder** | **str** |  Max length: 40; | 
**username** | **str** |  Max length: 100; | 

## Example

```python
from connectwise_psa.models.google_email_setup import GoogleEmailSetup

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleEmailSetup from a JSON string
google_email_setup_instance = GoogleEmailSetup.from_json(json)
# print the JSON string representation of the object
print GoogleEmailSetup.to_json()

# convert the object into a dict
google_email_setup_dict = google_email_setup_instance.to_dict()
# create an instance of GoogleEmailSetup from a dict
google_email_setup_form_dict = google_email_setup.from_dict(google_email_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


