Script for reformatting Dutch phone numbers
--------------------

This script checks if a potential phone number meets the criteria listed below and if it is (likely) a Dutch phone number, will transform the output to: `+31 20 123 4567` [recommended ITU-T international notation](https://www.itu.int/rec/T-REC-E.123-200102-I/en). <p>
This can be useful for cleaning up master data in an ERP/CRM/VoIP system. <p>


*Input criteria:*
- Characters: only digits, parenthesis "(",  ")", dashes "-" and spaces are allowed
- International: if a phone number starts with + or 00, it is only processed if it's +31 or 0031. If no country calling code is given, it's assumed to be a Dutch phone number (if it meets the other criteria)
- Length: 9 digits after 0031 or +31 or 10 digits without a country calling code, after all non-digit characters are removed


If any of the criteria is not matched, the result will be the original input. 

The output format will be:
`+31 20 123 4567` or  `+31 61 234 5678` for mobile phones

*Known exceptions:*<br>
There are valid phone numbers, such as emergency numbers (112) and service numbers (i.e. 0800-#### or 14 038) that are valid Dutch phone numbers but will not be reformatted. 

*Examples:*

```
Type:                                       Comment:                       Input:                      Output:
--------------------------------------------------------------------------------------------------------------
valid 1                             expected outcome              +31 20 123 4567              +31 20 123 4567
valid 2                               int, no spaces                 +31201234567              +31 20 123 4567
valid 3                                   int + zero              +31(0)201234567              +31 20 123 4567
valid 4                          int + zero + spaces           +31 (0)20 123 4567              +31 20 123 4567
valid 5                              as above + dash           +31 (0)20-123 4567              +31 20 123 4567
valid 6                           no int, has spaces                 020 123 4567              +31 20 123 4567
valid 7                              as above + dash                 020-123 4567              +31 20 123 4567
valid 8                no int, parentheses and space               (020) 123 4567              +31 20 123 4567
valid 9                              as above + dash               (020)-123 4567              +31 20 123 4567
valid 10                        no int mobile number                  06 12345678              +31 61 234 5678
valid 11                           int mobile number            +31 (0)6 12345678              +31 61 234 5678
valid 12                  int mobile number + dashes             +31 6 1234-5-678              +31 61 234 5678
invalid 1                                  too short                (020)-123 456                (020)-123 456
invalid 2                    int 0031, but too short                0031 123 4567                0031 123 4567
invalid 3                     int +31, but too short                 +31 123 4567                 +31 123 4567
invalid 4          int 0031, but too short with zero             0031 020 123 456             0031 020 123 456
invalid 5           int +31, but too short with zero              +31 020 123 456              +31 020 123 456
invalid 6                     phone number with text  020-123 4567 (ask for Mike)  020-123 4567 (ask for Mike)
invalid 7             international, foreign country                 +32 123 4567                 +32 123 4567
invalid 8             international, foreign country                 +32 123 4567                 +32 123 4567
known exception 1                   emergency number                          112                          112
known exception 2           city hall service number                       14 038                       14 038
known exception 3              police, non-emergency                    0900-8844                    0900-8844
```