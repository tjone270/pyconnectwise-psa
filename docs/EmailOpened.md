# EmailOpened


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **int** |  | [optional] 
**contact_id** | **int** |  | 
**date_opened** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.email_opened import EmailOpened

# TODO update the JSON string below
json = "{}"
# create an instance of EmailOpened from a JSON string
email_opened_instance = EmailOpened.from_json(json)
# print the JSON string representation of the object
print EmailOpened.to_json()

# convert the object into a dict
email_opened_dict = email_opened_instance.to_dict()
# create an instance of EmailOpened from a dict
email_opened_form_dict = email_opened.from_dict(email_opened_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


