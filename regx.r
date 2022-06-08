three_digits <- DGT %R% DGT %R% DGT
four_digits <- three_digits %R% DGT
separator <- char_class("-.() ")
phone_pattern <- optional(OPEN_PAREN) %R% 
  three_digits %R% 
  zero_or_more(separator) %R% 
  three_digits %R% 
  zero_or_more(separator) %R%
  four_digits
  
# Extract phone numbers
str_extract(contact, phone_pattern)

# Extract ALL phone numbers
str_extract_all(contact, phone_pattern)
