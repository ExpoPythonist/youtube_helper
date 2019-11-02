`YOUTUBE HELPER API`



# Sample Request API:

## base_url = 127.0.0.1:8000
### URL: base_url+/api/v1/processor

Request Body:
```json
{
	"city":"Dhaka",
	"state":"Bangladesh",
	"text":"affordable mortgage",
	"url":"https://idlc.com/mbr/article.php"
}
```

Response Body:
```json
{
    "title": "Affordable Mortgage Dhaka Bangladesh",
    "description": "affordable mortgage Dhaka Bangladesh - https://idlc.com/mbr/article.php if you are looking for affordable mortgage Dhaka Bangladesh, then watch this video to learn everything to know about affordable mortgage Dhaka Bangladesh",
    "description_tags": "#Bangladesh, #Dhaka, #Dhaka Bangladesh, #mortgage, #mortgage Bangladesh, #Dhaka mortgage, #Dhaka mortgage Bangladesh, #affordable, #affordable Bangladesh, #affordable Dhaka, #affordable Dhaka Bangladesh, #affordable mortgage, #affordable mortgage Bangladesh, #affordable Dhaka mortgage, #affordable Dhaka mortgage Bangladesh",
    "tags": "Bangladesh, Dhaka, Dhaka Bangladesh, mortgage, mortgage Bangladesh, Dhaka mortgage, Dhaka mortgage Bangladesh, affordable, affordable Bangladesh, affordable Dhaka, affordable Dhaka Bangladesh, affordable mortgage, affordable mortgage Bangladesh, affordable Dhaka mortgage, affordable Dhaka mortgage Bangladesh"
}
```