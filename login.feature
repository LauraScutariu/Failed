Feature:Login to https://twitter.com/
  Scenario: Login successful
    Given I am on the login page
    When I enter the correct username
    And I enter the correct password
    And I click the login button
    Then I should be redirected to the my account

  Scenario: Unsuccessful Login(negative username)
    Given I am on the login page
    When I enter the wrong username
    And I enter the correct password
    And I click the login button
    Then I should be prompted with an error message

  Scenario: Unsuccessful Login(negative password)
    Given I am on the login page
    When I enter the correct username
    And I enter the wrong password
    And I click the login button
    Then I should be prompted with an error message