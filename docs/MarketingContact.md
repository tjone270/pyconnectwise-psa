# MarketingContact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**group_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**note** | **str** |  Max length: 50; | [optional] 
**unsubscribe_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.marketing_contact import MarketingContact

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingContact from a JSON string
marketing_contact_instance = MarketingContact.from_json(json)
# print the JSON string representation of the object
print MarketingContact.to_json()

# convert the object into a dict
marketing_contact_dict = marketing_contact_instance.to_dict()
# create an instance of MarketingContact from a dict
marketing_contact_form_dict = marketing_contact.from_dict(marketing_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


