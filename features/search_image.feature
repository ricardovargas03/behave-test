Feature: Search koombea on google images
         As a user
         I want to search some words on google images
         So I want to view result images

  Scenario Outline: Find some images about koombea
     Given I open google images
     When I search any "<word>" on google
     Then I choose the image on the position "<number>"
     And  I save the image with desire file "<name>"

     Examples:
     |  word    |  number |     name       |
     |  Koombea |    3    |  koombea_team  |