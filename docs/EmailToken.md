# EmailToken


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_flag** | **bool** |  | [optional] 
**agreement_flag** | **bool** |  | [optional] 
**company_flag** | **bool** |  | [optional] 
**config_flag** | **bool** |  | [optional] 
**contact_flag** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**invoice_flag** | **bool** |  | [optional] 
**portal_password_flag** | **bool** |  | [optional] 
**purchase_order_flag** | **bool** |  | [optional] 
**purchase_order_status_flag** | **bool** |  | [optional] 
**rma_flag** | **bool** |  | [optional] 
**sales_flag** | **bool** |  | [optional] 
**service_flag** | **bool** |  | [optional] 
**token** | **str** |  | [optional] 
**tracks_flag** | **bool** |  | [optional] 
**workflow_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.email_token import EmailToken

# TODO update the JSON string below
json = "{}"
# create an instance of EmailToken from a JSON string
email_token_instance = EmailToken.from_json(json)
# print the JSON string representation of the object
print EmailToken.to_json()

# convert the object into a dict
email_token_dict = email_token_instance.to_dict()
# create an instance of EmailToken from a dict
email_token_form_dict = email_token.from_dict(email_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


