# EmailConnectorParsingStyleReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.email_connector_parsing_style_reference import EmailConnectorParsingStyleReference

# TODO update the JSON string below
json = "{}"
# create an instance of EmailConnectorParsingStyleReference from a JSON string
email_connector_parsing_style_reference_instance = EmailConnectorParsingStyleReference.from_json(json)
# print the JSON string representation of the object
print EmailConnectorParsingStyleReference.to_json()

# convert the object into a dict
email_connector_parsing_style_reference_dict = email_connector_parsing_style_reference_instance.to_dict()
# create an instance of EmailConnectorParsingStyleReference from a dict
email_connector_parsing_style_reference_form_dict = email_connector_parsing_style_reference.from_dict(email_connector_parsing_style_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


