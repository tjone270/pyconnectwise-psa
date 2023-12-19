# EmailConnectorReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.email_connector_reference import EmailConnectorReference

# TODO update the JSON string below
json = "{}"
# create an instance of EmailConnectorReference from a JSON string
email_connector_reference_instance = EmailConnectorReference.from_json(json)
# print the JSON string representation of the object
print EmailConnectorReference.to_json()

# convert the object into a dict
email_connector_reference_dict = email_connector_reference_instance.to_dict()
# create an instance of EmailConnectorReference from a dict
email_connector_reference_form_dict = email_connector_reference.from_dict(email_connector_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


