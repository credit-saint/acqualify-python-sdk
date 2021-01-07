# swagger_client.ApplicantsApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lookup_applicant**](ApplicantsApi.md#lookup_applicant) | **GET** /lookup-applicant | Returns public information about a loan applicant


# **lookup_applicant**
> lookup_applicant(first_name, last_name, addr_line1, city, state, zip, dob, addr_line2=addr_line2, email=email, phone_number=phone_number, loan_amount=loan_amount)

Returns public information about a loan applicant

See publicly available financial info about a loan applicant including credit score, based on name, address and date of birth

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ApplicantsApi(swagger_client.ApiClient(configuration))
first_name = 'first_name_example' # str | Applicant first name
last_name = 'last_name_example' # str | Applicant last name
addr_line1 = 'addr_line1_example' # str | Address line 1
city = 'city_example' # str | City
state = 'state_example' # str | State (2-letter abbreviation)
zip = 789 # int | Zip code
dob = 'dob_example' # str | Date of birth (MM/DD/YYYY)
addr_line2 = 'addr_line2_example' # str | Address line 2 (optional)
email = 'email_example' # str | Applicant email address (optional)
phone_number = 'phone_number_example' # str | Phone number (optional)
loan_amount = 'loan_amount_example' # str | Loan amount (optional)

try:
    # Returns public information about a loan applicant
    api_instance.lookup_applicant(first_name, last_name, addr_line1, city, state, zip, dob, addr_line2=addr_line2, email=email, phone_number=phone_number, loan_amount=loan_amount)
except ApiException as e:
    print("Exception when calling ApplicantsApi->lookup_applicant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**| Applicant first name | 
 **last_name** | **str**| Applicant last name | 
 **addr_line1** | **str**| Address line 1 | 
 **city** | **str**| City | 
 **state** | **str**| State (2-letter abbreviation) | 
 **zip** | **int**| Zip code | 
 **dob** | **str**| Date of birth (MM/DD/YYYY) | 
 **addr_line2** | **str**| Address line 2 | [optional] 
 **email** | **str**| Applicant email address | [optional] 
 **phone_number** | **str**| Phone number | [optional] 
 **loan_amount** | **str**| Loan amount | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

