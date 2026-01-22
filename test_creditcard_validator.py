class TestCreditCardValidator:
    "Test suite for testing credit card validation functions."

    # Karim Rivera-Apolinar
    # Date: Jan 22 2026
    # ======= Positive Cases =======
        
    def test_valid_visa_num_pos(self):
        """ Tests if the first number of visa card is 4 """
        assert credit_card_validator('4012888888881881') == True

    def test_valid_master_num_pos(self):
        """ Tests if the first number of master card is 51 - 55 or 2221 - 2720 """
        assert credit_card_validator('5555555555554444') == True

    def test_valid_amex_num_pos(self):
        """ Tests if the first number of american express is 34 or 37 """
        assert credit_card_validator('378282246310005') == True

    
    def test_valid_visa_len_pos(self):
        """ Tests if the length of visa is 16 """
        assert credit_card_validator('4012888888881881') == True

    def test_valid_master_len_pos(self):
        """ Tests if the length of master is 16 """
        assert credit_card_validator('5555555555554444') == True
    
    def test_valid_amex_len_pos(self):
        """ Tests if the length of american express is 15 """
        assert credit_card_validator('378282246310005') == True

   
     # ======= Negative Cases =======

    def test_valid_visa_num_neg(self):
        """ Tests if the first number of visa card is 4 """
        assert credit_card_validator('5012888888881888') == False

    def test_valid_master_num_neg(self):
        """ Tests if the first number of master card is 51 - 55 or 2221 - 2720 """
        assert credit_card_validator('3255555555554442') == False

    def test_valid_amex_num_neg(self):
        """ Tests if the first number of american express is 34 or 37 """
        assert credit_card_validator('858282246310004') == False

    
    def test_valid_visa_len_neg(self):
        """ Tests if the length of visa is 16 """
        assert credit_card_validator('401288888888188134') == False

    def test_valid_master_len_neg(self):
        """ Tests if the length of master is 16 """
        assert credit_card_validator('555555555555444426') == False
    
    def test_valid_amex_len_neg(self):
        """ Tests if the length of american express is 15 """
        assert credit_card_validator('37828224631005459') == False

    
    def test_visa_luhn_invalid_neg(self):
        """ Tests if the visa card number fails Luhn check """
        assert credit_card_validator("4012888888881882") is False

    def test_master_luhn_invalid_neg(self):
        """ Tests if the master card number fails Luhn check """
        assert credit_card_validator("5555555555554445") is False

    def test_amex_luhn_invalid_neg(self):
        """ Tests if the american express card number fails Luhn check """
        assert credit_card_validator("378282246310006") is False


    # ======= Boundary Value Tests =======

    # --- MasterCard 51–55 boundaries ---
    def test_mastercard_50_boundary(self):
        """ Tests MasterCard prefix just below valid range """
        assert credit_card_validator("5000000000000000") is False

    def test_mastercard_51_boundary(self):
        """ Tests MasterCard prefix at lower valid boundary """
        assert credit_card_validator("5105105105105100") is True

    def test_mastercard_55_boundary(self):
        """ Tests MasterCard prefix at upper valid boundary """
        assert credit_card_validator("5555555555554444") is True

    def test_mastercard_56_boundary(self):
        """ Tests MasterCard prefix just above valid range """
        assert credit_card_validator("5600000000000000") is False

    # --- MasterCard 2221–2720 boundaries ---

    def test_mastercard_2220_boundary(self):
        """ Tests MasterCard prefix just below valid range """
        assert credit_card_validator("2220000000000000") is False
    
    def test_mastercard_2221_boundary(self):
        """ Tests MasterCard prefix at lower valid boundary """
        assert credit_card_validator("2221000000000009") is True
    
    def test_mastercard_2720_boundary(self):
        """ Tests MasterCard prefix at upper valid boundary """
        assert credit_card_validator("2720999999999995") is True
    
    def test_mastercard_2721_boundary(self):
        """ Tests MasterCard prefix just above valid range """
        assert credit_card_validator("2721000000000000") is False

    # --- Visa Prefix Boundaries ---

    def test_visa_prefix_3_boundary(self):
        """ Tests Visa card prefix just below valid range """
        assert credit_card_validator("3012888888881881") is False

    def test_visa_prefix_4_boundary(self):
        """ Tests Visa card prefix at valid boundary """
        assert credit_card_validator("4012888888881881") is True

    def test_visa_prefix_5_boundary(self):
        """ Tests Visa card prefix just above valid range """
        assert credit_card_validator("5012888888881881") is False

    # --- American Express Prefix Boundaries ---

    def test_amex_prefix_33_boundary(self):
        """ Tests American Express card prefix just below valid range """
        assert credit_card_validator("331234567890123") is False
    
    def test_amex_prefix_34_boundary(self):
        """ Tests American Express card prefix at lower valid boundary """
        assert credit_card_validator("341234567890123") is True

    def test_amex_prefix_35_boundary(self):
        """ Tests American Express card prefix at upper valid boundary """
        assert credit_card_validator("351234567890124") is False

    def test_amex_prefix_36_boundary(self):
        """ Tests American Express card prefix just above valid range """
        assert credit_card_validator("361234567890123") is False
    
    def test_amex_prefix_37_boundary(self):
        """ Tests American Express card prefix at upper valid boundary """
        assert credit_card_validator("371234567890123") is True

    def test_amex_prefix_38_boundary(self):
        """ Tests American Express card prefix just above valid range """
        assert credit_card_validator("381234567890123") is False


        
    # --- Length Boundaries ---
    
    def test_visa_length_15(self):
        """ Tests Visa card number with 15 digits """
        assert credit_card_validator("401288888888188") is False

    def test_visa_length_16(self):
        """ Tests Visa card number with 16 digits """
        assert credit_card_validator("4012888888881881") is True

    def test_visa_length_17(self):
        """ Tests Visa card number with 17 digits """
        assert credit_card_validator("40128888888818811") is False

    def test_master_length_15(self):
        """ Tests MasterCard number with 15 digits """
        assert credit_card_validator("555555555555444") is False

    def test_master_length_16(self):
        """ Tests MasterCard number with 16 digits """
        assert credit_card_validator("5555555555554444") is True

    def test_master_length_17(self):
        """ Tests MasterCard number with 17 digits """
        assert credit_card_validator("55555555555544445") is False

    def test_amex_length_14(self):
        """ Tests American Express card number with 14 digits """
        assert credit_card_validator("37828224631000") is False

    def test_amex_length_15(self):
        """ Tests American Express card number with 15 digits """
        assert credit_card_validator("378282246310005") is True 

    def test_amex_length_16(self):
        """ Tests American Express card number with 16 digits """
        assert credit_card_validator("3782822463100050") is False