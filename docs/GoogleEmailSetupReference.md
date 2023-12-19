# GoogleEmailSetupReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.google_email_setup_reference import GoogleEmailSetupReference

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleEmailSetupReference from a JSON string
google_email_setup_reference_instance = GoogleEmailSetupReference.from_json(json)
# print the JSON string representation of the object
print GoogleEmailSetupReference.to_json()

# convert the object into a dict
google_email_setup_reference_dict = google_email_setup_reference_instance.to_dict()
# create an instance of GoogleEmailSetupReference from a dict
google_email_setup_reference_form_dict = google_email_setup_reference.from_dict(google_email_setup_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


